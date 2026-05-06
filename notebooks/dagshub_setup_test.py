import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/kanhacoderx/MoodSense-AI.mlflow')

dagshub.init(repo_owner='kanha-here',repo_name='MoodSense-AI',mlflow=True)


with mlflow.start_run():
    mlflow.log_param('parameter name','value')