# Prafull-LevelUp2-FinalAgent
<h1>Build an Agent with MCP tool and GroqAPi and Model</h1>


<h2>Prerequisites</h2>
<ul>
  <li>Python 3.11+</li>
  <li>Download llama3.2 from ollama (LLM model) (ollama pull llama3.2)</li>
  <li>Download mxbai-embed-large from ollama(embedding model)(ollama pull mxbai-embed-large)</li>
  <li>Or</li>
  <li>Create an API key on groq </li>
  <li>Use models that are avalilable on groq</li>
  <li>To set groq API key globally run this command - set GROQ_API_KEY=your_key_here </li>
  <li>To run the MCP inspector - required node js to install and then run  -  npx @modelcontextprotocol/inspector</li>
</ul>

<h2>Installation</h2>
<h3>1. Clone the repository:</h3>

```
git clone https://github.com/PS-Prafull-Panchori/1Prafull-LevelUp2-FinalAgent
cd "Project name"
```

<h3>2. Create a virtual environment</h3>

```
python -m venv venv
```

<h3>3. Activate the virtual environment</h3>

```
venv\Scripts\Activate

```

<h3>4. Install libraries</h3>

```
pip install "mcp>=1.2" requests ollama
pip install groq
```

<h3>
<ul>
<li><i>If you want to use ollama local - API KEy not required for Ollama)</i></li>
</ul>

<h2>Executing the scripts</h2>

- Open a terminal in VS Code

- Execute the following command:

```
python agent-fun.py

```
<h2>Note: Ignore SSL Certificate error

The error only affects analytics upload, your local chat UI still works at the shown URL. </h2>


 
