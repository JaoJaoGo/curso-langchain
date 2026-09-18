## Documentação
# https://python.langchain.com/docs/how_to/#prompt-templates

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# ========== EXEMPLO 01 ==========

print("======= Exemplo 01 =======")

prompt_template = PromptTemplate.from_template("Gere para mim um poema sobre: {assunto}. Escreva em {língua}")
retorno = prompt_template.invoke({"assunto": "navegação", "língua": "pt-br"})
print(retorno)

print("==========================")

# ========== EXEMPLO 02 ==========

print("\n======= Exemplo 02 =======")

prompt_template_2 = ChatPromptTemplate(["Gere para mim um poema sobre: {assunto}. Escreva em {língua}"])
retorno_2 = prompt_template_2.invoke({"assunto": "navegação", "língua": "pt-br"})
print(retorno_2)

print("\n===== Alternativa 01 =====")

prompt_template_2_1 = ChatPromptTemplate([
    HumanMessagePromptTemplate.from_template("Gere para mim um poema sobre: {assunto}. Escreva em {língua}")
])
retorno_2_1 = prompt_template_2_1.invoke({"assunto": "navegação", "língua": "pt-br"})
print(retorno_2_1)

print("\n===== Alternativa 02 =====")

prompt_template_2_2 = ChatPromptTemplate([
    ("user", "Gere para mim um poema sobre: {assunto}. Escreva em {língua}")
])
retorno_2_2 = prompt_template_2_2.invoke({"assunto": "navegação", "língua": "pt-br"})
print(retorno_2_2)

print("=============================")

# ========== EXEMPLO 03 ==========

print("\n======= Exemplo 03 =======")

prompt_template_3 = ChatPromptTemplate([
    ("system", "Você é um assistente de IA com habilidade de escritor de poesias."),
    ("user", "Gere para mim um poema sobre: {assunto}. Escreva em {língua}")
])
retorno_3 = prompt_template_3.invoke({"assunto": "navegação", "língua": "pt-br"})
print(retorno_3)

print("\n===== Alternativa 01 =====")

prompt_template_3_1 = ChatPromptTemplate([
    ("system", "Você é um assistente de IA com habilidade de escritor de poesias."),
    MessagesPlaceholder("msgs_user")
])
retorno_3_1 = prompt_template_3_1.invoke({"msgs_user": [HumanMessage(content="Gere para mim um poema sobre: navegação. Escreva em pt-br")]})
print(retorno_3_1)

print("===========================")