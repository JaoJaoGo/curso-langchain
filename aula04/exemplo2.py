from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.1)

## Criando a conversa. Lembrando que os ChatModels recebem como entrada uma lista de mensagens. Assim o LangChain automaticamente converte isso na
## estrutura que o modelo LLM precisa receber para responder.

# Forma 1 de escrever:
mensagens = [
    SystemMessage(content="Você é um especialista em astrofísica."),
    HumanMessage(content="Qual a distância do Sol até a Terra?"),
    AIMessage(content="O Sol está a 49.600.000 km de distância da Terra."),
    HumanMessage(content="E a distância da Terra até Marte?"),
]

# Forma 2 de escrever:
# mensagens = [
#   ("system", "Você é um especialista em astrofísica."),
#   ("user", "Qual a distância do Sol até a Terra?"),
#   ("assistant", "O Sol está a 49.600.000 km de distância da Terra."),
#   ("user", "E a distância da Terra até Marte?"),
# ]

# Como a entrada do usuário é a ultima mensagem da lista, você pode dá invoke usando a lista de pensamentos contendo o histórico de conversação.
resposta = model.invoke(mensagens)

print("------- RESPOSTA AIMessage -------")
print(resposta)
print("----------------------------------")

print("\n------- RESPOSTA Somente Texto -------")
print(resposta.content)
print("--------------------------------------")