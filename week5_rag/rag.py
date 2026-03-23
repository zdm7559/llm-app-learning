import os
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from utils import read_file, list_text_files

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

CHAT_MODEL = os.getenv("CHAT_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    chunks = []
    start = 0
    text = text.strip()

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def load_documents(data_dir: str) -> list[dict]:
    """
    读取 data_dir 下的所有 txt / md 文件，并切分成 chunk
    返回:
    [
        {"source": "data/doc1.txt", "chunk_id": 0, "text": "..."},
        ...
    ]
    """
    docs = []
    file_paths = list_text_files(data_dir)
    for file_path in file_paths:
        content = read_file(file_path)
        chunks = chunk_text(content)

        for i, chunk in enumerate(chunks):
            docs.append({
                "source": file_path,
                "chunk_id": i,
                "text": chunk
            })
    return docs


embedding_model = SentenceTransformer("BAAI/bge-small-zh-v1.5")

def get_embedding(text: str) -> list[float]:
    vec = embedding_model.encode(text, normalize_embeddings=True)
    return vec.tolist()

    return response.data[0].embedding

def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    if denominator == 0:
        return 0.0
    
    return float(np.dot(v1, v2) / denominator)

def build_vector_store(data_dir: str) -> list[dict]:
    docs = load_documents(data_dir)

    for doc in docs:
        doc["embedding"] = get_embedding(doc["text"])

    return docs

def retrieve(query: str, vector_store: list[dict], top_k: int = 3) -> list[dict]:
    """
    对 query 做 embedding，然后跟每个 chunk 算相似度，取 top_k
    """
    query_embedding = get_embedding(query)
    
    scored_docs = []
    for doc in vector_store:
        score = cosine_similarity(query_embedding, doc["embedding"])
        scored_docs.append({
            "source": doc["source"],
            "chunk_id": doc["chunk_id"],
            "text": doc["text"],
            "score": score
        })

        scored_docs.sort(key=lambda x: x["score"], reverse=True)

        return scored_docs[:top_k]
    
def build_context(retrieved_docs: list[dict]) -> str:
    """
    把检索结果拼成上下文
    """
    context_parts = []

    for i, doc in enumerate(retrieved_docs, start=1):
        part = (
            f"[片段{i}]\n"
            f"来源: {doc['source']} | chunk_id: {doc['chunk_id']} | score: {doc['score']:.4f}\n"
            f"内容: {doc['text']}\n"
        )
        context_parts.append(part)

    return "\n".join(context_parts)

def generate_answer(query: str, context: str) -> str:
    prompt = f"""你是一个基于知识库回答问题的助手。
请严格依据给定的上下文回答问题。
如果上下文无法支持答案，请明确说“我无法从给定资料中确定答案”。

以下是检索到的上下文：
{context}

用户问题：
{query}
"""
    
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "你是一个严谨、清晰的中文知识库问答助手。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content

def ask(query: str, vector_store: list[dict], top_k: int = 3) -> dict:
    retrieved_docs = retrieve(query, vector_store, top_k=top_k)
    context = build_context(retrieved_docs)
    answer = generate_answer(query, context)

    return {
        "query": query,
        "answer": answer,
        "retrieved_docs": retrieved_docs
    }

