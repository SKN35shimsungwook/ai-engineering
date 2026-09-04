# 2026년 실전 LLM 평가 도구

- Braintrust: 전용 평가 워크스페이스와 프롬프트 플레이그라운드를 제공, 예측 가능한 평가량을 가진 팀에 적합
- LangSmith: LangChain/LangGraph로 구축한 애플리케이션과 네이티브로 통합, 트레이스 조사와 데이터셋 관리에 강점
- Arize Phoenix: 무료 오픈소스로 로컬 자체 호스팅 가능, OTLP 기반 어떤 소스든 채점 가능
- DeepEval: 50개 이상의 사전 구축된 평가 지표를 오픈소스로 제공, RAGAS와 함께 CI/CD 게이팅용 경량 프레임워크로 자주 사용
- 실무에서는 CI/CD 게이팅용 경량 프레임워크(DeepEval, RAGAS)와 사람 평가/회귀 추적용 플랫폼(Braintrust, LangSmith, Arize)을 함께 조합하는 경우가 많음

> Source: [Best LLM Evaluation Tools 2026](https://pydantic.dev/articles/best-llm-evaluation-tools)
> Source: [Top LLM Observability and Evaluation Platforms in 2026](https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/)
