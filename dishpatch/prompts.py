from pathlib import Path

PROMPTS_DIR = Path(__file__).parent / "prompts"

def load_prompt(name: str) -> str:
    return (PROMPTS_DIR / f"{name}.txt").read_text(encoding="utf-8")

ORCHESTRATOR_PROMPT = load_prompt("orchestrator")
MENU_AGENT_PROMPT = load_prompt("menu_agent")
ORDER_AGENT_PROMPT = load_prompt("order_agent")
