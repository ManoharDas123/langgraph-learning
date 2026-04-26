from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama


load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3

tools = [TavilySearch(max_result=1), triple]

# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
llm = ChatOllama(
    model="llama3.1",                  # <-- chat-capable
    temperature=0
).bind_tools(tools)