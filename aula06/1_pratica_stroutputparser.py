# documentação: https://python.langchain.com/docs/concepts/output_parsers/

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt_template = ChatPromptTemplate([("user", "Escreva um poema em {lingua} sobre o tema: {assunto}")])

chain1 = prompt_template | model

resposta1 = chain1.invoke({"lingua": "pt-br", "assunto": "frutas"})

print(type(resposta1))
print("--" * 50)
print(resposta1)
print("--" * 50)

# Prática 01 - StrOutputParser

# E se eu quisesse pegar a saída anterior e obtê-la sem precisar acessar content? Simples, usamos StrOutputParser para capturar
# a saída do LLM no formato puro de string.

from langchain_core.output_parsers import StrOutputParser

analisador_saida = StrOutputParser()

chain1_com_outputparser = prompt_template | model | analisador_saida

resposta2 = chain1_com_outputparser.invoke({"lingua": "pt-br", "assunto": "frutas"})

print(type(resposta2))
print("--" * 50)
print(resposta2)
print("--" * 50)