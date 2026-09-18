from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

async def conversa_com_modelo():
    model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.1)

    conversa = [SystemMessage(content="Você é um assistente útil que responde ao usuário com detalhes e exemplos.")]

    while True:
        entrada: str = input("\nEntrada Usuário (digite 'q' para parar.): ")
        if entrada.lower() == 'q':
            break
        
        conversa.append(HumanMessage(content=entrada))

        all_chunks = []
        async for chunk in model.astream(conversa):
            all_chunks.append(chunk.content)
            print(chunk.content, end="", flush=True)
        
        conversa.append(AIMessage(content="".join(all_chunks)))

    print("\n------- Histórico Completo -------")
    print(conversa)
    print("----------------------------------")

import asyncio

asyncio.run(conversa_com_modelo())