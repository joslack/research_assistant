import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from index import read_pdfs, vectorize_pages

load_dotenv()

def main():     
    # TODO: load and vectorize pdf content
    vectorize_pages(read_pdfs())
    # TODO: output a list of the papers
    
    # infinite loop
    # TODO: use user input to find a specific paper, and find the content most likely to be associated with their query

    # TODO: generate a prompt with langchain

    # TODO: use gpt turbo to ingest and answer the question
    # user_input = input("Enter a question about AI: ")
    # template = f"You are an expert in the field of Artificial Intelligence, answer the following question: {user_input}"
    
    # openaichat = OpenAI(temperature=0.5)
    # response = openaichat(template)
    # print(response)




if __name__ == "__main__":
    main()
    