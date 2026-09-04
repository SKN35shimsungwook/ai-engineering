# 흔한 함정과 안티패턴

- 모호한 지시: "AI가 알아서 잘 해주길" 기대하며 구체성이 부족한 프롬프트를 쓰면 모델이 임의로 가정을 채워 넣게 됨
- 지시 과적재(instruction stacking): 규칙을 추가할수록 이전 규칙에 대한 주의가 희석되며, 대략 8~10개 이상의 개별 지시부터 모델의 준수율이 눈에 띄게 떨어짐
- 예시 오염(example contamination): 현재 지시와 모순되는 오래된 예시가 남아있는 것이 프로덕션 프롬프트에서 가장 흔한 "조용한" 실패 원인
- 기법 과다 적용: "페르소나 추가", "퓨샷 예시 넣기", "CoT 시키기" 같은 정석 기법도 측정 없이 남용하면 오히려 안티패턴이 됨
- 하나의 프롬프트에 여러 작업 욱여넣기: 분류·추출·DB 업데이트·답장 작성을 한 번에 요청하면 각 하위 작업의 추론 품질이 함께 저하됨
- 모델의 한계 무시: RAG 등으로 명시적으로 연결하지 않는 한 LLM은 실시간 데이터나 사설 데이터베이스에 접근할 수 없음

> Source: [Prompt Engineering Anti-Patterns: 10 Mistakes to Avoid 2026](https://www.digitalapplied.com/blog/prompt-engineering-anti-patterns-10-mistakes-2026)
