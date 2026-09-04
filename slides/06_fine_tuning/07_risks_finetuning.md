# 파인튜닝의 리스크: 과적합, 재앙적 망각, 비용

- 재앙적 망각(Catastrophic Forgetting): 좁은 데이터셋으로 파인튜닝하면 새 태스크 성능은 오르지만 기존에 갖고 있던 범용 능력을 잃을 수 있음
- 모델 규모가 커질수록 재앙적 망각이 더 심해지는 경향이 있다는 연구 결과가 있음
- 과적합 위험: 소규모 데이터셋에 과도하게 맞추면 실제 배포 환경의 다양한 입력에 일반화되지 못함
- 비용 구조: PEFT(LoRA 등)는 전체 파인튜닝 대비 90% 이상의 성능을 훨씬 낮은 비용으로 달성(프로젝트 비용 약 2천~2만 달러 vs 풀파인튜닝 5만 달러 이상)
- 완화 기법으로 정규화 기반 방법, OSFT(직교 부분공간 파인튜닝), AWD(anchored weight decay) 등이 연구되고 있음

> Source: [How to Prevent Catastrophic Forgetting in LLM Fine-Tuning](https://www.cognizant.com/us/en/ai-lab/blog/overcoming-forgetting-in-llm-fine-tuning)
> Source: [OSFT explained: Prevent catastrophic forgetting in LLM fine-tuning](https://developers.redhat.com/articles/2026/07/28/osft-explained-prevent-catastrophic-forgetting-llm-fine-tuning)
