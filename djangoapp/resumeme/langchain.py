# from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader, UnstructuredMarkdownLoader
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_community.document_loaders import ToMarkdownLoader
# import markdown
import os

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
chain = load_summarize_chain(llm, chain_type="stuff")


def scrapUrl(valid_url):
    MD_API_KEY = os.getenv('MD_API_KEY')
    loader = ToMarkdownLoader(
        url=valid_url,
        api_key=MD_API_KEY
    )

    docs = loader.load()
    result = chain.invoke(docs)

    return result['output_text']
