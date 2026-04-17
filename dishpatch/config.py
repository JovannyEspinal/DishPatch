import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def load_config() -> dict:
    config_path = Path(__file__).parent / "config.yaml"

    with open(config_path) as f:
        return yaml.safe_load(f)

config = load_config()

ORCHESTRATOR_MODEL = config["models"]["orchestrator"]
MENU_AGENT_MODEL = config["models"]["menu_agent"]
ORDER_AGENT_MODEL = config["models"]["order_agent"]
SYNTHESIZER_MODEL = config["models"]["synthesizer"]
EMBEDDINGS_MODEL = config["models"]["embeddings"]

ORCHESTRATOR_TEMP = config["temperatures"]["orchestrator"]
MENU_AGENT_TEMP = config["temperatures"]["menu_agent"]
ORDER_AGENT_TEMP = config["temperatures"]["order_agent"]

RAG_TOP_K = config["rag"]["top_k"]
MAX_TOOL_ITERATIONS = config["agents"]["max_tool_iterations"]