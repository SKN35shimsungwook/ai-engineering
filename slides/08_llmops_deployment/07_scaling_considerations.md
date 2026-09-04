# 스케일링: 지연시간, 처리량, 속도 제한, 비용

- 요청량이 늘어날수록 지연시간(latency)과 처리량(throughput) 사이의 트레이드오프가 커짐 — GPU 포화 시 배칭 전략을 재조정해야 함
- 대부분의 상용 API는 분당/일당 요청 수, 토큰 수에 속도 제한(rate limit)을 두어 급격한 트래픽 증가에 대비한 재시도·백오프 로직이 필요
- 비용은 토큰 단가뿐 아니라 캐싱 적중률, 프롬프트 길이, 모델 크기 선택(작은 모델로 라우팅)에 크게 좌우됨
- 트래픽 패턴에 따라 여러 모델 크기/제공자를 라우팅하는 모델 라우터(model router) 아키텍처가 비용 최적화에 널리 쓰임
- 사용량이 임계치(하루 약 1,600만 토큰 이상 등)를 넘으면 자체 호스팅으로 전환하는 하이브리드 전략도 고려 대상

> Source: [GPT-6 API vs Self-Hosted LLMs: Cost, Latency, and Privacy in 2026](https://www.spheron.network/blog/gpt-6-vs-self-hosted-llm-2026/)
