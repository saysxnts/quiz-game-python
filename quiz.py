# quiz.py

import json
import random

def carregar_perguntas(arquivo_json):
    """Carrega as perguntas de um arquivo JSON e as retorna."""
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            perguntas = json.load(f)
        return perguntas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{arquivo_json}' não é um JSON válido.")
        return None

def iniciar_quiz():
    """Função principal que executa a lógica do quiz."""
    perguntas = carregar_perguntas('perguntas.json')

    # Se houve um erro ao carregar as perguntas, o programa para.
    if not perguntas:
        return

    # Embaralha a ordem das perguntas para que cada jogo seja diferente
    random.shuffle(perguntas)

    pontuacao = 0
    total_de_perguntas = len(perguntas)

    print("--- Bem-vindo ao Quiz de Conhecimentos Gerais! ---")
    print(f"Responda a {total_de_perguntas} perguntas e teste seus conhecimentos.\n")

    # Itera sobre cada pergunta na lista
    for i, p in enumerate(perguntas, 1):
        print(f"Pergunta {i}: {p['pergunta']}")

        # Itera sobre as opções da pergunta atual
        for opcao in p['opcoes']:
            print(opcao)

        # Pede a resposta do usuário e valida a entrada
        resposta_usuario = ""
        opcoes_validas = ['A', 'B', 'C', 'D']
        while resposta_usuario not in opcoes_validas:
            resposta_usuario = input("Sua resposta (A, B, C ou D): ").upper()

        # Converte a letra da resposta para o texto completo da opção
        # Ex: 'C' -> 'C) Brasília'
        indice_resposta = opcoes_validas.index(resposta_usuario)
        texto_resposta_usuario = p['opcoes'][indice_resposta]

        # Verifica se a resposta está correta
        if texto_resposta_usuario == p['resposta_correta']:
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"Resposta errada! A resposta correta era: {p['resposta_correta']}\n")

    # Exibe o resultado final
    print("--- Fim do Quiz! ---")
    print(f"Sua pontuação final foi: {pontuacao} de {total_de_perguntas} perguntas.")
    percentual = (pontuacao / total_de_perguntas) * 100
    print(f"Você acertou {percentual:.2f}% das perguntas.")

# Garante que a função iniciar_quiz() seja chamada apenas quando o script é executado diretamente
if __name__ == "__main__":
    iniciar_quiz()