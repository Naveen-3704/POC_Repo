from pathlib import Path
from prefect import Flow, task
from prefect_dbt.cli.commands import DbtCoreOperation

@task
def trigger_dbt_flow(a):
    result = DbtCoreOperation(
        commands=["pwd", "dbt debug", "dbt run -s " + a],
        project_dir=Path(r"C:\Users\naveen.koyada\PycharmProjects\Snowflake_DBT_Project\dbt-env\Lib\site-packages\dbt\config"),
        profiles_dir=Path(r"C:\Users\naveen.koyada\PycharmProjects\Snowflake_DBT_Project\dbt-env\Lib\site-packages\dbt\config")
    ).run()
    return result

@Flow
def run_dbt(a):
    trigger_dbt_flow(a)

if __name__ == "__main__":
    run_dbt('dim_customer')