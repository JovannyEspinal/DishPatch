from typing import Literal
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.types import Command, interrupt
from dishpatch.models import StackState
from dishpatch.llms import order_llm
from dishpatch.prompts import ORDER_AGENT_PROMPT
from dishpatch.tools.order_tools import order_tools_list
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

_llm = order_llm.bind_tools(order_tools_list)

def order_agent_node(state: StackState) -> Command[Literal["order_tools_node", "synthesizer_node", "order_agent_node"]]:
    logger.info("Order agent started")
    local = [SystemMessage(content=ORDER_AGENT_PROMPT)] + state["messages"] + state.get("order_messages", [])
    response = _llm.invoke(local)

    if response.tool_calls:
        logger.info(f"Order agent calling tool: {response.tool_calls[0]['name']}")
        return Command(goto="order_tools_node", update={"order_messages": [response]})

    if response.content.strip().endswith("?"):
        user_input = interrupt(response.content)
        logger.info(f"HITL resumed with: {user_input}")
        return Command(goto="order_agent_node", update={"messages": [HumanMessage(content=user_input)]})

    logger.info("Order agent finished")
    return Command(goto="synthesizer_node", update={"order_response": response.content, "order_messages": [response]})