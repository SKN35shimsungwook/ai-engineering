# 지연시간(latency) 최적화 기법

- 스트리밍: 전체 응답이 끝날 때까지 기다리지 않고 토큰이 생성되는 대로 전송 —
  체감 대기시간을 1초 이내로 줄이는 가장 손쉬운 방법 (총 생성 시간 자체는 줄지 않음)
- 병렬 호출: 서로 의존하지 않는 단계는 동시에 LLM을 호출해 전체 파이프라인 시간을 단축
- 추측 실행(speculative execution): 다음 단계 결과를 미리 예측해 병렬로 실행, 예측이 맞으면 지연시간 절감
- 프롬프트 길이 축소: 불필요한 컨텍스트를 줄이면 처리 시간과 비용을 동시에 낮출 수 있음
- 사용자 체감 기준으로 400~800ms를 넘는 지연은 이탈로 이어지는 경우가 많아 인터랙티브 앱에서는 핵심 지표

> Source: [Latency optimization | OpenAI API](https://developers.openai.com/api/docs/guides/latency-optimization)
> Source: [LLM Latency in Production: What Actually Moves the Needle](https://tianpan.co/blog/2025-10-30-llm-latency-optimization-production)
