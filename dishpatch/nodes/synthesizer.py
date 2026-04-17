from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.types import Command
from dishpatch.models import StackState
from dishpatch.llms import synthesizer_llm
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

_SYSTEM = """You are the final response synthesizer for DishPatch.
Combine the provided agent responses into a single, friendly, coherent reply.
If only one agent responded, clean it up and present it directly.
Do not mention agents or internal routing to the user."""

def synthesizer_node(state: StackState) -> dict:
    logger.info("Synthesizer started")
    parts = []
    if state.get("menu_response"):
        parts.append(f"Menu Agent: {state['menu_response']}")
    if state.get("order_response"):
        parts.append(f"Order Agent: {state['order_response']}")

    combined = "\n\n".join(parts)
    response = synthesizer_llm.invoke([
        SystemMessage(content=_SYSTEM),
        HumanMessage(content=combined)
    ])

    logger.info("Synthesizer finished")
    return {"final_answer": response.content}