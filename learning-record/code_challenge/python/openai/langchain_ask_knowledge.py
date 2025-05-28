import os
from langchain_deepseek import ChatDeepSeek
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()
# Ensure the DeepSeek API key is set
if not os.getenv("DEEPSEEK_API_KEY"):
    raise EnvironmentError("Please set the DEEPSEEK_API_KEY environment variable.")

# Load the text file as a document
loader = TextLoader("knowledge_base.txt", encoding="utf-8")
documents = loader.load()

# Split the document into manageable chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Generate embeddings using Hugging Face's sentence-transformers model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

# Initialize the DeepSeek chat model
llm = ChatDeepSeek(
    model="deepseek-chat",  # Specify the DeepSeek model
    temperature=0.7,        # Adjust the creativity of the responses
    max_tokens=500,         # Limit the response length
    max_retries=2           # Retry on failure
)

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# Interactive terminal loop
print("Welcome to the DeepSeek Knowledge Base Chat!")
print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = qa_chain.run(query)
    print(f"DeepSeek: {response}\n")
