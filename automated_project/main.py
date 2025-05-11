# Warning control
import warnings

from app.crew import CrewClass
from data.input import INPUTS
from utils.utils import (
    calculate_cost,
    display_milestones,
    display_tasks,
    display_usage_metrics,
)

warnings.filterwarnings("ignore")

crew = CrewClass.AUTOMATE_PROJECT_CREW
result = crew.kickoff(inputs=INPUTS)

calculate_cost(crew)
display_usage_metrics(crew)
display_tasks(result)
display_milestones(result)
