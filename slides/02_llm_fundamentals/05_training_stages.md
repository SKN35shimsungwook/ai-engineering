# 학습 단계: 사전학습 → SFT → RLHF

- 사전학습(Pretraining): 방대한 텍스트 코퍼스에서 다음 토큰을 예측하도록 자기지도학습(self-supervised)하며 언어 구조와 세계 지식의 토대를 형성
- 지도 미세조정(SFT, Supervised Fine-Tuning): 사람이 작성한 (프롬프트, 응답) 쌍 데이터셋으로 지도학습을 수행해 지시를 따르는 형태의 응답을 생성하도록 조정
- 인간 피드백 기반 강화학습(RLHF): 사람이 매긴 응답 쌍의 선호 순위로 보상 모델을 학습시키고, 이를 극대화하도록 정책을 최적화(PPO 등)해 응답을 인간 선호에 더 가깝게 정렬
- SFT만으로는 지시를 "따르게" 할 수는 있어도 사람이 선호하는 방식으로 정렬하기엔 한계가 있어 RLHF(혹은 DPO 등 대안 기법)가 추가로 필요
- 세 단계는 순차적이지만 실무에서는 사전학습 이후 단계를 반복적으로 재수행하며 모델을 지속적으로 개선

> Source: [LLM Training: RLHF and Its Alternatives - Ahead of AI (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives)
