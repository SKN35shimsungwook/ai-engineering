# 비용 절감 기법

- 프롬프트 캐싱: 시스템 프롬프트, 도구 정의처럼 반복되는 고정 구간을 캐싱해 입력 토큰 비용을 최대 90%까지 절감
- 모델 라우팅: 질의 난이도를 분류해 쉬운 작업은 저가 모델로, 어려운 작업만 고성능 모델로 보내 40~70% 절감
- 모델 캐스케이딩: 저가 모델의 응답 품질을 점수화해 기준 미달일 때만 상위 모델로 에스컬레이션
- 배치 처리: 즉시 응답이 필요 없는 작업은 배치 API로 처리해 약 50% 할인
- 출력 형식 최적화: 자유서술 대신 구조화된 JSON 출력을 요구해 불필요한 출력 토큰을 줄이는 것도 효과적

> Source: [LLM Routing and Model Cascades: How to Cut AI Costs Without Sacrificing Quality](https://tianpan.co/blog/2025-11-03-llm-routing-model-cascades)
> Source: [LLM Cost Optimization: 5 Levers to Cut API Spend 70-85%](https://www.morphllm.com/llm-cost-optimization)
