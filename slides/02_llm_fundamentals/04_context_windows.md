# 컨텍스트 윈도우

- 컨텍스트 윈도우는 모델이 한 번에 참고할 수 있는 입력+출력 토큰의 총량을 의미
- 2026년 9월 기준 Claude Opus 5, Sonnet 5, Fable 5.1 등 주요 모델은 기본 100만(1M) 토큰 컨텍스트를 지원하며 최대 출력은 12만 8천 토큰 수준
- OpenAI GPT-5.6 계열(Sol/Terra/Luna)도 약 105만 토큰 컨텍스트로 통일되었고, Gemini 3.1 Pro는 최대 200만 토큰까지 지원
- Llama 4 Scout는 1,000만 토큰 컨텍스트를 광고하지만, 실제로 그 정도 길이에서 품질이 유지된다는 벤치마크는 아직 확인되지 않음
- 컨텍스트가 커질수록 비용도 커짐 — 동일한 100만 토큰을 채우는 비용이 모델에 따라 0.14달러에서 10달러까지 약 71배 차이가 남

> Source: [Claude Platform 릴리스 노트](https://platform.claude.com/docs/en/release-notes/overview)
> Source: [LLM Context Window Comparison (2026) - Morph](https://www.morphllm.com/llm-context-window-comparison)
