# agent_fun.py
import asyncio, json, sys, os
from typing import Dict, Any, List
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from groq import Groq

# ----------------------
# GROQ Client
# ----------------------
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

def groq_chat(messages: List[Dict[str, str]], temperature=0.2) -> str:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature
    )
    return resp.choices[0].message.content


SYSTEM = (
    "You are a cheerful weekend helper. You can call MCP tools."
    "Decide step-by-step (ReAct). If you need a tool, output ONLY JSON:"
    '{"action":"","args":{...}}'
    "If you can answer, output ONLY JSON:"
    '{"action":"final","answer":"..."}'
)


# ----------------------
# JSON forcing wrapper
# ----------------------
def llm_json(messages: List[Dict[str, str]]) -> Dict[str, Any]:
    txt = groq_chat(messages, temperature=0.2)

    try:
        return json.loads(txt)
    except Exception:
        # force valid JSON
        fixed = groq_chat(
            [
                {"role": "system", "content": "Return ONLY valid JSON."},
                {"role": "user", "content": txt}
            ],
            temperature=0
        )
        return json.loads(fixed)


# ----------------------
# Main MCP Agent
# ----------------------
async def main():
    server_path = sys.argv[1] if len(sys.argv) > 1 else "server_fun.py"

    exit_stack = AsyncExitStack()
    stdio = await exit_stack.enter_async_context(
        stdio_client(
            StdioServerParameters(command=sys.executable, args=[server_path])
        )
    )

    r_in, w_out = stdio
    session = await exit_stack.enter_async_context(ClientSession(r_in, w_out))
    await session.initialize()

    tools = (await session.list_tools()).tools
    tool_index = {t.name: t for t in tools}
    print("Connected tools:", list(tool_index.keys()))

    history = [{"role": "system", "content": SYSTEM}]

    try:
        while True:
            user = input("You: ").strip()
            if not user or user.lower() in {"exit", "quit"}:
                break

            history.append({"role": "user", "content": user})

            for _ in range(4):
                decision = llm_json(history)

                # Final answer
                if decision.get("action") == "final":
                    answer = decision.get("answer", "")

                    # Reflection step
                    reflect = groq_chat(
                        [
                            {
                                "role": "system",
                                "content": "Check for mistakes or missing tool calls. If fine, reply 'looks good'; else give corrected answer."
                            },
                            {"role": "user", "content": answer}
                        ],
                        temperature=0
                    )

                    if reflect.strip().lower() != "looks good":
                        answer = reflect

                    print("Agent:", answer)
                    history.append({"role": "assistant", "content": answer})
                    break

                # Tool call
                tname = decision.get("action")
                args = decision.get("args", {})

                if tname not in tool_index:
                    history.append({"role": "assistant", "content": f"(unknown tool {tname})"})
                    continue

                result = await session.call_tool(tname, args)
                payload = (
                    result.content[0].text
                    if result.content
                    else result.model_dump_json()
                )

                history.append({"role": "assistant", "content": f"[tool:{tname}] {payload}"})

    finally:
        await exit_stack.aclose()


if __name__ == "__main__":
    asyncio.run(main())
