from typing import Literal
from langchain_core.messages import SystemMessage
from langgraph.types import Command, Send
from dishpatch.models import StackState, RouteDecision
from dishpatch.llms import orchestrator_llm
from dishpatch.prompts import ORCHESTRATOR_PROMPT
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

_llm = orchestrator_llm.with_structured_output(RouteDecision)

def orchestrator_node(state: StackState) -> Command[Literal["menu_agent_node", "order_agent_node"]]:
    logger.info(f"Orchestrator received: {state['user_query']}")
    system = SystemMessage(content=ORCHESTRATOR_PROMPT)
    result: RouteDecision = _llm.invoke([system] + state["messages"])
    logger.info(f"Routing to: {result.agents} | Reason: {result.reasoning}")

    sends = [Send(f"{agent}_node", state) for agent in result.agents]
    return Command(goto=sends, update={"route": result.agents})