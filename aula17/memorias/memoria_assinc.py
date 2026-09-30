from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.messages import trim_messages
from sqlalchemy.ext.asyncio import create_async_engine

## Criando o gestor de memória (histórico): Função para retornar o histórico de mensagens com base no `session_id`

# criando uma engine (conexão) assincrona com o banco de dados.
async_engine = create_async_engine("sqlite+aiosqlite:///memorychatbot.db")

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, connection=async_engine)

# Criando a função que corta o histórico e captura as 10 últimas mensagens trocadas na conversa:
trimmer = trim_messages(strategy='last', max_tokens=10, token_counter=len)