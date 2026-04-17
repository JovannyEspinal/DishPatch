import uuid
from langgraph.types import Command
from langchain_core.messages import HumanMessage
from dishpatch.graph import graph
from dishpatch.logger import setup_logger

logger = setup_logger(__name__)

class DishPatchAssistant:
    def __init__(self):
        self.thread_id = str(uuid.uuid4())

    def _config(self) -> dict:
        return {"configurable": {"thread_id": self.thread_id}}

    def ask(self, user_input: str) -> str:
        state = {"user_query": user_input, "messages": [HumanMessage(content=user_input)]}
        result = graph.invoke(state, config=self._config())

        while True:
            snapshot = graph.get_state(config=self._config())
            if not snapshot.next:
                break

            interrupts = [i for task in snapshot.tasks for i in task.interrupts]
            if not interrupts:
                break

            interrupt_value = interrupts[0].value
            answer = input(f"\n DishPatch: {interrupt_value}\n You: ").strip()
            result = graph.invoke(Command(resume=answer), config=self._config())

        return  result.get("final_answer", "Sorry, I couldn't process that.")

    def reset(self):
        self.thread_id = str(uuid.uuid4())
        logger.info("Conversation reset")

def run_text_loop():
  assistant = DishPatchAssistant()
  print("\nWelcome to DishPatch! Type 'quit' to exit or 'reset' to start over.\n")

  while True:
      user_input = input("You: ").strip()
      if not user_input:
          continue
      if user_input.lower() == "quit":
          print("Goodbye!")
          break
      if user_input.lower() == "reset":
          assistant.reset()
          print("Conversation reset.\n")
          continue

      response = assistant.ask(user_input)
      print(f"\nDishPatch: {response}\n")

def main():
    run_text_loop()

if __name__ == "__main__":
    main()