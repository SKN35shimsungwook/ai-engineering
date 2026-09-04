# 지시어 튜닝 vs 선호도 튜닝(RLHF/DPO)

- 지시어 튜닝(Instruction Tuning)은 (지시-응답) 쌍으로 지도학습(SFT)하여 모델이 사용자 요청을 따르도록 학습
- RLHF(인간 피드백 강화학습)는 별도의 보상 모델을 학습한 뒤, 이를 이용해 정책 모델을 강화학습(PPO 등)으로 최적화
- RLHF는 보상 모델 학습과 RL 최적화라는 두 단계가 필요해 하이퍼파라미터에 민감하고 불안정해지기 쉬움
- DPO(Direct Preference Optimization)는 보상 모델과 RL 단계를 생략하고 선호/비선호 응답 쌍으로 모델을 직접 최적화 — SFT처럼 안정적으로 학습 가능
- 다만 최근 연구는 DPO가 오프라인 데이터에 제한되어 특정 상황에서 보상 기반 RLHF보다 정렬 품질이 낮을 수 있음을 지적

> Source: [How is RLHF different from DPO at a high level?](https://sebastianraschka.com/faq/docs/rlhf-vs-dpo.html)
> Source: [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/pdf/2305.18290)
