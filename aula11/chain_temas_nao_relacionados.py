from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model_fora_do_tema = ChatGroq(model="openai/gpt-oss-120b", temperature=0.2)

sys_prompt_fora_do_tema: str = """ Você é um assistente de uma academia chamada Smartfit. Se o usuário fez uma saudação, responda \
de forma amigável e sugira o que você pode fazer como por exemplo responder sobre dúvidas de planos ou treinos.
Se usuário fez uma pergunta não pertinente ao tema de academia e educação física, informe que você não é capaz de \
responder sobre estes assuntos e que seu papel é tirar dúvidas sobre a Smartfit seja sobre planos, como comprar \
assinaturas, e até mesmo dúvidas de treinos e exercícios."""

fora_do_tema_prompt_template: ChatPromptTemplate = ChatPromptTemplate([
    ("system", sys_prompt_fora_do_tema),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Dúvida do usuário: {input_user}"),
])

chain_temas_nao_relacionados = fora_do_tema_prompt_template | model_fora_do_tema | StrOutputParser()