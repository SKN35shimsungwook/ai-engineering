# 엔지니어를 위한 AI 정렬(Alignment) 기초

- 정렬이란 모델의 행동을 "도움이 되고, 정직하고, 해롭지 않게" 사람이 원하는 방향과 일치시키는 작업
- RLHF(인간 피드백 기반 강화학습): 사람이 여러 응답 중 더 나은 것을 선택하면,
  그 선호를 보상 모델이 학습하고 이를 기준으로 모델을 미세조정
- 실무적으로는 완벽한 규칙을 코딩하는 대신 "좋은 답변의 예시"를 통해 모델이 패턴을 학습하게 하는 접근
- 최근에는 RLHF 외에도 DPO(Direct Preference Optimization) 등 더 단순한 정렬 기법이 함께 쓰임
- 엔지니어 입장에서는 완벽한 정렬은 불가능하다는 전제하에, 가드레일·모니터링과 함께 계층적으로 안전을 설계해야 함

> Source: [What is AI Alignment Explained](https://www.youtube.com/watch?v=bqPwa6A5v4I)
> Source: [What is RLHF? Reinforcement learning from human feedback](https://wandb.ai/site/articles/what-is-rlhf/)
