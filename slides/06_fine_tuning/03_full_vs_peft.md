# 전체 파인튜닝 vs 효율적 파인튜닝(LoRA/QLoRA)

- 전체 파인튜닝(Full Fine-tuning)은 모델의 모든 가중치를 업데이트 — 성능은 최상이지만 GPU 메모리와 비용 부담이 큼
- LoRA(Low-Rank Adaptation)는 원래 가중치는 고정하고 저랭크(low-rank) 행렬 어댑터만 학습해 학습 파라미터를 전체의 1% 미만으로 줄임
- 실제 사례: OpenLLaMA-3B 모델에서 어텐션 블록만 타겟팅 시 학습 파라미터가 전체의 0.08%까지 감소
- QLoRA는 기반 모델을 4비트로 양자화한 상태에서 LoRA 어댑터만 고정밀로 학습 — 단일 48GB GPU로 65B 모델 파인튜닝 가능
- 어댑터 파일은 수 메가바이트에 불과해 여러 태스크별 어댑터를 하나의 기반 모델에 유연하게 교체 장착 가능

> Source: [Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for LLMs](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms)
> Source: [What is LoRA? Low-Rank Adaptation for finetuning LLMs EXPLAINED](https://www.youtube.com/watch?v=KEv-F5UkhxU)
