# 추론 최적화: 양자화, 배칭, 캐싱, 추측 디코딩

- 양자화(Quantization): FP8/INT8/INT4 등으로 가중치와 KV 캐시 정밀도를 낮춰 메모리 사용량을 줄이고 처리량을 늘림 — FP8은 품질 손실을 최소화하며 처리량을 약 2배로 향상
- 연속 배칭(Continuous Batching): 끝난 요청을 즉시 빼고 새 요청을 채워 넣어 정적 배칭 대비 2~4배의 실질 처리량 달성
- PagedAttention: vLLM이 도입한 기법으로, KV 캐시를 작은 페이지 단위로 필요할 때만 할당해 메모리 활용률을 2~4배 개선
- 추측 디코딩(Speculative Decoding): 작은 초안 모델이 후보 토큰을 여러 개 생성하면 큰 모델이 한 번의 순전파로 검증 — 배치가 작을 때 특히 효과적
- 캐싱(프롬프트/응답 캐시)은 반복되는 질의나 공통 시스템 프롬프트에서 지연시간과 비용을 동시에 줄이는 실전 기법

> Source: [LLM Inference Optimization: vLLM vs TensorRT-LLM vs SGLang Decision Framework](https://www.spheron.network/blog/llm-inference-optimization-2026/)
