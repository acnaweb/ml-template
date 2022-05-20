# Cookiecutter Data Science

#### Pre-req

* sudo apt install git git-flow
* gh
 * wget https://github.com/cli/cli/releases/download/v2.10.1/gh_2.10.1_linux_amd64.deb
	* sudo apt install ./gh_2.10.1_linux_amd64.deb
* conda create --name ml-python-3.8 python=3.8.5
* conda activate ml-python-3.8
* pip install cookiecutter 

linha 1  
linha 2
linha 3  
linha 4

#### 1- Duplicação de repositórios
* criar repositório tool
	git@github.com:acnaweb/ml-tool.git
	
* criar repositório template
	git@github.com:acnaweb/ml-template.git
 
	* Configurar como "Template Repository"
		https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-template-repository
		https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
		
	
#### 2-Gitflow
* git@github.com:acnaweb/ml-template.git	
	* git flow init
	* git push
	* setup default branch

* git@github.com:acnaweb/ml-tool.git
	* git flow init
	* git push
	* setup default branch


#### 3 - Create new from ml-template
Base: http://drivendata.github.io/cookiecutter-data-science/

* cookiecutter https://github.com/acnaweb/ml-template.git
* cookiecutter ml-template

* Option 1
	* gh repo create modelo-will --template="acnaweb/ml-template" --private
	* gh repo create {{new_repo}} --template="acnaweb/ml-template" --private

* Option 2
	`
	- gh repo create "${{user}}/${{repository}}" --private
	- git init
	- git add . && git commit -m "init"
	- git branch -M main
	- git remote add origin https://github.com/${{user}}/${{repository}}.git
	- git push -u origin main
	`
	
#### 4- Setup requirements
- git@github.com:acnaweb/ml-template.git	

- Instructions
	- make
	- make create_environment
	- make requirements

#### Fluxo
- Data
	- make data

- Train




_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.8+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

### New version of Cookiecutter Data Science
------------
Cookiecutter data science is moving to v2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work, and this version of the template will still be available.
To use the legacy template, you will need to explicitly use `-c v1` to select it.
Please update any scripts/automation you have to append the `-c v1` option (as above),
which is available now.


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
