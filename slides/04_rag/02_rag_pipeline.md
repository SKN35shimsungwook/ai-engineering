# 핵심 RAG 파이프라인

- Load(적재): PDF, 웹페이지, DB 등 원문 데이터를 수집
- Chunk(분할): 검색 단위로 문서를 작은 조각으로 나눔
- Embed(임베딩): 각 청크를 벡터로 변환
- Store(저장): 벡터 DB(예: Pinecone, Weaviate, Milvus)에 색인
- Retrieve → Augment → Generate: 질의와 유사한 청크를 검색해 프롬프트에 추가한 뒤 LLM이 답변 생성
- 최신 아키텍처는 단일 왕복이 아니라 여러 차례 검색-생성을 반복하는 모듈형 구조로 진화 중

> Source: [RAG Architecture: 4 Key Components & Example Implementation (2026)](https://cloudian.com/guides/ai-infrastructure/rag-architecture-4-key-components-example-implementation-2026/)
