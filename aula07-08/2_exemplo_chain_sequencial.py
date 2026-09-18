from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.5)

# Criamos a função personalizada para tratar a saída textual do LLM
def separador_de_tweet(entrada: str) -> list:
    """
    Função que recebe uma string e retorna uma lista com os elementos separados por quebras de linha.

    Args:
        entrada (str): A string de entrada, onde os valores estão separados por quebras de linha.

    Returns:
        list: Uma lista contendo cada elemento da string como um item separado.
    """
    # Divida a string em uma lista utilizando o caractere de quebra de linha '\n'
    elementos = entrada.split('\n')

    # Remove espaços extras e ignora linhas vazias
    elementos_limpos = [elemento.strip() for elemento in elementos if elemento.strip()]

    return elementos_limpos

def relatorio_de_analise_de_caracteres(entrada: list) -> dict:
    """
    Função que gera um relatório com os tweets e a contagem de caracteres de cada tweet.

    Args:
        entrada (list): Lista de strings representando os tweets.

    Returns:
        dict: Um dicionário com duas chaves:
            - 'tweets': contendo a lista original.
            - 'num_caract': contendo uma lista com o número de caracteres de cada tweet.
    """
    # Gera a contagem de caracteres para cada item na lista
    contagem_caracteres = [len(tweet) for tweet in entrada]

    # Monta o dicionário de saída
    relatorio = {
        "tweets": entrada,
        "num_caract": contagem_caracteres
    }

    return relatorio

prompt_sistema = """Você é um assistente especialista em criar conteúdo para o twitter e tem como objetivo criar os melhores tweets virais sobre o tema que o \
usuário te passar. Seja criativo e atenda ao padrão de 280 caracteres do twitter.
Orientação:
- Crie apenas o número de tweets informado.
- Separe cada um deles por uma quebra de linha.
"""

prompt_template = ChatPromptTemplate([
    ("system", prompt_sistema),
    ("user", "Crie um total de {numero_de_publicacoes} tweets sobre o tema {input_tema}."),
])

chain = prompt_template | model | StrOutputParser() | RunnableLambda(separador_de_tweet) | RunnableLambda(relatorio_de_analise_de_caracteres)

result = chain.invoke({"numero_de_publicacoes": 3, "input_tema": "tecnologia"})

# Imprimindo o nosso dicionário de relatório:
print(result)
print('--' * 50)

# Imprimindo a saida de forma mais estruturada:
for i, (tweet, num_caract) in enumerate(zip(result["tweets"], result["num_caract"]), start=1):
    print(f"Tweet {i}: {tweet}")
    print(f"Total de caracteres: {num_caract}")

    if num_caract <= 280:
        print("Validação: OK")
    else:
        print("Validação: Tweet supera o limite de 280 caracteres")
    print('--' * 50)
