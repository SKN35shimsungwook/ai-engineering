# Slack AI — 보안과 프라이버시를 지키며 RAG 구축

- 4대 원칙: 고객 데이터는 신뢰 경계를 벗어나지 않음 / 모델 학습에 미사용 / 사용자가 볼 수 있는 데이터만 접근 / 기존 보안·컴플라이언스 요건 유지
- 파인튜닝 대신 상태를 저장하지 않는(stateless) RAG 방식 채택 — 요청마다 컨텍스트를 담아 전달하고 아무것도 남기지 않음
- AWS와 협력해 폐쇄형 모델을 에스크로 VPC에 호스팅 — 모델 제공업체도 고객 데이터에 접근 불가
- 채널 요약, 검색 답변 등 대부분의 결과물은 디스크에 저장하지 않는 휘발성(ephemeral) 데이터로 처리
- 기존 접근 제어 목록(ACL)을 그대로 활용해 AI가 사용자 권한 밖의 정보를 노출하지 않도록 설계

> Source: [How we built Slack AI to be secure and private](https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/)
