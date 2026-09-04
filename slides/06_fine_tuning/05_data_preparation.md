# 파인튜닝 데이터 준비: 품질이 양보다 중요하다

- 소량의 고품질 데이터가 대량의 노이즈 섞인 데이터보다 결과가 좋음 — 일관된 라벨링과 오류 없는 예시가 핵심
- OpenAI 가이드에 따르면 단 50~100개의 예시만으로도 유의미한 성능 개선이 가능한 경우가 있음
- 실제 사례: 수천 개의 정제된 예시가 5만 개의 기계 생성 예시보다 파인튜닝 성능이 더 좋았던 사례가 보고됨
- 과제 난이도에 따라 필요한 데이터량이 다름 — 분류/개체명 추출은 적은 데이터로 충분, 텍스트 생성/요약은 더 많은 데이터 필요
- 데이터셋은 학습용과 평가(테스트)용으로 분리하고, 실제 서비스 분포를 대표하도록 다양성을 확보해야 과적합을 방지

> Source: [Fine-tuning best practices](https://developers.openai.com/api/docs/guides/fine-tuning-best-practices)
> Source: [How to fine-tune: Focus on effective datasets](https://ai.meta.com/blog/how-to-fine-tune-llms-peft-dataset-curation/)
