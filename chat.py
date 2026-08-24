from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
import time
from config import *


#加载模型
embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5"
)

#搭建数据检索库
vector_db = FAISS.load_local(
    "./faiss_db",
    embedding,
    allow_dangerous_deserialization=True
)

#调用千问
llm = ChatTongyi(model="qwen-turbo",
                 dashscope_api_key=dashscope_api_key)

#规范千问职责
prompt = ChatPromptTemplate.from_template(
"""
你是一个知识库问答助手。请严格根据下面提供的资料回答。如果资料没有相关内容，请回答："知识库中没有相关信息"
资料：{context}
问题：{question}
"""
)

#循环问答
def ask_question(question):
    #FAISS检索
    docs = vector_db.similarity_search(question,k=3)
    #拼接检索结果
    context = "\n\n".join([
            doc.page_content
            for doc in docs
        ])

    #规范化输入格式
    messages = prompt.format_messages(context=context,question=question)

    #调大千问回答
    response = llm.invoke(messages)
    return response.content

