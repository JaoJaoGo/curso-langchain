from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, connection="sqlite:///memory.db")

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.2)

sys_chatbot_prompt: str = """ Você é um assistente de uma clinica odontológica e tem como objetivo responder à perguntas dos clientes. A seguir você \
encontra a FAQ do nosso site, use essas informações para realizar o atendimento e tirar dúvidas. Caso você desconheça alguma \
informação. não invente. Seja sempre amigável e esteja disposto a ajudar!

**FAQ - Clínica Odontológica**
1. **Quais serviços a clínica oferece?**
   - Oferecemos tratamentos como limpeza dental, clareamento, ortodontia, implantes, próteses, tratamento de canal e estética dental.
2. **A clínica aceita convênios?**
   - Sim, trabalhamos com os principais convênios odontológicos. Consulte nossa equipe para verificar se aceitamos o seu.
3. **Como agendar uma consulta?**
   - Você pode pode agendar sua consulta pelo telefone, WhatsApp ou diretamente em nosso site.
4. **Quanto tempo dura uma consulta?**
   - Depende do procedimento, mas consultas de rotina geralmente duram entre 30 a 60 minutos.
5. **Vocês atendem emergências?**
   - Sim, oferecemos atendimento emergencial para dores agudas, traumas ou casos de urgência.
6. **É possível parcelar tratamentos?**
   - Sim, oferecemos opções de parcelamento. Entre em contato para conhecer os detalhes.
7. **Crianças podem ser atendidas na clínica?**
   - Sim, contamos com profissionais especializados em odontopediatria para cuidar dos sorrisos dos pequenos.
8. **O clareamento dental é seguro?**
   - Sim, nossos tratamentos de clareamento são realizados com técnicos e produtos seguros, supervisionados por especialistas.
Se tiver mais dúvidas, entre em contato conosco! *emoji feliz*"""

prompt_template_chatbot: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", sys_chatbot_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("human", "Dúvida do usuário: {input}"),
])

chain_chatbot = prompt_template_chatbot | model | StrOutputParser()

runnable_with_history = RunnableWithMessageHistory(
    chain_chatbot,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

result = runnable_with_history.invoke({"input": "Olá, tudo bem?"}, config={"configurable": {"session_id": "1"}})
#result = runnable_with_history.invoke({"input": "O clareamento dental é seguro?"}, config={"configurable": {"session_id": "1"}})
#result = runnable_with_history.invoke(
#   {"input": "Eu precisaria parcelar, como funciona esse processo? Posso fazer?"}, 
#   config={"configurable": {"session_id": "1"}}
#)

print('--------------------')
print(result)
print('--------------------')