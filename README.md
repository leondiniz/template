
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

### Executando os fastapi

sem docker(apontar o database no .env)

``` bash
make run 
```

ou

com docker

``` bash
make run_docker_app 
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
