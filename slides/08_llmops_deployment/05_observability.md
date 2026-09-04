# LLM 애플리케이션 관측가능성(Observability)

- 프롬프트, 완성(completion), 검색 결과, 도구 호출, 토큰 수, 지연시간, 비용까지 파이프라인의 모든 스팬(span)을 기록하는 트레이싱이 핵심
- Langfuse: 오픈소스로 셀프호스팅 가능, 멀티턴 대화 트레이싱과 프롬프트 버전 관리, LLM-as-judge 평가를 통합 제공
- LangSmith: LangChain/LangGraph 기반 애플리케이션과 네이티브로 통합되어 트레이스 조사에 강점
- Helicone: 프록시 방식으로 가장 빠르게 설정 가능하고 비용 추적을 자동화
- 관측가능성 데이터는 실시간 이상 탐지뿐 아니라, 프로덕션에서 주기적으로 품질을 재평가하는 온라인 평가의 입력으로도 활용됨

> Source: [Top LLM Observability and Evaluation Platforms in 2026](https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/)
> Source: [Best LLM Observability Tools in 2026](https://www.firecrawl.dev/blog/best-llm-observability-tools)
