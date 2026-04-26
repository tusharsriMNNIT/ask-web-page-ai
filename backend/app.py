from flask import Flask, request, jsonify
from flask_cors import CORS
import time

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

app = Flask(__name__)
CORS(app)

print("Starting Flask server...")

model = ChatOllama(
    model="llama3:latest",
    temperature=0.7
)

print("Ollama model initialized.")

prompt = PromptTemplate(
    template="""
Answer the question:

{question}

Using this webpage content:

{text}
""",
    input_variables=["question", "text"]
)

parser = StrOutputParser()
chain = prompt | model | parser


@app.route("/ask", methods=["POST"])
def ask():
    try:
        start = time.time()

        print("\n========== NEW REQUEST ==========")

        data = request.json
        print("Received JSON:", data)

        url = data["url"]
        question = data["question"]

        print("URL:", url)
        print("Question:", question)

        print("\nLoading webpage using WebBaseLoader...")
        t1 = time.time()

        loader = WebBaseLoader(url)
        docs = loader.load()

        print(f"Webpage loaded in {round(time.time()-t1,2)} sec")

        if not docs:
            return jsonify({"answer": "No content found."})

        text = docs[0].page_content[:12000]

        print("Extracted text length:", len(text))
        print("Text preview:", text[:500])

        print("\nSending to Ollama...")
        t2 = time.time()

        answer = chain.invoke({
            "question": question,
            "text": text
        })

        print(f"Ollama responded in {round(time.time()-t2,2)} sec")
        print("Answer:", answer)

        print(f"Total request time: {round(time.time()-start,2)} sec")
        print("========== DONE ==========\n")

        return jsonify({"answer": answer})

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"answer": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)