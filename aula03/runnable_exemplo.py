""" Realizando as importações """
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnablePassthrough, RunnableParallel

""" Exemplo 1 - RunnableLambda """

# Criando uma função customizada (adição de +1 á entrada)

def add_one(x: int) -> int:
    return x + 1

# transformando a minha função genérica em um Runnable do LangChain, ou seja, ele implementa automáticamente os métodos `invoke` etc.
runnable: RunnableLambda[int, int] = RunnableLambda(add_one)

# Executando...
resposta: int = runnable.invoke(1)

print("------- RESPOSTA DO INVOKE EXEMPLO 1 - RunnableLambda -------")
print(resposta)
print("-------------------------------------------------------------")

# ===================================================================================================================================================

""" Exemplo 2 - RunnableSequence """

def mul_two(x: int) -> int:
    return x * 2

runnable_1: RunnableLambda[int, int] = RunnableLambda(add_one) # Convertendo a função de soma para runnable
runnable_2: RunnableLambda[int, int] = RunnableLambda(mul_two) # Convertendo a função de multiplicação para runnable

# Criando a cadeia sequencial
sequence: RunnableSequence[int, int] = runnable_1 | runnable_2

resposta: int = sequence.invoke(1)

print("\n------- RESPOSTA DO INVOKE EXEMPLO 2 - RunnableSequence -------")
print(resposta)
print("---------------------------------------------------------------")

# ===================================================================================================================================================

"""Exemplo 3 - RunnableParallel"""

def mul_three(x: int) -> int:
    return x * 3

runnable_1 = RunnableLambda(add_one) # Convertendo a função de multiplicação para 3 por nullable
runnable_2= RunnableLambda(mul_two) # Convertendo a função de multiplicação para 2 por nullable
runnable_3: RunnableLambda[int, int] = RunnableLambda(mul_three) # Convertendo a função de multiplicação para 3 por nullable

sequence = runnable_1 | {
    "mul_two": runnable_2,
    "mul-three": runnable_3,
}

# Ou usando o equivalente:
# sequence = runnable_1 | RunnableParallel({"mul_two: runnable_2, "mul_three": runnable_3})

# Ou também o equivalente:
# sequence = runnable_1 | RunnableParallel(mul_two=runnable_2, mul_three=runnable_3)

resposta: int = sequence.invoke(1)

print("\n------- RESPOSTA DO INVOKE EXEMPLO 3 - RunnableParallel -------")
print(resposta)
print("---------------------------------------------------------------")

# ===================================================================================================================================================

"""Exemplo 4 - RunnablePassthrough"""

chain: RunnableSequence[str, str] = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough()

# Independente de quantas vezes você "passar o resultado para frente", a entrada não é alterada.RunnablePassthrough

response: str = chain.invoke("Olá")

print("\n------- RESPOSTA DO INVOKE EXEMPLO 4 - RunnablePassthrough -------")
print(response)
print("--------------------------------------------------------------------")

# ===================================================================================================================================================

"""Exemplo 5 - RunnablePassthrough + RunnableLambda"""

def entrada_para_letras_maiusculas(entrada: str) -> str:
    saida =  entrada.upper()
    return saida

chain = RunnablePassthrough() | RunnableLambda(entrada_para_letras_maiusculas) | RunnablePassthrough()

# Neste caso vamos receber a entrada do usuário, passar para a função 'entrada_para_letras_maiusculas, transformar olá -> OLÁ e passar para frente.
resposta = chain.invoke("olá")

print("\n------- RESPOSTA DO INVOKE EXEMPLO 5 - RunnablePassthrough + RunnableLambda -------")
print(resposta)
print("-------------------------------------------------------------------------------------")

# ===================================================================================================================================================

"""Exemplo 6 - Operador Assign"""

# https://python.langchain.com/docs/how_to/assign/

# Pego a entrada e passo para frente e na mesma etapa, eu antes de passar para frente eu adiciono uma chave 'multiplica_3'
# no dicionário de entrada multiplicando 3.

runnable = RunnablePassthrough() | RunnablePassthrough.assign(multiplica_3=lambda x: x["num"] * 3)

resposta = runnable.invoke({"num": 1})

print("\n------- RESPOSTA DO INVOKE EXEMPLO 6 - Operador Assign -------")
print(resposta)
print("----------------------------------------------------------------")