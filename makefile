############################################################### SETUP ###################################################################

create-venv:
	python3 -m venv .venv

setup:
	pip install -r requirements.txt;


############################################################# DELPOY LIVE ###############################################################

deploy-default:
	gcloud app deploy app.yaml --no-cache --promote --version=cache

deploy-local:
	FLASK_APP=main.py flask run

deploy-queue:
	gcloud app deploy queue.yaml


########################################################### BUILD & DELPOY ##############################################################

## USE WITH CAUTION - DEPLOYS EVEN IF BUILD FAILS
build-deploy-default:
	make build;
	make deploy-default;

build-deploy-local:
	make build;
	make deploy-local;


