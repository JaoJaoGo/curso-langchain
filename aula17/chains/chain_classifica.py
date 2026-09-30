from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model_classificador = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

# Criando o classificador da pergunta de entrada do usuário:
class ClassificaEntrada(BaseModel):
    opcao: int = Field(description="Define 1 se a pergunta do usuário solicitar informações ou orientações sobre Dengue ou gráfico da dengue. \
        Define 2 se for saudações ou temas que não são referentes à Dengue. \
        Defina 3 se for uma solicitação de cadastro de ocorrência de Dengue ou se a pessoa está registrando que está com Dengue.")

# Criando o parser estruturado
parser_classifica = PydanticOutputParser(pydantic_object=ClassificaEntrada)

# Criando o ChatPromptTemplate que solicitará ao LLM que ele classifique a entrada do usuário:
sys_prompt_rota = """Você é um especialista em classificação. Você receberá perguntas do usuário e precisará classificá-las da melhor forma entre as \
    opções estabelecidas.
    Também preste atenção ao histórico da conversa quando você for realizar a classificação, pois durante um cadastro de ocorrência pode ser solicitado \
    novas informações do usuário e a classificação pode ser com base no contexto histórico.
    
    \n{format_instructions}\n
    
    Pergunta Usuário: {input}
    
    ## Histórico da Conversa: {history}"""

rota_prompt_template = ChatPromptTemplate([
    ("system", sys_prompt_rota),
], partial_variables={"format_instructions": parser_classifica.get_format_instructions()})

# Criando a chain que vai classificar a entrada do usuário:
chain_de_roteamento = rota_prompt_template | model_classificador | parser_classifica