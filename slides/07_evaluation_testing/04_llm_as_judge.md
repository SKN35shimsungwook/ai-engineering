# LLM-as-Judge: 또 다른 LLM으로 평가하기

- LLM-as-judge는 더 강력한 LLM을 이용해 다른 모델(또는 같은 모델)의 출력을 채점하는 기법 — 사람 평가 대비 속도와 비용에서 유리
- 작동 방식: 평가 기준(rubric)을 프롬프트에 명시하고, 판정 LLM이 점수 또는 합격/불합격을 반환
- 대표적 함정: 위치 편향(먼저 제시된 답을 선호), 장황함 편향(긴 답을 더 좋다고 평가), 자기선호 편향(자신과 비슷한 스타일 선호)
- 프롬프트 인젝션 등 적대적 조작에 취약할 수 있어 고위험 상황에서는 신뢰도에 한계가 있음
- 완화책: 세부적인 평가 기준 제공, 사람 채점과의 정기적 캘리브레이션(교정), 여러 판정 모델의 앙상블 사용

> Source: [LLM-as-a-Judge: Why Frontier Models Fail 50%+ Bias Tests](https://www.adaline.ai/blog/llm-as-a-judge-reliability-bias)
> Source: [LLM-as-a-Judge Explained Simply | Evaluate AI Models Like a Pro](https://www.youtube.com/watch?v=T01FT3_T0n0)
