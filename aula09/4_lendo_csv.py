from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="exemplo_arquivo.csv")
data = loader.load()

linha = 0
for record in data:
    print(f"Imprimindo linha: {linha}")
    print("----------")
    print(record)
    print('----------')
    linha += 1
print("---- Imprimindo de forma estruturada ----")
linha = 0
for record in data:
    print(f"Imprimindo linha: {linha}")
    print(f"Conteúdo: {record.page_content}")
    print('----------')
    linha += 1
print("PARAR AQUI")