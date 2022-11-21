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

