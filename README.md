# ml-template

## Instalação

### 1 - Pré-requisitos

#### Git & Git Flow
- sudo apt install git git-flow

#### Github client (gh)
- wget https://github.com/cli/cli/releases/download/v2.10.1/gh_2.10.1_linux_amd64.deb
- sudo apt install ./gh_2.10.1_linux_amd64.deb

#### Conda Environment
- conda create --name ml-python-3.8 python=3.8.5
- conda activate ml-python-3.8

#### Cookiecutter tool
- pip install cookiecutter 

### 2 - Criação de Repositório

#### Cookiecutter 
- cookiecutter https://github.com/trybe/ml-template.git
	
### 3 - Setup

#### Conda environment
- cd project-folder/
- conda create --name [env_name] python=3.8.5
- conda activate [env_name]

#### Repositorio
- make requirements
- make create_repository
	- verificar o respoitorio criado em https://github.com/betrybe/[repositorio]
- make setup
	
## Ciencia de Dados	

src/app/data/
settings.CREATE_PROFILER

DataIngestion.load
	"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
	
DataIngestion.validate_data

DataPreparation.set_header
	["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "target"]
	
	make run_etl			
		data/*
		reports/*


--------------------------------------------------
MLFlow	
project-folder/mlflow ui --host 0.0.0.0

--------------------------------------------------
src/app/models/
settings.EXPERIMENT_NAME (MLFlow)
settings.params = {}

model.Model - Extends AlgoritmModel
	from sklearn.linear_model import LogisticRegression
	LogisticRegression
	
model.train
model.validate_training	
model.evaluate_performance

experiment.track_performance_metrics 		
	
	make run_train
		MLflow
			
--------------------------------------------------
src/app/models/
predict_model.get_dataset
predict_model.logged_model = 
			generalizar por model/ no MLFlow
			'runs:/[id]'
				
	make batch
		data/*				
--------------------------------------------------	
src/app/models/
api.logged_model = 
			generalizar por model/ no MLFlow
			'runs:/[id]'	
			
api.columns 
	["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm"]
	
	make serve
		POST http://127.0.0.1:8080/invocations
{
    "sepal length in cm": 4.9,
    "sepal width in cm": 3.0,
    "petal length in cm": 1.4,
    "petal width in cm": 0.2
}



### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.│
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
├── scripts            <- scripts for make
│
├── src/app                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── conf       	<- Used for general configurations
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│                       predictions
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## References

[See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

