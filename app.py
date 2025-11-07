import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Importações do SDK Gemini
import google.generativeai as genai

# Não precisamos importar 'types'
# from google.generativeai import types

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)


# --- Função de Geração de Receita (Backend) ---
def gerar_receita(ingredientes_lista):
    """Gera uma receita usando a API Gemini."""
    try:
        # 1. Configurar o cliente com a chave de API
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            # Lança um erro se a chave não for encontrada
            raise ValueError("GEMINI_API_KEY não encontrada. Verifique o arquivo .env.")

        # Configura o SDK
        genai.configure(api_key=api_key)

        client = genai.GenerativeModel('gemini-2.5-flash')

        # 2. Monta o prompt - Otimizado por instrução e para ser mais rápido
        ingredientes_str = ', '.join(ingredientes_lista)
        prompt_usuario = (
            f"Com base nos seguintes ingredientes: {ingredientes_str}, "
            f"sugira **apenas 1 receita** criativa e detalhada, com **máximo de 300 palavras**.\n"
            f"Formato: Liste o NOME, Ingredientes e Passos. Use quebras de linha e marcadores."
        )

        # 3. Chama a API - Sintaxe estável
        response = client.generate_content(
            contents=prompt_usuario
        )

        return response.text

    except ValueError as ve:
        return f"Erro de Configuração: {ve}"
    except Exception as e:
        print(f"Erro ao chamar a API: {e}")
        return f"Erro na API: {e}"


# --- Rotas do Flask ---

@app.route('/')
def index():
    """Renderiza a página HTML principal."""
    return render_template('index.html')


@app.route('/gerar_receita', methods=['POST'])
def api_gerar_receita():
    """Endpoint de API que recebe a requisição AJAX e chama o Gemini."""
    try:
        data = request.json
        ingredientes_raw = data.get('ingredientes', '')

        if not ingredientes_raw:
            return jsonify({"error": "Por favor, forneça os ingredientes."}), 400

        ingredientes_lista = [s.strip() for s in ingredientes_raw.split(',') if s.strip()]

        receita_texto = gerar_receita(ingredientes_lista)

        if "Erro de Configuração" in receita_texto or "Erro na API" in receita_texto:
            return jsonify({"error": receita_texto}), 500

        return jsonify({"receita": receita_texto})

    except Exception as e:
        return jsonify({"error": f"Erro interno do servidor: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)