import pandas as pd


def calculate_cost(crew):
    costs = (
        0.150
        * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens)
        / 1_000_000
    )
    print(f"Total costs: ${costs:.4f}")


def display_usage_metrics(crew):
    if crew is not None:
        df_usage_metrics = pd.DataFrame([crew.usage_metrics.model_dump()])
        print(df_usage_metrics)


def display_tasks(result):
    if result is not None:
        tasks = result.pydantic.model_dump()["tasks"]
        df_tasks = pd.DataFrame(tasks)
        print(df_tasks)


def display_milestones(result):
    if result is not None:
        milestones = result.pydantic.model_dump()["milestones"]
        df_milestones = pd.DataFrame(milestones)
        print(df_milestones)
