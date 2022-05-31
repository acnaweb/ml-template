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

#### ETL
- src/app/data/settings
	- CREATE_PROFILER
		- True - gerar relatórios automaticamente 
		- False - não gerar relatórios automaticamente

- src/app/data/data_ingestion.py
	- DataIngestion.load() - implementar o data source
	- DataIngestion.validate_data() - implementar a validação dos dados
	
- src/app/data/data_prep.py
	- DataPreparation.set_header() - implementar o header do dataser		
	
- run	
	- make run_etl			
		- output: data/*
		- output: reports/*

--------------------------------------------------
MLFlow	
project-folder/mlflow ui --host 0.0.0.0

#### Experimento
- src/app/models/settings.py
	- EXPERIMENT_NAME - configurar o nome do experimento no ML Flow
	- params = configurar o dicionário de hiperparâmetros

- src/app/models/model.py
	- Model - extender a classe base para o algoritmo		
	- Model.train() - definir algoritmo de treinamento
	- model.validate_training()  - definir algoritmo de validação
	- model.evaluate_performance() - definir algoritmo de avaliação 

- src/app/models/experiment
	- track_performance_metrics() - parâmetros com tracking no ML Flow	

- run	
	- make run_train
		- ouptput: MLflow			 	
			
#### Predição em batch

- src/app/models/predict_model.py
	- get_dataset() - dataset para predição
	- logged_model = id do modelo no MLFlow			
- make batch
	- output: data/*

#### Predição online

- src/app/models/api.py
	- logged_model = id do modelo no MLFlow			
	- columns = nomes dos atributos no json recebido pelo POST

- make serve
	- POST http://127.0.0.1:8080/invocations
Data:
{
    "attr1": 1,
    "attr2": 0.5,
    ...
    "attrN": 2,
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

