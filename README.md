### Sova

## Installation

Before installing Sova, ensure you have Python installed on your system. You will also need pip, which is typically included with Python.

To install Sova, follow these steps:

1. Clone the repository: git clone https://github.com/LexiestLeszek/sova_ollama.git
2. Install the required dependencies: `pip install -r requirements`
3. Download the local llm: `ollama run tinydolphin`
4. Run the gunicorn server: `gunicorn -b 0.0.0.0:8080 app:app`

