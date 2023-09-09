.PHONY: run
run: # Run the service.
		@cd src/ && poetry run python manage.py runserver 0.0.0.0:8080

.PHONY: migrate
migrate: # Apply the latest migrations.
		@cd src/ && poetry run python manage.py migrate

.PHONY: importdata
importdata: # Fill in the database.
		@cd src/ && poetry run python manage.py importdata ../data/data-5-structure-1.csv

.PHONY: up
up: # Create and launch service containers.
		docker compose up -d

.PHONY: db
db: # Launch database container.
		docker compose up -d db

.PHONY: psql
psql: # Log in to the service database.
		docker compose exec db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

.PHONY: nice
nice: # Format the code.
		poetry run python -m pyclean -v src/
		poetry run python -m isort src/
		poetry run python -m black src/

.PHONY: env
env: # Create .env file with variables.
		@cp configuration/.env.example .env

.PHONY: help
help: # Show help for each of the Makefile recipes.
		@grep -E '^[a-zA-Z0-9 -]+:.*#' Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done
