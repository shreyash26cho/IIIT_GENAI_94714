from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """The series focuses on Asta, a young orphan raised in an orphanage.
He was born without magic power and trains his physical strength.
Yuno is gifted with wind magic.
Both dream of becoming the Wizard King."""

# RecursiveCharacterTextSplitter does NOT need a manual separator
text_splitter = CharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

docs = text_splitter.create_documents([text])

for i, doc in enumerate(docs):
    print(f"\nChunk {i + 1}:")
    print(doc.page_content)