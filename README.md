# Nome do Projeto

## Descrição

Este projeto é um _coding_agent_ que empodera a API do Gemini para interagir com o sistema de arquivos. Permite com que o usuário performe diversas operações como listar arquivos e diretórios, ler conteúdo de arquivos, escrever ou sobrescrever arquivos, e executar arquivos com código em Python. O agente usa um prompt sistematizado para guiar o seu comportamento e um conjunto de funções pré-definidas para interagir com os arquivos do sistema. É criado para automatizar tarefas de código e provê um modo conveniente de manusear arquivos de modo programado.

## Funcionalidades

- Lista arquivos do diretório especificado 
- Lê os arquivos do diretório 
- Executa código em Python 
- Escreve ou sobrescreve arquivos 

## Como Usar
1. Faça o clone do repositório:

```bash
git clone git@github.com:luis-octavius/llm-agent.git 
cd llm-agent 
```
> [!warning] Originalmente, o diretório utilizado pelo agente é a pasta `llm-agent/archives`, porém, é possível mudar a variável do diretório no arquivo `config`. Use com cuidado! 

2. Execute:

```bash 
uv run main.py "<seu_prompt_aqui>" --verbose # a flag verbose é opcional e serve para adicionar estatísticas e a resposta do agente
```

## Requisitos
- uv 
- Python
- Chave Gemini API 
 
