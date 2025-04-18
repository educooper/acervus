# acervus
Sistema de Publicação Promoção e Compartilhamento de Artigos Científicos

Além da interface web tradicional, o sistema fornece uma API RESTful para permitir integração com aplicativos móveis, automações de submissão, e futuras plataformas de indexação científica. A API implementa autenticação segura via JWT e permite operações completas de cadastro, edição e consulta de artigos.



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

Estrutura do projeto Fase 2


```
GET     /api/articles               # Lista artigos
POST    /api/articles               # Cadastra novo artigo
GET     /api/articles/<id>          # Detalhes de um artigo
PUT     /api/articles/<id>          # Atualiza um artigo
DELETE  /api/articles/<id>          # Remove um artigo

GET     /api/articles/search?q=...  # Busca avançada por termo, tag, autor

POST    /api/login                  # Autentica e retorna JWT
GET     /api/user/articles          # Lista artigos submetidos pelo usuário logado
```



