import mlflow

# Base de datos separada para esta actividad
mlflow.set_tracking_uri("sqlite:///hello_mlflow.db")

# Nombre del experimento
mlflow.set_experiment("Hello World MLflow")

# Crear un archivo para usarlo como artifact
with open("hello_artifact.txt", "w") as archivo:
    archivo.write("Hello World desde MLflow")

# Iniciar un run
with mlflow.start_run():

    mlflow.log_param("modelo", "hello_world")
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("hello_artifact.txt")

    print("Experimento registrado correctamente")