# from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader, UnstructuredMarkdownLoader
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_community.document_loaders import ToMarkdownLoader
import markdown
import os


def scrapUrl(valid_url):
    loader = ToMarkdownLoader(
        url=valid_url,
        api_key=os.getenv('MD_API_KEY')
    )
    print(loader['error'])
    print(loader['article'])
    docs = loader.load()

    assert len(docs) == 1
    assert isinstance(docs[0], Document)
    resumed_text = docs[0].page_content
    html_resumed_text = markdown.markdown(resumed_text)

    return html_resumed_text
