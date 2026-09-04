# RAG 한눈에 정리

- 문제: LLM의 지식 단절과 환각 → 해결책: 외부 지식을 검색해 근거로 제시하는 RAG
- 파이프라인 순서: 적재 → 청킹 → 임베딩 → 저장 → 검색 → (리랭킹) → 프롬프트 증강 → 생성
- 검색 품질은 청킹 전략, 임베딩 모델, 하이브리드 검색, 리랭킹이 함께 결정
- 고급 패턴(HyDE, Agentic RAG, GraphRAG)은 복잡한 질의·다단계 추론에서 성능을 끌어올림
- 평가(RAGAS 등)와 프로덕션 운영 노하우 없이는 데모 단계를 벗어나기 어려움
- 아래 영상은 RAG의 개념과 구현 흐름을 20분 분량으로 실습과 함께 설명

> Source: [RAG Explained in 20 Minutes | Retrieval Augmented Generation + Hands on Project](https://www.youtube.com/watch?v=RosLeHGBLoY)
