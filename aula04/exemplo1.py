from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.1)

# O ChatModel é um componente LangChain então ele possui o protocolo invoke()

resposta = model.invoke("Olá, como você está e o que você é capaz de fazer?")

print("------- RESPOSTA AIMessage -------")
print(resposta)
print("----------------------------------")

print("\n------- RESPOSTA Somente Texto -------")
print(resposta.content)
print("--------------------------------------")