from flask import Flask, render_template, request
from googlesearch import search
import re
import translators as ts
import gunicorn
import requests
import ollama
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

app = Flask(__name__)

def get_context(question):
    print("Init Search")
    search_results = search(question, num=5, stop=5, pause=2)
    top_links = list(search_results)
    exclude_list = ["google", "facebook", "twitter", "instagram", "youtube", "tiktok", "kremlin"]
    top_links = [link for link in top_links if not any(domain in link for domain in exclude_list)]
    scraped_texts = []
    for link in top_links:
        print(link)
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            text = ' '.join([p.get_text() for p in soup.find_all('p')])
            print(text)
        except Exception as e:
            print(f"Failed to scrape the link: {link}\nError: {e}")
        scraped_texts.append(text)

    all_scraped_text = '.\n'.join(scraped_texts)
    
    print(all_scraped_text)
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    documents = text_splitter.split_text(all_scraped_text)
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

    db = Chroma.from_texts(documents, embedding=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    
    context = retriever.get_relevant_documents(question)

    return context

# Function to generate output using the LLM model
def generate_output(question,context):
    # Prepare the prompt with the input text
    # Define a prompt template
    prompt = f"""Use the following context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Answer only factual information based on the context below.
    Context: {context}.\n
    Question: {question}\n
    Helpful Answer:"""
    
    response = ollama.chat(model='qwen:1.8b', messages=[
        
        {
            'role': 'system',
            'content': 'You are a Helpful AI assistant that answers based on the information from the user prompt Context and nothing else.',
            
            'role': 'user',
            'content': f'{prompt}',
            },
        ])
    
    output = response['message']['content']
    
    # Return the generated text
    return output

@app.route('/', methods=['GET', 'POST'])
def index():
    query = ""
    answer = ""

    if request.method == 'POST':
        query = request.form['query']

        if query:
        
            context = get_context(query)
            
            # Generate the output using the LLM model
            answer = generate_output(query,context)
            
            print(answer)

    return render_template('index.html', query=query, answer=answer)

#if __name__ == '__main__':
#    app.run(debug=True, port="8021")

# to run on ngrok:    
# 1. in main Mac terminal: "ngrok http 8080"
# 2. run this app in IDE terminal: "gunicorn -b 0.0.0.0:8080 app:app"

# # Find the process running on port 8081
# lsof -ti tcp:PORT

# Kill the process (replace PID with the actual process ID)
# kill PID
