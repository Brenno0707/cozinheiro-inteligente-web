# 🍳 Cozinheiro Inteligente (Gemini AI)

Aplicação web interativa desenvolvida em Python (Flask) que utiliza o poder da API Google Gemini para gerar receitas criativas baseadas nos ingredientes que o usuário possui em casa.

O projeto demonstra uma arquitetura completa de backend (Flask) e frontend moderno (Tailwind CSS com JavaScript interativo).

## ✨ Funcionalidades

* **Geração de Receitas por Ingrediente:** O usuário insere uma lista de ingredientes e o Gemini (Modelo `gemini-2.5-flash`) sugere uma receita completa.
* **Otimização de Prompt:** O backend utiliza técnicas de engenharia de prompt para garantir que o Gemini retorne apenas **uma receita**, de forma concisa e estruturada.
* **Interface Interativa:** Uso de JavaScript para gerenciar requisições assíncronas (AJAX) e exibir o resultado da IA com um **efeito de digitação** (typing effect) e animações visuais (Tailwind CSS).
* **Segurança:** Utilização do arquivo `.env` para gerenciar a chave de API de forma segura.

## 💻 Tecnologias Utilizadas

| Componente | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Backend** | Python 3.x, Flask | Servidor web, rotas de API e lógica de negócio. |
| **Inteligência Artificial** | Google GenAI SDK (`gemini-2.5-flash`) | Geração do conteúdo da receita. |
| **Frontend** | HTML5, Tailwind CSS | Estrutura e estilização moderna e responsiva. |
| **Interatividade** | JavaScript | Manipulação do DOM, efeitos de carregamento e efeito de digitação. |

## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e rodar a aplicação localmente.

### Pré-requisitos

* Python 3.x instalado.
* Uma Chave de API do Gemini, que pode ser obtida no [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).

🚀 Como Rodar o Projeto

1. Clonar o Repositório

Abra seu terminal (Recomendado: Git Bash ou terminal do PyCharm) e clone o projeto:

git clone [https://github.com/Brenno0707/cozinheiro-inteligente-web.git](https://github.com/Brenno0707/cozinheiro-inteligente-web.git)
cd cozinheiro-inteligente-web


2. Configurar o Ambiente Virtual

É crucial isolar as dependências do projeto para evitar conflitos:

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Comando para Windows)
.\venv\Scripts\activate


3. Instalar Dependências

Instale todas as bibliotecas necessárias, incluindo a biblioteca google-genai (que substitui o SDK antigo):

pip install -r requirements.txt


4. Configurar a Chave de API

Crie um arquivo chamado .env (sem extensão!) na raiz da pasta do projeto e adicione sua chave de API nele.

Conteúdo do .env:

GEMINI_API_KEY="SUA_CHAVE_AQUI_GEMINI_API"


⚠️ Atenção: Problema de Sintaxe (Muito Importante)

As instruções originais do projeto usam uma sintaxe antiga da biblioteca do Gemini. Você deve substituir o código do arquivo app.py pela versão corrigida.

Altere a função gerar_receita em app.py para usar a sintaxe compatível com o SDK atual:

# Versão COMPATÍVEL com a sua instalação:
# Substitua o código da função 'gerar_receita' pela sintaxe abaixo:

# ----------------------------------------------------
# from google.generativeai import GenerativeModel, Client (se importado acima)
def gerar_receita(ingredientes_lista):
    # ... código de verificação de chave ...
    client = genai.Client() 
    MODEL_NAME = 'gemini-2.5-flash' 
    
    # Sintaxe estável (resolve AttributeErrors)
    model = client.get_model(MODEL_NAME) # OU use 'model = client.models[MODEL_NAME]' se preferir

    # ... restante do código para montar o prompt ...
    
    response = model.generate_content(
        contents=prompt_usuario
    )
    # ... restante do código ...


5. Rodar a Aplicação

Após corrigir o app.py, inicie o servidor Flask:

python app.py


Acesse o navegador na URL indicada pelo terminal (http://127.0.0.1:5000/).

📝 Licença

Este projeto está sob a licença MIT.
