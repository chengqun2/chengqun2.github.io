from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader("knowledge_base.txt", encoding="utf-8")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import HuggingFacePipeline

model_name = "gpt2"  # Replace with your desired local model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=500)
llm = HuggingFacePipeline(pipeline=llm_pipeline)


from langchain.chains import RetrievalQA

retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)


query = "What is the capital of France?"
answer = qa_chain.run(query)
print(answer)
