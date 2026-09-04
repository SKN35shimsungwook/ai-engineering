# 오픈웨이트 vs 폐쇄형 모델

- 폐쇄형(Claude, GPT, Gemini 등): API 형태로만 제공되며 최신 성능·안정적인 운영·기업용 지원을 받을 수 있지만 데이터가 외부로 전송되고 벤더 종속 위험이 있음
- 오픈웨이트(Llama, DeepSeek, Qwen, GLM 등): 가중치를 직접 다운로드해 자체 인프라에서 구동 가능해 데이터 주권과 비용 효율성 확보에 유리
- 코딩·범용 작업 벤치마크에서는 격차가 크게 좁혀짐 — 예: GLM-5.1이 SWE-Bench Pro에서 58.4%를 기록해 GPT-5.4(57.7%), Claude Opus 4.6(57.3%)를 근소하게 앞선 사례도 있음
- 다만 가장 어려운 추론 과제와 깊은 에이전트 루프에서는 여전히 서구 프론티어(Claude·GPT 최상위 티어)가 우위를 유지
- "오픈소스"라는 표현과 달리 실제 라이선스는 Apache 2.0·MIT 같은 완전 개방형부터 사용량 제한·지역 제한·매출 조건이 붙은 경우까지 다양해 실제 제품에 적용하기 전 라이선스 확인이 필수

> Source: [Best Open-Weight LLMs 2026: DeepSeek vs Qwen vs Kimi vs GLM vs Llama](https://wavect.io/blog/open-weight-llm-comparison-2026/)
