from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

### Exemplo 01:
# Parte 01: Criando ChatPromptTemplate
print('------ Exemplo Chain 1 ------')

prompt_template = ChatPromptTemplate([
    ("user", "Escreva um poema em {lingua} sobre o tema: {assunto}")
])

# Parte 02: Criando a chain
chain1 = prompt_template | model

# Parte 03: Invoke da chain passando as variáveis.
resposta = chain1.invoke({
    "lingua": "pt-br",
    "assunto": "frutas"
})

print(resposta.content)
print("-----------------------------")

### Exemplo 02:
# Parte 01: Criando ChatPromptTemplate já com mensagem do sistema:
print("\n------ Exemplo Chain 2 ------")

mensagens = [
    ("system", "Você é um poeta brasileiro famoso e escreve poemas de no máximo {n_versos} versos."),
    ("user", "Escreva para mim um poema sobre {assunto}")
]

prompt_template_2 = ChatPromptTemplate(mensagens)

# Parte 02: Criando a chain
chain2 = prompt_template_2 | model

# Parte 03: Invoke da chain passando as variáveis.
resposta2 = chain2.invoke({
    "n_versos": "10",
    "assunto": "navios"
})

print(resposta2.content)
print("-----------------------------")