# 基于 RAG 的高中数学本地知识库问答系统

## 1. 项目简介

本项目基于 RAG（Retrieval-Augmented Generation，检索增强生成）技术搭建高中数学本地知识库问答系统。

系统将高中数学知识文档进行解析和文本切分，通过中文 Embedding 模型将知识内容转换为向量，并使用 FAISS 构建本地向量数据库。用户提出问题后，系统首先从知识库中进行语义检索，获取与问题相关的知识内容，再结合大语言模型生成最终回答。

项目使用 LangChain 串联文档处理、文本向量化、知识检索和大语言模型调用流程，并使用 Docker 完成系统部署，实现可通过 Web 页面进行交互的本地知识库问答系统。

## 2. 技术栈

- Python
- LangChain
- PyTorch / HuggingFace
- BGE 中文 Embedding 模型
- FAISS
- 大语言模型 API
- FastAPI
- Docker

## 3. 系统流程

```text
高中数学知识文档
        ↓
文档解析
        ↓
文本切分
        ↓
Embedding 向量化
        ↓
FAISS 向量数据库
        ↓
用户输入问题
        ↓
语义相似度检索
        ↓
获取相关知识
        ↓
结合大语言模型生成回答
        ↓
Web 页面返回结果
