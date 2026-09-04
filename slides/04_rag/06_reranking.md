# 리랭킹(Reranking)

- 1차 검색(하이브리드/벡터)으로 후보군을 넓게 뽑은 뒤, 정밀도를 높이는 2차 재정렬 단계
- Cross-encoder 기반 리랭커가 프로덕션 RAG 파이프라인의 권장 3단계 구성 요소로 자리잡음
- 단, 리랭커는 이미 검색된 후보만 재정렬할 뿐 — 애초에 검색이 놓친 문서는 되살릴 수 없음
- 하이브리드 검색 + 신경망 리랭킹 2단계 파이프라인이 Recall@5 0.816, MRR@3 0.605를 기록해 단일 단계 방식을 크게 앞섬
- 리랭킹 생략 시 무관한 청크가 섞이는 비율이 크게 늘고, 경량 리랭커 도입만으로 무관 검색 결과가 절반 이상 감소한 사례 보고

> Source: [Hybrid Search for RAG: BM25, SPLADE, and Vector Search Combined](https://www.premai.io/blog/hybrid-search-for-rag-bm25-splade-and-vector-search-combined/)
> Source: [Six Lessons Learned Building RAG Systems in Production](https://towardsdatascience.com/six-lessons-learned-building-rag-systems-in-production/)
