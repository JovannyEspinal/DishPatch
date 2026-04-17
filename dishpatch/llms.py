from langchain_openai import ChatOpenAI
from dishpatch.config import (
    ORCHESTRATOR_MODEL, ORCHESTRATOR_TEMP,
    MENU_AGENT_MODEL, MENU_AGENT_TEMP,
    ORDER_AGENT_MODEL, ORDER_AGENT_TEMP,
    SYNTHESIZER_MODEL,
)
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

orchestrator_llm = ChatOpenAI(model=ORCHESTRATOR_MODEL, temperature=ORCHESTRATOR_TEMP)
menu_llm = ChatOpenAI(model=MENU_AGENT_MODEL, temperature=MENU_AGENT_TEMP)
order_llm = ChatOpenAI(model=ORDER_AGENT_MODEL, temperature=ORDER_AGENT_TEMP)
synthesizer_llm = ChatOpenAI(model=SYNTHESIZER_MODEL, temperature=0.0)
