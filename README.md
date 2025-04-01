# acervus
Sistema de Publicação Promoção e Compartilhamento de Artigos Científicos


```shell
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

 ```


Criar um config.py com as diretivas de aceso ao banco de dados

```py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_super_secreta')
    
    # Configuração do Banco de Dados
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://usuario:senha@localhost/nome_do_banco')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Credenciais da API do Google
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', 'sua_client_id_aqui')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', 'sua_client_secret_aqui')

```

com o usuário do banco criado e configurado corretamente,

```
flask db init
flask db migrate -m "Criando tabela de Artigos e usuarios"
flask db upgrade

``` 



Após corrigir o __init__.py, execute o Flask corretamente:
```sh
export FLASK_APP=app
flask run
``` 
Ou, se estiver no Windows (PowerShell):

```sh
$env:FLASK_APP="app"
flask run
```

Estrutura do projeto Fase 1



