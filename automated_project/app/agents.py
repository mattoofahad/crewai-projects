from crewai import Agent
from utils.config import AGENTS_CONFIG


class AgentsClass:
    PROJECT_PLANNING_AGENT = Agent(config=AGENTS_CONFIG["project_planning_agent"])
    ESTIMATION_AGENT = Agent(config=AGENTS_CONFIG["estimation_agent"])
    RESOURCE_ALLOCATION_AGENT = Agent(config=AGENTS_CONFIG["resource_allocation_agent"])
