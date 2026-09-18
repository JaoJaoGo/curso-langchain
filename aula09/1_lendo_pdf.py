from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("exemplo_arquivo.pdf")
pages_sinc = loader.load()

# Aqui verificamos que pages_sinc é uma lista de 'Document':
print('\n------ Imprimindo o resultado ------\n')
print(pages_sinc)

print('\n------ Imprimindo o resultado ------\n')
# Acessando os valores carregados:
for elemento in pages_sinc:
    print('----- Página Início -----')
    print(f"Conteúdo: {elemento.page_content}\n")
    print(f'Metadado: {elemento.metadata}')
    print('----- Página Fim -----')
print("PARAR AQUI")