from crewai import Crew

from app.agents import AgentsClass
from app.tasks import TasksClass


class CrewClass:
    AUTOMATE_PROJECT_CREW = Crew(
        agents=[
            AgentsClass.PROJECT_PLANNING_AGENT,
            AgentsClass.ESTIMATION_AGENT,
            AgentsClass.RESOURCE_ALLOCATION_AGENT,
        ],
        tasks=[
            TasksClass.TASK_BREAKDOWN,
            TasksClass.TIME_RESOURCE_ESTIMATION,
            TasksClass.RESOURCE_ALLOCATION,
        ],
        verbose=False,
    )
