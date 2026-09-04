# 추론(Inference) 기초: 온도와 샘플링

- 추론 시점에는 모델이 계산한 다음 토큰 확률 분포에서 실제로 어떤 토큰을 뽑을지를 여러 파라미터로 조절
- 온도(temperature): 확률 분포를 얼마나 "뾰족하게" 또는 "평평하게" 만들지 조절하며, 낮을수록 결정적이고 예측 가능한 출력을 생성
- Top-p(뉴클리어스 샘플링): 고정된 개수 대신 누적 확률 기준으로 후보 토큰을 동적으로 필터링하는 방식
- 일반적인 파이프라인은 먼저 온도로 분포를 재조정한 뒤 Top-p로 후보를 추린 후 최종 샘플링을 수행 — 사실 기반 작업(요약, 코드 생성, Q&A)은 낮은 온도와 상대적으로 높은 Top-p를 조합하는 것이 권장됨
- 온도가 높아질수록 추측 디코딩(speculative decoding) 같은 지연시간 최적화 기법의 가속 효율은 떨어지는 경향이 있어, 정확도·다양성과 처리량(throughput) 사이에 트레이드오프가 존재

> Source: [How Temperature, Top-K, Top-P, and Min-P Control LLM Output](https://www.kenmuse.com/blog/how-temp-topk-topp-minp-control-llm-output/)
