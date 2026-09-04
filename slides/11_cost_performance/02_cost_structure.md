# LLM API 비용 구조 이해하기

- 과금은 입력 토큰(prompt)과 출력 토큰(completion)을 따로 계산하며, 출력 토큰이 훨씬 비쌈
- 2026년 기준 예시: Claude Sonnet 5는 입력 100만 토큰당 2달러, 출력 100만 토큰당 10달러
- 저가형 모델(GPT-5.6 Luna 등)은 입력 0.2달러/출력 1.2달러 수준까지 내려가고,
  최상위 모델(GPT-5.5 Pro 등)은 입력 30달러/출력 180달러까지 올라가는 등 가격 폭이 매우 큼
- 대부분의 공급자에서 출력 토큰 단가가 입력 대비 5~6배 높아, 응답 길이가 비용을 좌우하는 핵심 변수
- 2025년 대비 2026년 업계 전반 토큰 단가는 경쟁 심화로 큰 폭으로 하락하는 추세

> Source: [LLM API pricing comparison in 2026: every major model ranked by cost](https://www.cloudzero.com/blog/llm-api-pricing-comparison/)
