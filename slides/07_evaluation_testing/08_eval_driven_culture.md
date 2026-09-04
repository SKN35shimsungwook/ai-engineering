# 평가 중심 개발(Eval-Driven Development) 문화 만들기

- 평가 중심 개발은 LLM 애플리케이션을 "평가를 먼저 만들고" 그 위에 구축하는 개발 방식 — 코드 테스트 주도 개발(TDD)의 LLM 버전
- OpenAI는 "일찍, 자주" 평가하고 개발 단계마다 범위를 좁힌 테스트를 작성할 것을 권장
- 실제 사례: Descript는 "고장내지 않기, 요청한 대로 하기, 잘 하기"라는 세 축으로 평가를 설계하고, 수동 채점에서 LLM 채점기로 진화시키며 주기적으로 사람이 재보정
- 실제 사례: Bolt AI는 이미 널리 쓰이는 에이전트를 만든 뒤 3개월 만에 정적 분석, 브라우저 에이전트 테스트, LLM 판정을 결합한 평가 시스템을 구축
- 평가는 배포 후에도 가치가 커짐 — 모델 업그레이드 속도, 회귀 감지, 제품팀과 연구팀 간 소통 채널 역할

> Source: [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
> Source: [Eval Driven Development: What it is, how to do it right, and real examples to learn from](https://deepeval.com/blog/eval-driven-development)
