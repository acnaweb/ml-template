requirements:
	pip install -r requirements.txt

create_repository: 
	chmod +x scripts/create_repository.sh
	scripts/create_repository.sh	

run_etl: clean
	python src/app/data/make_dataset.py

clean: 
	scripts/clean.sh	

setup: clean
	chmod +x scripts/*
	scripts/create_folder.sh
	unset MLFLOW_TRACKING_URI

run_train: 
	python src/app/models/train_model.py

batch: 
	python src/app/models/predict_model.py

serve:
	python src/app/models/api.py

lint:
	flake8 
