# 검색 방식: Dense vs Sparse vs Hybrid

- Sparse(BM25): TF-IDF 기반 통계적 키워드 매칭 — 제품코드·고유명사 등 정확한 용어에 강함
- Dense(벡터 검색): 임베딩 기반 의미 유사도 검색 — 동의어·패러프레이즈 등 문맥적 매칭에 강함
- Hybrid(하이브리드) 검색: 두 방식을 Reciprocal Rank Fusion(RRF)으로 결합
- 하이브리드 검색이 dense 단독 대비 NDCG를 26~31% 향상시켰다는 벤치마크 결과 존재
- 실무에서는 BM25가 놓치는 의미적 매칭과 dense가 놓치는 정확 키워드를 서로 보완

> Source: [Hybrid Search for RAG: Combining BM25 and Dense Vector Search (2026 Guide)](https://denser.ai/blog/hybrid-search-for-rag/)
> Source: [Hybrid RAG: Dense and Sparse Retrieval for Better AI Answers](https://atlan.com/know/hybrid-rag/)
