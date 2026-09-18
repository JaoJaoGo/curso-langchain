from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Carregando as variáveis de ambiente
load_dotenv()

# Chama a API do modelo do Groq
llm = ChatGroq(model="openai/gpt-oss-120b")

# Executa a chamada do modelo
result = llm.invoke("Este é um teste. Se você recebeu a requisição responda 'Teste OK'.")
print(result.content)