from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model_classificador = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

class ClassificaEntrada(BaseModel):
    opcao: int = Field(description="Defina 1 se a pergunta do usuário for referente à dúvidas gerais de um FAQ. \
    Defina 2 se for uma solicitação de ajuda para montar um treino ou pergunta específica sobre um exercício ou treino. \
    Defina 3 se for saudações ou temas que não são referentes à dúvidas sobre academia.")

parser_classifica: PydanticOutputParser = PydanticOutputParser(pydantic_object=ClassificaEntrada)

sys_prompt_rota: str = """Você é um especialista em classificação. Você receberá perguntas do usuário e precisará classificar, \
de forma booleana, se o usuário está perguntando sobre dúvidas gerais sobre a academia e planos ou se ele precisa \
de ajuda com um treino ou exercício.
\n{format_instructions}\n
Pergunta Usuário: {input}
"""

rota_prompt_template: ChatPromptTemplate = ChatPromptTemplate([
    ("system", sys_prompt_rota),
], partial_variables={"format_instructions": parser_classifica.get_format_instructions()})

chain_de_roteamento = rota_prompt_template | model_classificador | parser_classifica