# 🍳 Cozinheiro Inteligente (Gemini AI)

Aplicação web interativa desenvolvida em Python (Flask) que utiliza o poder da API Google Gemini para gerar receitas criativas baseadas nos ingredientes que o usuário possui em casa.

O projeto demonstra uma arquitetura completa de backend (Flask) e frontend moderno (Tailwind CSS com JavaScript interativo).

---

### ✨ Funcionalidades

* **Geração de Receitas por Ingrediente:** O usuário insere uma lista de ingredientes e o Gemini (Modelo **gemini-2.5-flash**) sugere uma receita completa.
* **Otimização de Prompt:** O backend utiliza técnicas de engenharia de prompt para garantir que o Gemini retorne apenas uma receita, de forma concisa e estruturada.
* **Interface Interativa:** Uso de JavaScript para gerenciar requisições assíncronas (AJAX) e exibir o resultado da IA com um efeito de digitação (typing effect) e animações visuais (Tailwind CSS).
* **Segurança:** Utilização do arquivo **.env** para gerenciar a chave de API de forma segura.

### 💻 Tecnologias Utilizadas (Reorganizadas para Máxima Compatibilidade)

#### Backend
* **Python 3.x, Flask:** Servidor web, rotas de API e lógica de negócio.
* **Google GenAI SDK (gemini-2.5-flash):** Geração do conteúdo da receita.

#### Frontend
* **HTML5, Tailwind, CSS:** Estrutura e estilização moderna e responsiva.
* **JavaScript:** Manipulação do DOM e interatividade.

---

### 🚀 Instalação e Execução

Siga os passos abaixo para configurar e rodar a aplicação localmente.

#### Pré-requisitos
* **Python 3.x** instalado.
* Uma **Chave de API do Gemini**, obtida no [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).

#### 1. Clonar o Repositório

```bash
git clone [https://github.com/Brenno0707/cozinheiro-inteligente-web.git](https://github.com/Brenno0707/cozinheiro-inteligente-web.git)
cd cozinheiro-inteligente-web
2. Configurar o Ambiente Virtual
Bash

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Comando para Windows)
.\venv\Scripts\activate
3. Instalar Dependências
Bash

pip install -r requirements.txt
4. Configurar a Chave de API
Crie um arquivo chamado .env (sem extensão!) na raiz da pasta do projeto e adicione sua chave de API nele.

Conteúdo do .env:

GEMINI_API_KEY="SUA_CHAVE_AQUI_GEMINI_API"
5. Corrigir o app.py (Crucial)
ATENÇÃO: O código original do app.py é obsoleto e causará erros de sintaxe. Você deve substituir o conteúdo do app.py pela versão mais recente e corrigida para garantir que a aplicação funcione corretamente.

6. Rodar a Aplicação
Inicie o servidor Flask:

Bash

python app.py
Acesse o navegador na URL indicada pelo terminal (http://127.0.0.1:5000/).

📝 Licença

Este projeto está sob a licença MIT.
