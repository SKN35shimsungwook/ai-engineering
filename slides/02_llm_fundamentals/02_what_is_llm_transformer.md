# LLM과 트랜스포머 아키텍처

- 대규모 언어 모델은 입력 텍스트 다음에 올 텍스트의 확률 분포를 예측하도록 학습된 신경망
- 오늘날 사용되는 거의 모든 모델(GPT, Claude, Gemini, Llama, Mistral, DeepSeek 등)이 2017년 등장한 트랜스포머(Transformer) 구조를 기반으로 함
- 트랜스포머는 순차 처리(RNN)를 완전히 배제하고, 셀프 어텐션(self-attention)만으로 입력 전체의 관계를 한 번에 파악
- 어텐션은 각 토큰이 Query·Key·Value 벡터를 통해 다른 모든 토큰과의 연관도를 계산하고, softmax로 정규화한 가중합으로 문맥을 반영한 표현을 생성
- 어텐션 연산량은 문장 길이에 따라 제곱으로 증가하는 것이 근본적 한계이며, FlashAttention·RoPE 등의 기법으로 이를 완화

> Source: [Large Language Models explained briefly - 3Blue1Brown (YouTube)](https://www.youtube.com/watch?v=LPZh9BOjkQs)
> Source: [Transformer Architecture in 2026: From Attention to Mixture of Experts (DEV Community)](https://dev.to/jintukumardas/transformer-architecture-in-2026-from-attention-to-mixture-of-experts-moe-3d46)
