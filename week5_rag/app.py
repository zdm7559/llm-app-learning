from rag import build_vector_store, ask

def main():
    print("正在加载文档并构建向量库...")
    # vector_store = build_vector_store("data")
    # print(f"知识库已构建完成，共 {len(vector_store)} 个 chunks。\n")

    # while True:
    #     query = input("问题（输入 exit 退出）：").strip()
    #     if query.lower() == "exit":
    #         print("已退出。")
    #         break

    #     result = ask(query, vector_store, top_k=3)
    #     print("\n========== 回答 ==========")
    #     print(result["answer"])

    #     print("\n========== 检索到的片段 ==========")
    #     for i, doc in enumerate(result["retrieved_docs"], start=1):
    #         print(f"\n--- Top {i} ---")
    #         print(f"来源: {doc['source']}")
    #         print(f"chunk_id: {doc['chunk_id']}")
    #         print(f"score: {doc['score']:.4f}")
    #         print(f"内容: {doc['text']}")

    #     print("\n" + "=" * 30 + "\n")

if __name__ == "__main__":
    print("---------------")
    # main()