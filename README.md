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

### 1. Clonar o Repositório

Abra seu terminal (Git Bash) e clone o projeto:

```bash
git clone [https://github.com/Brenno0707/cozinheiro-inteligente-web.git](https://github.com/Brenno0707/cozinheiro-inteligente-web.git)
cd cozinheiro-inteligente-web


2. Configurar o Ambiente Virtual
É uma boa prática isolar as dependências do projeto:

Bash

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
# Se estiver usando o Git Bash ou PowerShell, o comando pode variar.
# Geralmente:
.\venv\Scripts\activate

3. Instalar Dependências
Instale todas as bibliotecas necessárias listadas no requirements.txt:

Bash

pip install -r requirements.txt
4. Configurar a Chave de API
Crie um arquivo chamado .env na raiz da pasta do projeto e adicione sua chave de API nele.

Conteúdo do .env:

GEMINI_API_KEY="SUA_CHAVE_AQUI_GEMINI_API"
5. Rodar a Aplicação
Inicie o servidor Flask:

Bash

python app.py


📝 Licença
Este projeto está sob a licença MIT.


### 🏁 Próximos Passos Finais:

1.  Crie o arquivo **`README.md`** na pasta do projeto e cole o conteúdo acima.
2.  **Adicione e Envie o `README.md`** ao GitHub:
    ```bash
    git add README.md
    git commit -m "Adiciona README.md detalhado"
    git push origin master
    ```

Sua página do GitHub ficará agora com uma descrição completa do seu projeto!
