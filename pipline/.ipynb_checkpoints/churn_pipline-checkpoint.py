from kfp.v2 import dsl
NAME_PROJECT='mlopsbasico'

@dsl.component(
    base_image=f"gcr.io/{NAME_PROJECT}/mlops-churn:latest"
)
def data_validation_op():
    import subprocess
    subprocess.run(
        ["python", "src/data_validation.py"],
        check=True
    )


@dsl.component(
    base_image=f"gcr.io/{NAME_PROJECT}/mlops-churn:latest"
)
def preprocessing_op():
    import subprocess
    subprocess.run(
        ["python", "src/preprocessing.py"],
        check=True
    )


@dsl.component(
    base_image=f"gcr.io/{NAME_PROJECT}/mlops-churn:latest"
)
def training_op():
    import subprocess
    subprocess.run(
        ["python", "src/train.py"],
        check=True
    )


@dsl.component(
    base_image=f"gcr.io/{NAME_PROJECT}/mlops-churn:latest"
)
def evaluation_op():
    import subprocess
    subprocess.run(
        ["python", "src/evaluate.py"],
        check=True
    )
