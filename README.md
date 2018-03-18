# Flask-CRUD

Projeto Web Python 2.7 com a microframework Flask e Flask-SQLAlchemy. A aplicação consiste em um painel de administrador (sem autenticação) para gerenciar veículos de uma base de dados. O projeto faz uso de modularização (Blueprints) e aplica padrões como Application Factory, tornando viável a escalabilidade da aplicação. O projeto também utiliza, a framework Flask-WTForms, que possibilita a validação dos forms dentro do front-end da aplicação.

## Configuração
### Máquina Virtual
É recomendável utilizar uma máquina virtual python para executar o projeto. Entretanto, caso desejável executar o projeto o interpretador previamente instalado, pule para o próximo tópico. 

Para criar a máquina virtual, basta executar o seguintes comando:
```bash
virtualenv venv
```
É possível que você tenha que instalar a virtualenv na sua máquina.
Em seguida, ative a máquina virtual executando o seguinte comando:

Linux:
```bash
. venv/bin/activate
```
Windows:
```bash
\venv\Scripts\activate
```
### Instalando as Dependências
Com a máquina ativada, é necesário instalar as dependências do projeto com o client PIP. Portanto, execute o seguinte comando:
```bash
pip install -r requirements.txt
```

## Inicializando a Aplicação
Deve ser criado a base de dados SQLite3 executando o seguinte comando:
```bash
python run.py --init-db
```
Em seguida, inicialize a aplicação:
```bash
python run.py
```

Pronto, para acessar aplicação, basta acessar a URL [localhost:5000](http://127.0.0.1:5000): 
