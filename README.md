# Logophone

Este projeto trata de buscar na web os logos e telefones dos sites acessado
## Começado
Para acessar o sistema serão necessários os seguintes programas:


- [Python 3.8: necessário para a execução do sistema](https://www.python.org/downloads/)
- [Docker: Caso queira rodar apartir de containers](https://www.docker.com/get-started)

## Desenvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do Github em um diretório de sua preferência:
```commandline
cd "diretorio de sua preferencia"
git clone https://github.com/mcribeiro27/Cial-dunbradstreet-test.git
```
## Construção

Para construir o projeto, execute os comandos abaixo dentro da pasta onde baixou o projeto:

Para ambiente Unix
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Para ambiente Windows
```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

O Comando irá instalar todos os módulos necessários para a execução do sistema

## Configuração

Para a execução do projeto basta criar um arquivo ".txt", com as urls que deseja pesquisar e executar:

Para ambiente Unix
```commandline
cat seu_arquivo.txt | python file.py
```
Para ambiente Windows
```commandline
type seu_arquivo.txt | python file.py
```

Caso desejar usar docker basta executar o docfile para criar a imagem:
```commandline
docker build . -t nome-da-imagem
cat seu_arquivo.txt | docker run -i nome-da-imagem
```
## Licença

não se aplica

# Logophone

This project seeks to search the logos and phones of the websites accessed on the web

## Started

To access the system, the following programs will be required: 
- [Python 3.8: necessary for the system to run](https://www.python.org/downloads/)
- [Docker: If you want to run from containers](https://www.docker.com/get-started)

## Development

To start the development, it is necessary to clone the Github project in a directory of your choice:
```commandline
cd "directory of your choice"
git clone https://github.com/mcribeiro27/Cial-dunbradstreet-test.git
```
## Build

To build the project, execute the commands below inside the folder where you downloaded the project:

For Unix environment
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
For Windows environment
```commandline
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```
The Command will install all the modules necessary for the execution of the system

## Configuration

To execute the project, just create a ".txt" file, with the urls you want to search and execute

For Unix environment
```commandline
cat your_file.txt | python file.py
```
For Windows environment
```commandline
type seu_arquivo.txt | python file.py
```
If you want to use docker, just run the docfile to create the image
```commandline
docker build . -t image-name
cat your_file.txt | docker run -i image-name
```
## License

not applicable
