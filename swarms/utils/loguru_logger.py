import os
import sys
from dotenv import load_dotenv
from loguru import logger

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

load_dotenv()

print("Current PYTHONPATH:", sys.path)

WORKSPACE_DIR = os.getenv("WORKSPACE_DIR", os.getcwd())

def get_log_path(file_path: str) -> str:
    return os.path.join(WORKSPACE_DIR, file_path)

logger.add(
    get_log_path("swarms.log"),
    level="INFO",
    colorize=True,
    backtrace=True,
    diagnose=True,
)

def loguru_logger(file_path: str = "swarms.log"):
    return logger.add(
        get_log_path(file_path),
        level="INFO",
        colorize=True,
        backtrace=True,
        diagnose=True,
    )
