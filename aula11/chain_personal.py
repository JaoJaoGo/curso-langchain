from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model_personal = ChatGroq(model="openai/gpt-oss-120b", temperature=0.2)

sys_prompt_personal: str = """Você é um personal trainer renomado e entende de todos os tipos de treinos para todos os tipos de \
físicos. Você precisa responder às dúvidas do usuário sobre exercícios ou treinos. Seja amigável e detalhista. Apoie sempre \
seu aluno.
"""

personal_prompt_template: ChatPromptTemplate = ChatPromptTemplate([
    ("system", sys_prompt_personal),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Dúvida do usuário: {input_user}"),
])

chain_personal = personal_prompt_template | model_personal | StrOutputParser()