from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from pydantic import BaseModel

class StackState(TypedDict):
    messages: Annotated[list, add_messages]
    menu_messages: Annotated[list, add_messages]
    order_messages: Annotated[list, add_messages]
    user_query: str
    route: list[str]
    menu_response: str
    order_response: str
    final_answer: str

class RouteDecision(BaseModel):
    agents: list[str]
    reasoning: str