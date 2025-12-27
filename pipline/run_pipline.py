from google.cloud import aiplatform
from kfp.v2 import compiler
from pipeline.churn_pipeline import churn_pipeline

PROJECT_ID = "mlopsbasico"
REGION = "us-central1"
PIPELINE_ROOT = "gs://mlopsbucket12/pipelines"

aiplatform.init(project=PROJECT_ID, location=REGION)

compiler.Compiler().compile(
    pipeline_func=churn_pipeline,
    package_path="churn_pipeline.json"
)

job = aiplatform.PipelineJob(
    display_name="churn-mlops-pipeline",
    template_path="churn_pipeline.json",
    pipeline_root=PIPELINE_ROOT,
    parameter_values={
        "data_path": "gs://mlopsbucket12/data/telco.csv"
    }
)

job.run(sync=False)
