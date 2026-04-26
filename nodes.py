from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE="""
You are a ReAct agent.
You MUST use tools when they are relevant.
Do NOT describe tool calls in text.
Do NOT write JSON manually.
Use the tool calling interface directly.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node
    """
    messages = state["messages"]
    response = llm.invoke([{"role":"system","content":SYSTEM_MESSAGE}, *state["messages"]])

    return {
        "messages": messages + [response]
    }


tool_node = ToolNode(tools)