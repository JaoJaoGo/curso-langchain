from chonkie import SemanticChunker
from langchain_core.documents import Document

text = """A inteligência artificial (IA) é uma área da ciência da computação que tem revolucionado diversas \
indústrias e aspectos da vida cotidiana. Mas, o que realmente significa "inteligência artificial"? Trata-se de sistemas \
computacionais capazes de realizar tarefas que, anteriormente, só lowered ser executadas por seres humanos, como \
reconhecimento de fala, tomada de decisão e aprendizado com dados. Impressionante, não é? Esses sistemas utilizam \
algoritmos avançados e grandes volumes de dados para identificar padrões, adaptarem-se a novas situações e fornecerem \
soluções inovadoras.

Um dos maiores avanços recentes em IA é o aprendizado profundo (ou deep learning). Essa técnica permite que máquinas \
realizem tarefas extremamente complexas, como diagnosticar doenças a partir de imagens médicas ou até mesmo compor \
músicas! Curioso como isso funciona? Redes neurais artificiais – inspiradas no funcionamento do cérebro humano – \
processam informações em múltiplas camadas, identificando nuances que seriam impossíveis para métodos tradicionais. \
Como resultado, a IA tem transformado áreas como saúde, finanças e transporte, promovendo eficiência e inovação em \
escala global.

No entanto, a expansão da inteligência artificial também levanta questões importantes. Estamos preparados para lidar \
com os desafios éticos que a IA traz? Por exemplo: como garantir que algoritmos de IA sejam imparciais e inclusivos? \
Além disso, há preocupações sobre o impacto no mercado de trabalho – algumas profissões podem ser substituídas por \
máquinas. Apesar desses desafios, uma coisa é certa: a inteligência artificial já não é mais uma tecnologia do futuro; \
é uma realidade do presente, moldando o mundo ao nosso redor com potencial ilimitado!"""

texto_original = Document(page_content=text)

# Inicializa o Chunker Semântico Local Gratuito (baixa o MiniLM automaticamente)
chunker = SemanticChunker(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    similarity_threshold=0.5
)

# Quebra o texto semânticamente
chunks = chunker.chunk(texto_original.page_content)

# Transforma de volta para a lista de Documentos padrão do LangChain se precisar alimentar seu banco vector
docs_finais = [Document(page_content=c.text) for c in chunks]

for i, pedaco in enumerate(docs_finais):
    print("--" * 20)
    print(f"Chunk {i+1}:")
    print(pedaco.page_content)
    print("--" * 20)