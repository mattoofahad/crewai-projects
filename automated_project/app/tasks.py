from app.agents import AgentsClass
from app.models import ProjectPlan
from crewai import Task
from utils.config import TASKS_CONFIG


class TasksClass:
    TASK_BREAKDOWN = Task(
        config=TASKS_CONFIG["task_breakdown"], agent=AgentsClass.PROJECT_PLANNING_AGENT
    )

    TIME_RESOURCE_ESTIMATION = Task(
        config=TASKS_CONFIG["time_resource_estimation"],
        agent=AgentsClass.ESTIMATION_AGENT,
    )

    RESOURCE_ALLOCATION = Task(
        config=TASKS_CONFIG["resource_allocation"],
        agent=AgentsClass.RESOURCE_ALLOCATION_AGENT,
        output_pydantic=ProjectPlan,
    )
