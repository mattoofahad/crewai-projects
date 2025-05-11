# Add your utilities or helper functions to this file.
import os

import yaml
from dotenv import find_dotenv, load_dotenv

files = {"agents": "config/agents.yaml", "tasks": "config/tasks.yaml"}


# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService
def load_env():
    _ = load_dotenv(find_dotenv())


def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def load_configs():
    # Load configurations from YAML files
    configs = {}
    for config_type, file_path in files.items():
        with open(file_path, "r") as file:
            configs[config_type] = yaml.safe_load(file)

    return configs["agents"], configs["tasks"]


load_env()
AGENTS_CONFIG, TASKS_CONFIG = load_configs()

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
