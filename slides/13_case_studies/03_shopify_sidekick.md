# Shopify Sidekick — 에이전트 확장의 함정과 해법

- 머천트를 돕는 AI 에이전트, 50개 이상의 도구(tool) 중에서 선택해 작업을 수행
- 도구가 20개에서 50개 이상으로 늘며 시스템 프롬프트가 비대해지는 "천 개 지시의 죽음" 문제 발생
- 해결책: 모든 지침을 프롬프트에 넣는 대신, 도구 호출 시점에 필요한 지침만 동적으로 제공(Just-in-Time Instructions)
- "감으로 하는 테스트"를 버리고 LLM 판정자(judge)를 도입 — 인간 평가자와의 일치도(Cohen's Kappa)가 0.02에서 0.61로 개선(인간 간 일치도는 0.69)
- GRPO 강화학습 훈련으로 문법 정확도가 약 93%에서 99%로 상승

> Source: [Building production-ready agentic systems: Lessons from Shopify Sidekick](https://shopify.engineering/building-production-ready-agentic-systems)
