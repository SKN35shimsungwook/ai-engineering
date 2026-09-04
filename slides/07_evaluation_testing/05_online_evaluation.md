# 온라인 평가: A/B 테스트와 사용자 피드백

- 오프라인 평가는 배포 전 알려진 실패 유형을 잡아내고, 온라인 평가는 실제 트래픽에서 발생하는 새로운 실패와 분포 변화를 탐지
- A/B 테스트 시 대화형 기능은 요청 단위가 아닌 사용자 단위로 무작위 배정해야 세션 오염(이전 턴의 인상이 다음 턴 평가에 영향)을 방지
- 프로덕션에서는 지연시간, 토큰 비용, LLM-as-judge 품질 점수, 명시적 사용자 피드백(좋아요/싫어요)을 함께 추적
- 인간 피드백은 수집 속도는 느리지만 가장 신뢰할 수 있는 신호로, 소수 예시를 few-shot으로 축적해 자동 채점기를 지속적으로 교정
- 휴먼인더루프(human-in-the-loop)는 자동 평가와 실제 사용자 판단 사이의 간극을 좁히는 핵심 장치

> Source: [The Definitive Guide to A/B Testing LLM Models in Production](https://www.traceloop.com/blog/the-definitive-guide-to-a-b-testing-llm-models-in-production)
> Source: [How to Calibrate LLM-as-Judge with Human Corrections](https://www.langchain.com/resources/llm-as-a-judge)
