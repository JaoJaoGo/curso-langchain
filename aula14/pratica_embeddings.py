from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

documents = [
    "Olá!",
    "Quantos anos você tem?",
    "Qual o seu nome?",
    "Meu amigo se chama Flávio",
    "Oi!"
]

embeddings = embeddings_model.embed_documents(documents)

print("----- QUANTOS VETORES EXISTEM -----")
print(len(embeddings))
print("-----------------------------------------------------------------")

print("\n----- DIMENSÃO DOS VETORES -----")
print("O Modelo de embeddings all-MiniLM-L6-v2 do HuggingFace ten um tamanho de 384.")
print(len(embeddings[0]))
print("-----------------------------------------------------------------")

print("\n----- CONVERTENDO UMA PERGUNTA EM EMBEDDING -----")
embedded_query = embeddings_model.embed_query("Qual é o nome do seu amigo?")

print("\n----- DIMENSÃO DOS VETORES -----")
print("Como na query tmb utilizamos o mesmo modelo, a dimensão será igual dos documentos.")
print(len(embedded_query))

print("-----------------------------------------------------------------")
print("\n----- Imprimindo o vetor Numérico -----")
print(embedded_query)