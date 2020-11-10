# Descrição

Projeto Django para implementação de operações CRUD utilizando PostgreSQL.

# Ambiente de Trabalho

* Sistema Operacional: Windows 10
* IDE: Visual Studio Code
* Database: PostgreSQL
* Bibliotecas: 

# Instalação de Dependências

Para instalar as dependências do projeto é necessário primeiramente instalar o Python. É recomendado fazer o update do pip com o seguinte comando:

  * Linux ou MacOS: pip install -U pip
  * Windows: python -m pip install -U pip
  
Após isso, clonar o projeto no local desejado e executar a seguinte linha de comando na pasta do projeto: pip install -r requirements.txt

# Instalação e configuração do Banco de Dados

Primeiramente, é necessário instalar o PostgreSQL. No wizard de instalação não se esqueça de confirmar a instalação do pgAdmin 4.
Após a instalação, criar um novo Database e alterar as informações de conexão com Databases no arquivo settings.py.
Por fim, para migrar as tabelas criadas basta executar o comando: python manage.py migrate