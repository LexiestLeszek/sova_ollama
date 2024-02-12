### Sova

## Description

Sova is a web search engine that utilizes power of Large Language Models (LLM) to return full text answer instead of bunch of links like traditional search engines do.

## Installation

Before installing Sova, ensure you have Python installed on your system. You will also need pip, which is typically included with Python.

To install Sova, follow these steps:

1. Clone the repository using this command in terminal: `git clone https://github.com/LexiestLeszek/sova_ollama.git`
2. Install the required dependencies using this command in terminal: `pip install -r requirements.txt`
3. Install Ollama from their website https://ollama.com/
4. Download the local LLM (in our case - qwen:1.8b) using this command in terminal: `ollama pull qwen:1.8b`
5. Run the gunicorn server using this command in terminal: `gunicorn -b 0.0.0.0:8080 app:app`
6. Use the search-bar to input your search query or or question.

