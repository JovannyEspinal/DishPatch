from typing import Literal
from langchain_core.messages import SystemMessage
from langgraph.types import Command
from dishpatch.models import StackState
from dishpatch.llms import menu_llm
from dishpatch.prompts import MENU_AGENT_PROMPT
from dishpatch.tools.menu_tools import menu_tools_list
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

_llm = menu_llm.bind_tools(menu_tools_list)

def menu_agent_node(state: StackState) -> Command[Literal["menu_tools_node", "synthesizer_node"]]:
    logger.info("Menu agent started")
    local = [SystemMessage(content=MENU_AGENT_PROMPT)] + state["messages"] + state.get("menu_messages", [])
    response = _llm.invoke(local)

    if response.tool_calls:
        logger.info(f"Menu agent calling tool: {response.tool_calls[0]['name']}")
        return Command(goto="menu_tools_node", update={"menu_messages": [response]})

    logger.info("Menu agent finished")
    return Command(goto="synthesizer_node", update={"menu_response": response.content, "menu_messages": [response]})
