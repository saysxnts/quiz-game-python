# Jogo de Quiz em Python a Partir de um Arquivo

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)

## 📖 Sobre o Projeto

Este é um jogo de quiz interativo de linha de comando desenvolvido em Python. A principal característica do projeto é que todas as perguntas, opções e respostas corretas são carregadas dinamicamente de um arquivo `perguntas.json` externo. Isso torna o quiz facilmente expansível: para adicionar mais perguntas, basta editar o arquivo JSON, sem necessidade de alterar o código Python.

O projeto foi criado para praticar habilidades intermediárias de Python, incluindo manipulação de arquivos, parsing de JSON e o uso de estruturas de dados como listas e dicionários para gerenciar o estado do jogo.

---

## ✨ Funcionalidades

- **Quiz Dinâmico:** Carrega as perguntas de um arquivo JSON, permitindo fácil customização e expansão.
- **Perguntas Aleatórias:** A ordem das perguntas é embaralhada a cada nova partida, garantindo uma experiência diferente a cada vez.
- **Interação com Usuário:** Apresenta perguntas de múltipla escolha e valida a entrada do usuário.
- **Cálculo de Pontuação:** Mantém o controle das respostas corretas e exibe uma pontuação final detalhada, incluindo o percentual de acertos.
- **Feedback Imediato:** Informa ao usuário se a resposta está correta ou errada após cada pergunta.

---

## 🛠️ Tecnologias e Conceitos Praticados

- **Python 3**
- **Manipulação de Arquivos:** Leitura de arquivos de texto com `with open()`.
- **Parsing de JSON:** Uso do módulo `json` da biblioteca padrão para converter dados JSON em estruturas de dados Python.
- **Estruturas de Dados:** Manipulação de listas e dicionários para armazenar e acessar os dados do quiz.
- **Módulos da Biblioteca Padrão:** Uso do módulo `random` para embaralhar as perguntas.
- **Tratamento de Erros:** Bloco `try...except` para lidar com possíveis erros, como a não localização do arquivo de perguntas.
- **Lógica de Controle:** Laços de repetição (`for`, `while`) e condicionais (`if/else`) para controlar o fluxo do jogo.

---

## 🚀 Como Rodar o Jogo

### **Pré-requisitos**

- É necessário ter o **Python 3** instalado.

### **Execução**

1.  **Clone o repositório** ou baixe os arquivos do projeto.
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```

2.  **Navegue até a pasta do projeto**:
    ```bash
    cd quiz_python
    ```
    *Certifique-se de que os arquivos `quiz.py` e `perguntas.json` estão na mesma pasta.*

3.  **Execute o script Python**:
    ```bash
    python quiz.py
    ```
4.  O jogo começará no seu terminal. Divirta-se!

---

## 📝 Como Adicionar Novas Perguntas

Para adicionar, remover ou modificar perguntas, basta editar o arquivo `perguntas.json`. Siga o formato abaixo para cada nova pergunta que desejar adicionar à lista:

```json
{
    "pergunta": "Sua nova pergunta aqui.",
    "opcoes": [
        "A) Primeira opção",
        "B) Segunda opção",
        "C) Terceira opção",
        "D) Quarta opção"
    ],
    "resposta_correta": "A) Primeira opção"
}
```
*Lembre-se de colocar uma vírgula entre os objetos de pergunta, exceto após o último.*

---

## ✒️ Autor

**Guilherme**
