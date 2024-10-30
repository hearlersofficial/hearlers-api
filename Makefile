# service_server 마이그레이션 명령어
migrate-service-server-revision:
	cd services/service_server && poetry run alembic revision --autogenerate -m "service_a migration"

migrate-service-server-upgrade:
	cd services/service_server && poetry run alembic upgrade head

# service_b 마이그레이션 명령어
migrate-service-b-revision:
	poetry run alembic -c services/service_b/alembic.ini revision --autogenerate -m "service_b migration"

migrate-service-b-upgrade:
	poetry run alembic -c services/service_b/alembic.ini upgrade head

# 카프카 도커로 실행
kafka:
	docker-compose -f docker/docker-compose.yaml up -d --build

#서버 실행
run:
	./start.sh