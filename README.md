
### Criando ambiente Virtual

```bash
python3 -m venv venv

source venv/bin/activate
```

### Instalando os requirements

``` bash
pip3 install --upgrade pip

pip3 install -r requirements.txt
```

### Criando o docker mongodb local

``` bash
make create_docker_mongo-local
```

### Criando o docker postgresql local

``` bash
make create_docker_postgresql-local
```

### Executando os fastapi

``` bash
make run
```

or

``` bash
make run_docker_app 
```

### Criando o token de acesso

Sem esse token de acesso, alguns endpoints ficam bloqueados.Para isso gere o token e na requisição envia-lo como Bearer token.

``` bash
curl --location --request POST 'https://dev-nzseols2.us.auth0.com/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: did=s%3Av0%3A72852440-28a0-11ed-8efc-85f3c24ebea9.AAi6EY3OjlGSbBWx%2FYAUSuNfFpa4i5A9Y%2BH%2BsLqGtoI; did_compat=s%3Av0%3A72852440-28a0-11ed-8efc-85f3c24ebea9.AAi6EY3OjlGSbBWx%2FYAUSuNfFpa4i5A9Y%2BH%2BsLqGtoI' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=FVjzOmoM02QG7mqxCjR70FvUbz7x6kn9' \
--data-urlencode 'client_secret=FeIP-eBGt0hkA5HAp2EA-V9qFZIL1YyUqw7-LOZsF_sgBPADRW_T82Gq3b65fBnO' \
--data-urlencode 'audience=template' \
--data-urlencode 'username=user_teste@gmail.com' \
--data-urlencode 'password=BBteste123_'
```

Um exemplo de requisição:

``` bash
curl --location --request POST 'http://127.0.0.1:8000/api/v1/ users?limit=0' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0Ijp7ImNvZGUiOiJhZG1pbiIsImVtYWlsIjoibGVkaXp0ZXN0ZSJ9LCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3NjMzODc0LCJpYXQiOjE2NTc2MzI5NzQsImp0aSI6Ijc1ODk3ZGRlLTBkMzItNDYwNy1hMGJiLTgxOGY5M2Y3MmQzNSJ9.GRJ2oLKr6LlQ8AMlTpN8B8Oa8-cEB-eCychmfstsz2s' \
--header 'Content-Type: application/json' \
--data-raw '{  
  "code": "teste1",
  "name": "teste1" , 
}'
```

### Url do swagger

Com o fastapi executando, abra o swager para ver os endpoints

``` bash
http://127.0.0.1:8000/docs#/
```

### Executando os testes

Foram criados apenas alguns testes para demonstrar a
execução dos testes integrados.

``` bash
make integration-tests 
```

### Celery/Flower tasks

Visualizar as tasks do celery

``` bash
http://localhost:5557/tasks
```

Conclusão:
Este projeto foi apenas criado para demonstrar uma pequena ideia de segurança e acesso por token, execução de testes por docker, pipeline
de testes no github , principios solid , mongodb local em docker ou postgresql microserviços.
