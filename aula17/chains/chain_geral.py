from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model_fora_do_tema = ChatGroq(model="openai/gpt-oss-120b", temperature=0.2)

sys_prompt_fora_do_tema = """Você é um assistente de saúde se o usuário fez uma saudação, responda de forma amigável e sugira o que você pode fazer como \
    por exemplo responder sobre dúvidas a respeito da Dengue, dar orientações sobre as causas, tratamento e sintomas da Dengue ou registrar uma ocorrência \
    de Dengue. Se usuário fez uma pergunta não pertinente ao tema, informe que você não é capaz de responder sobre estes assuntos e que o seu papel é tirar \
    dúvidas sobre saúde."""

fora_do_tema_prompt_template = ChatPromptTemplate([
    ("system", sys_prompt_fora_do_tema),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Dúvida do usuário: {pergunta_usuario}"),
])

chain_temas_nao_relacionados = fora_do_tema_prompt_template | model_fora_do_tema | StrOutputParser()