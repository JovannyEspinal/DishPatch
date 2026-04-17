from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from dishpatch.models import StackState
from dishpatch.nodes import orchestrator_node, menu_agent_node, order_agent_node, synthesizer_node
from dishpatch.tools.menu_tools import menu_tools_list
from dishpatch.tools.order_tools import order_tools_list
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

def build_graph():
    builder = StateGraph(StackState)

    builder.add_node("orchestrator_node", orchestrator_node)
    builder.add_node("menu_agent_node", menu_agent_node)
    builder.add_node("menu_tools_node", ToolNode(menu_tools_list, messages_key="menu_messages"))
    builder.add_node("order_agent_node", order_agent_node)
    builder.add_node("order_tools_node", ToolNode(order_tools_list, messages_key="order_messages"))
    builder.add_node("synthesizer_node", synthesizer_node)

    builder.add_edge(START, "orchestrator_node")
    builder.add_edge("menu_tools_node", "menu_agent_node")
    builder.add_edge("order_tools_node", "order_agent_node")
    builder.add_edge("synthesizer_node", END)

    return builder.compile(checkpointer=MemorySaver())

graph = build_graph()