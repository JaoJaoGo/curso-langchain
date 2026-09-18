from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.5)

prompt_sistema = """Você é um assistente especialista em criar conteúdo para o twitter e tem como objetivo criar os melhores tweets virais sobre o tema que o usuário passar. \
    Seja criativo e atenda ao padrão de 280 caracteres do twitter.
"""

prompt_template = ChatPromptTemplate([
    ("system", prompt_sistema),
    ("user", "Crie um total de {numero_de_publicacoes} tweets sobre o tema {input_tema}."),
])

# Crie a cadeia combinada usando LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()

result = chain.invoke({
    "numero_de_publicacoes": 3,
    "input_tema": "tecnologia"
})

print(result)