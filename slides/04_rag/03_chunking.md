# 청킹 전략: 크기와 겹침

- 일반적인 시작점은 400~512 토큰 청크; 용도에 따라 조정 필요
- 사실 조회형 질문은 작은 청크(256~512 토큰), 분석형 질문은 큰 청크(512~1024 토큰)가 유리
- 겹침(overlap)은 청크 크기의 10~20%가 일반적 권장값 (500토큰 청크 → 50~100토큰 겹침)
- Fixed-size(고정 크기)는 구현이 쉽지만 문맥이 중간에 끊기는 문제 발생
- Recursive(재귀적) 청킹: 문단 → 줄바꿈 → 공백 순으로 구분자를 적용해 자연스럽게 분할
- Semantic(의미 기반) 청킹은 재현율을 91~92%까지 끌어올리지만 문장 단위 임베딩 비용이 추가로 발생

> Source: [Best Chunking Strategies for RAG (and LLMs) in 2026](https://www.firecrawl.dev/blog/best-chunking-strategies-rag)
> Source: [Chunking Strategies for RAG: Best Practices and Key Methods](https://unstructured.io/blog/chunking-for-rag-best-practices)
