# AI 데이터 파이프라인 설계 시 고려사항

- 신선도(freshness): 임베딩은 "의미"만 비교하므로 오래된 문서도 최신 문서와 똑같이 높은 점수를 받을 수 있어,
  변경분을 지속적으로 반영하는 증분 인덱싱이 필요
- 버전 관리: 청크마다 문서 버전을 태깅해 이전 버전을 폐기(tombstone)하고 무엇을 모델이 봤는지 감사 가능하게 유지
- 임베딩 모델 버전도 고정(pin)해야 함 — 모델을 바꾸면 전체 코퍼스의 검색 결과가 예고 없이 달라짐
- PII 처리: 수집 단계에서부터 자동 PII 탐지·마스킹을 적용하고, 검색 계층에 접근 제어를 둬야 함
- 권한 없는 문서가 검색 결과에 노출되면 LLM이 의도치 않은 정보 유출 통로가 될 수 있음

> Source: [The RAG Freshness Problem: How Stale Embeddings Silently Wreck Retrieval Quality](https://tianpan.co/blog/2026-04-10-rag-freshness-problem-stale-embeddings-silent-failure)
> Source: [RAG Series – Embedding Versioning with pgvector](https://www.dbi-services.com/blog/rag-series-embedding-versioning-with-pgvector-why-event-driven-architecture-is-a-precondition-to-ai-data-workflows/)
