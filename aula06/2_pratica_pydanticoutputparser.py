from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

# Definindo a minha estrutura de saída usando Pydantic
class Rota(BaseModel):
    escolha: int = Field(description="Rota escolhida")
    pensamento: str = Field(description="Campo para o pensamento que levou a decisão da rota escolhida")

# Criando o analisador de saída
parser = PydanticOutputParser(pydantic_object=Rota)

prompt_template = ChatPromptTemplate([
    ("system", "Se a pergunta do usuário for relacionado ao setor financeiro, a escolha deve ser 1, caso contrário pode ser qualquer outro número diferente de 1. \
                \n{format_instructions}\n Pergunta Usuário: {pergunta_user}")
], partial_variables={"format_instructions": parser.get_format_instructions()})

chain = prompt_template | model | parser

output = chain.invoke({"pergunta_user": "Me diga quanto está o dollar."})

print("--" * 50)
print("Tipo de saída:")
print(type(output))
print("--" * 50)
print("Saída estruturada:")
print(output)
print("--" * 50)
print("Consigo acessar cada parametro da minha classe pydantic, veja:")
print(f"Valor do parametro 'escolha': {output.escolha}")
print(f"Valor do parametro 'pensamento': {output.pensamento}")
print("--" * 50)