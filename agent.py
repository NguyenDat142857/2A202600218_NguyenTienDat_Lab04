from typing import Annotated, List
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from tools import search_flights, search_hotels, calculate_budget

from dotenv import load_dotenv
import os


# ========================
# LOAD ENV
# ========================
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("❌ Missing OPENROUTER_API_KEY")


# ========================
# LOAD PROMPT
# ========================
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


# ========================
# STATE
# ========================
class AgentState(TypedDict):
    messages: Annotated[List, add_messages]


# ========================
# TOOLS
# ========================
tools_list = [
    search_flights,
    search_hotels,
    calculate_budget
]


# ========================
# LLM (FREE 120B 🔥)
# ========================
llm = ChatOpenAI(
    model="openai/gpt-oss-120b:free",  # 🔥 MODEL MỚI
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3,
)


# ⚠️ bind_tools vẫn giữ (nhưng không phụ thuộc)
llm_with_tools = llm.bind_tools(tools_list)


# ========================
# AGENT NODE
# ========================
def agent_node(state: AgentState):
    messages = state["messages"]

    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    print("\n🧠 Agent đang suy nghĩ...")

    try:
        response = llm_with_tools.invoke(messages)
    except Exception as e:
        print("❌ LLM error:", e)
        return {"messages": [HumanMessage(content="Model error")]}

    # Debug tool call
    if hasattr(response, "tool_calls") and response.tool_calls:
        for tc in response.tool_calls:
            print(f"🛠 Tool: {tc['name']} | args: {tc['args']}")
    else:
        print("⚠️ Model không gọi tool (bình thường với free model)")

    return {"messages": [response]}


# ========================
# GRAPH
# ========================
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools_list))

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()


# ========================
# RUN CHAT
# ========================
def run_chat():
    print("✈️ TravelBuddy AI (FREE 120B) - type 'quit'\n")

    messages = []

    while True:
        user_input = input("Bạn: ")

        if user_input.lower() == "quit":
            print("👋 Bye!")
            break

        messages.append(HumanMessage(content=user_input))

        try:
            result = graph.invoke({
                "messages": messages
            })
        except Exception as e:
            print("❌ Graph error:", e)
            continue

        last_msg = result["messages"][-1]

        print("🤖 TravelBuddy:", last_msg.content)

        messages = result["messages"]


# ========================
# MAIN
# ========================
if __name__ == "__main__":
    run_chat()