# 데이터 유출과 프라이버시 리스크

- 학습 데이터 기억(memorization): LLM이 학습 과정에서 이름, 이메일, 건강 정보 등 PII를 암기했다가
  추론 시점에 그대로 재생성할 수 있음
- RAG 데이터 유출: 검색된 문서에 담긴 민감 정보가 사용자의 질문 의도와 무관하게 답변에 노출될 수 있음
- 접근 제어 부재가 핵심 위험: 검색 계층이 사용자 권한과 무관하게 문서를 가져오면
  LLM이 의도치 않은 정보 유출 통로가 됨
- 완화 전략: 꼭 필요한 컨텍스트만 전달하고, 모델 입출력 전후로 PII를 자동 마스킹·토큰화
- 프롬프트에 실수로 포함된 고객 정보나 사내 기밀이 로그·캐시에 남는 것도 실무에서 흔한 리스크

> Source: [LLM Data Privacy: Safeguarding Data Privacy While Using LLMs](https://www.tonic.ai/guides/llm-data-privacy)
