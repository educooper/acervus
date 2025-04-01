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
export FLASK_APP=acervus
export FLASK_ENV=development
flask run
``` 
Ou, se estiver no Windows (PowerShell):

```sh
$env:FLASK_APP="acervus"
$env:FLASK_ENV="development"
flask run
```

Estrutura do projeto Fase 1

meu_projeto/
│
├── acervus/
│   ├── models.py
│   ├── views.py
│   ├── controllers.py
│   ├── templates/
│   │   ├── index.html
│
├── run.py
└── config.py





Fase 2

/flask_articles
│── /acervus
│   ├── /static        # Arquivos CSS, JS e imagens
│   ├── /templates     # HTML templates para o frontend
│   ├── /models        # Modelos do banco de dados
│   ├── /routes        # Rotas da aplicação
│   ├── /forms         # Formulários Flask-WTF
│   ├── /services      # Lógica de negócios e utilitários
│   ├── __init__.py    # Inicialização da aplicação
│── /migrations        # Controle de versões do banco (Flask-Migrate)
│── config.py          # Configuração do Flask
│── run.py             # Arquivo principal para rodar a aplicação
│── requirements.txt   # Dependências do projeto
│── .env               # Variáveis de ambiente




Fase A

meu_projeto/
├── acervus.py          # Arquivo principal do Flask
├── models.py       # Definição dos modelos do banco de dados (SQLAlchemy)
├── routes.py       # Definição das rotas da aplicação
├── auth.py         # Lógica de autenticação (Google Auth 2.0)
├── templates/      # Templates HTML
│   ├── index.html
│   ├── login.html
│   └── profile.html
├── static/         # Arquivos estáticos (CSS, JS, imagens)
├── requirements.txt # Dependências do projeto
└── config.py       # Configurações da aplicação (chaves de API, etc.)



Conceito do banco de dados


