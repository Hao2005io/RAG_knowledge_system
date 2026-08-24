from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatTongyi

#加载文档
file_path = "./data/math_all.docx"
loader =  Docx2txtLoader(file_path)
document = loader.load()

#切块
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(document)
print("切割后数量:", len(chunks))

#加载模型
embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)

#创建FAISS数据库并保存
vector_db = FAISS.from_documents(
    chunks,
    embedding
)
vector_db.save_local(
    "./faiss_db"
)

