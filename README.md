# Logofone

Este projeto trata de buscar na web os logos e telefones dos sites acessado
## Começado
Para acessar o sistema serão necessários os seguintes programas:

- [Python 3.8: necessário para a execução do sistema](https://www.python.org/downloads/)
- [Docker: Caso queira rodar apartir de containers](https://www.docker.com/get-started)

## Desenvolvimento

Para iniciar o desenvolvimento, é necessário clonar o projeto do Gitlab em um diretório de sua preferência:
```buildoutcfg
cd "diretorio de sua preferencia"
git clone https://gitlab.com/mcribeiro27/cial-dunbradstreet-test.git
```
## Construção

Para construir o projeto, execute os comandos abaixo dentro da pasta onde baixou o projeto:

Para ambiente Unix
```python
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Para ambiente Windows
```python
pip install virtualenv
virtualenv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

O Comando irá instalar todos os módulos necessários para a execução do sistema

## Configuração

Para a execução do projeto basta criar um arquivo ".txt", com as urls que deseja pesquisar e executar:
```commandline
cat seu_arquivo.txt | python file.py
```
Caso desejar usar docker basta executar o docfile para criar a imagem:
```commandline
docker build . -t nome-da-imagem
cat seu_arquivo.txt | docker run -i nome-da-imagem
```
## Licença

não se aplica
