### Sova

## Description

Sova is a web search engine that utilizes power of Large Language Models (LLM) to return full text answer instead of bunch of links like traditional search engines do.

## Installation

Before installing Sova, ensure you have Python installed on your system. You will also need pip, which is typically included with Python.

To install Sova, follow these steps:

1. Clone the repository: `git clone https://github.com/LexiestLeszek/sova_ollama.git`
2. Install the required dependencies: `pip install -r requirements`
3. Download the local LLM (in our case - qwen:0.5) : `ollama run qwen:0.5b`
4. Run the gunicorn server: `gunicorn -b 0.0.0.0:8080 app:app`
5. Use the search-bar to input your search querier or questions.

