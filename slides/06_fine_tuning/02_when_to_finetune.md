# 파인튜닝 vs 프롬프트 vs RAG: 언제 무엇을 쓸까

- 프롬프트 엔지니어링이 가장 빠르고 저렴한 시작점 — 모델 가중치를 바꾸지 않고 입력만으로 동작을 제어
- RAG는 모델이 모르는 최신/도메인 지식을 검색으로 보강할 때 적합 (지식 정확도 문제 해결)
- 파인튜닝은 "지식"이 아니라 "행동"을 바꿀 때 유리 — 출력 형식, 말투, 도메인 전문 용어, 반복적 추론 패턴을 각인
- 실제 프로덕션에서는 세 가지를 함께 쓰는 경우가 많음: 파인튜닝된 소형 모델 + RAG로 최신 지식 보강 + 프롬프트로 세부 제어
- 대량 트래픽에서는 데이터 투자 이후 파인튜닝이 장기적으로 비용 이점을 가짐

> Source: [RAG vs Fine-Tuning in 2026: A Decision Framework for LLM Teams](https://winder.ai/rag-vs-fine-tuning-2026-decision-framework/)
> Source: [RAG vs. Fine-tuning vs. Prompt Engineering: The Complete Guide to AI Optimization](https://www.news.aakashg.com/p/rag-vs-fine-tuning-vs-prompt-engineering)
