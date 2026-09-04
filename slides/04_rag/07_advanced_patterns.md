# 고급 RAG 패턴

- Query rewriting(질의 재작성): 사용자의 모호한 질문을 검색에 유리한 형태로 변환
- HyDE(Hypothetical Document Embeddings): 가상의 답변을 먼저 생성해 임베딩한 뒤 그것으로 검색
- Agentic RAG: LLM이 검색 앞단이 아니라 루프 안에서 직접 "언제, 무엇을 검색할지" 판단 (Self-RAG, FLARE 등)
- GraphRAG: 비정형 텍스트로부터 지식 그래프를 구축해 다단계(multi-hop) 추론 질문에 대응
  - 예: "2024 올림픽 개최국의 GDP는?" → 1홉(개최국 조회) → 2홉(GDP 조회)
- Microsoft Research가 2024년 GraphRAG를 MIT 라이선스 오픈소스로 공개, 이후 LazyGraphRAG·DRIFT Search 등으로 발전
- 2026년 트렌드는 질의 복잡도에 따라 검색 전략을 동적으로 선택하는 Adaptive RAG

> Source: [GraphRAG: New tool for complex data discovery now on GitHub](https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/)
> Source: [20 Advanced RAG Types to Know in 2026](https://www.turingpost.com/p/ragtypes)
