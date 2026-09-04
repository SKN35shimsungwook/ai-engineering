# 배포 패턴: API 기반 vs 자체 호스팅

- API 기반(OpenAI, Anthropic 등 관리형 API)은 인프라 관리 부담이 없고 최신 모델에 빠르게 접근 가능하지만 트래픽이 많아지면 토큰당 비용이 누적됨
- 자체 호스팅(오픈소스 모델을 자체 GPU에서 서빙)은 데이터가 경계 내부에 머물고 지연시간이 더 예측 가능하며, 대량 트래픽에서 장기적으로 비용 이점이 있음
- 손익분기점은 사용량에 좌우됨 — 하루 약 1,600만~2,200만 토큰 수준을 넘으면 자체 호스팅이 API보다 저렴해진다는 분석도 있음
- 숨은 비용 주의: 자체 호스팅은 매달 10~20시간의 엔지니어링 유지보수 시간이 필요해 인건비까지 고려해야 진짜 비용 비교가 가능
- 규제, 데이터 상주(data residency) 요건, 결정적 지연시간이 필요한 경우 자체 호스팅이 우선 고려 대상

> Source: [GPT-6 API vs Self-Hosted LLMs: Cost, Latency, and Privacy in 2026](https://www.spheron.network/blog/gpt-6-vs-self-hosted-llm-2026/)
> Source: [Self-Hosted LLM vs API: The $4,200/mo Break-Even Point](https://www.braincuber.com/blog/self-hosted-llms-vs-api-based-llms-cost-performance-analysis)
