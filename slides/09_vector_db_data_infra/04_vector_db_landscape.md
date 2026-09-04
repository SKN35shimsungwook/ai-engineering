# 2026년 벡터 데이터베이스 생태계

- Pinecone: 완전관리형 서버리스, 멀티테넌시와 하이브리드(BM25+벡터) 검색, 내장 임베딩/재랭킹 제공
- Weaviate: 벡터+BM25+메타데이터 필터를 결합한 하이브리드 검색이 강점, 오픈소스 모듈형 구조
- Qdrant: 단일 바이너리로 배포 가능, 스파스 벡터(SPLADE)·ColBERT 멀티벡터 지원, 무료 티어가 넉넉
- Milvus(Zilliz): 분산 아키텍처로 수십억 벡터·고QPS 처리에 강하지만 운영 난도가 높음
- 신규 RAG 프로젝트가 벡터 1천만 개 이하라면 기존 Postgres에 pgvector를 얹는 방식이 가장 단순한 출발점

> Source: [Top 15 Vector Databases in 2026](https://medium.com/@pratik-rupareliya/top-15-vector-databases-in-2026-a-production-decision-guide-from-100-enterprise-deployments-dd58a04f51a5)
> Source: [Vector Database Comparison 2026: Pinecone vs Weaviate vs Qdrant vs Milvus vs pgvector](https://aiml.qa/vector-database-comparison-2026/)
