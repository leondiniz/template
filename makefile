integration-tests:
	docker-compose -f docker-compose-tests.yaml stop
	docker-compose -f docker-compose-tests.yaml build
	docker-compose -f docker-compose-tests.yaml up --exit-code-from app-test

run:
	uvicorn app.main:app --reload

run_docker_app:
	docker-compose -f docker-compose.yaml stop
	docker-compose -f docker-compose.yaml build
	docker-compose -f docker-compose.yaml up

create_docker_postgresql-local:
	docker-compose -f docker-compose-postgresql.yaml stop
	docker-compose -f docker-compose-postgresql.yaml build
	docker-compose -f docker-compose-postgresql.yaml up

create_docker_mongo-local:
	docker-compose -f docker-compose.yaml stop
	docker-compose -f docker-compose.yaml build
	docker-compose -f docker-compose.yaml up	

create_docker_rabbitmq-local:
	docker-compose -f docker-compose-rabbitmq.yaml stop
	docker-compose -f docker-compose-rabbitmq.yaml build
	docker-compose -f docker-compose-rabbitmq.yaml up