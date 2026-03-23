from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-zh-v1.5")
model.save("./bge-small-zh-v1.5")

print("下载并保存完成")