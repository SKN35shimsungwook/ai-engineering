# RAG는 왜 필요한가

- LLM은 학습 시점 이후 정보나 사내 비공개 데이터를 알지 못함 (지식 단절)
- 파라미터 안에 없는 사실을 그럴듯하게 지어내는 "환각(hallucination)" 문제 완화
- 매번 모델을 재학습(fine-tuning)하는 대신, 외부 지식 소스를 검색해 프롬프트에 주입
- 답변의 근거가 된 문서를 함께 제시해 사용자가 출처를 검증할 수 있게 함
- 2026년 기준 거의 모든 챗봇·사내 지식베이스·AI 어시스턴트가 RAG를 기본 구조로 채택

> Source: [What Is RAG? How Retrieval-Augmented Generation Works in 2026](https://atlan.com/know/what-is-rag/)
> Source: [RAG Architecture Explained: A Comprehensive Guide (2026)](https://orq.ai/blog/rag-architecture)
