# Prafull-LevelUp2-FinalAgent
<h1>Build an Agent with MCP tool and GroqAPi and Model</h1>

<h2>Prerequisites or setup to run MCP inspector</h2>
<ul>
  <li>1. Under env environment in python install this  - pip install "mcp[cli]"  </li>
  <li>2. After run this - mcp dev server_fun.py</li>
  <li>3. It ill open in browser where you can see the tools connected</li>
</ul>

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
<h2>Note: Stretch goal any of two -  </h2>
<ul>
<li>
1. Add a city_to_coords(city) tool using Open‑Meteo’s geocoding, so users can type a city instead of coordinates. - Done </li>
<li>2. Change model parameters like temperature, topP , and see how it impacts the results </li>

</ul>




 
