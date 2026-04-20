import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print(os.environ.get("OPENAI_API_KEY"))    
    print("Hello from cursor-ai!")

if __name__ == "__main__":
    main()
