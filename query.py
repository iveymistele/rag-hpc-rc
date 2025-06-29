
import argparse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI 
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os
import openai 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "./chroma"

PROMPT_TEMPLATE = '''
Answer the question based only on the following context: {context}

---
Answer the question based on the above context: {question}

'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Query text")
    args = parser.parse_args()
    query_text = args.query

    embedding_func = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_func)

    results=db.similarity_search_with_relevance_scores(query_text, k=3) # top 3 most similar
    if len(results) == 0 or results[0][1] <0.7:
        print(f"Bad results ")
        return
    context_text = "\n\n--\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model= ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"

    print(formatted_response)


if __name__ == "__main__":
    main()


