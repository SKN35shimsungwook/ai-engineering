# ReAct 패턴: Reason → Act → Observe

- ReAct(Reasoning + Acting)는 추론과 행동을 같은 루프 안에서 번갈아 수행하는 패턴
- Thought(사고): 현재 상태를 해석하고 다음에 무엇을 할지 판단하는 명시적 추론 단계
- Action(행동): 판단에 따라 실제 도구를 호출
- Observation(관찰): 도구 실행 결과를 받아 컨텍스트에 반영, 다음 추론의 근거로 사용
- 처음부터 전체 계획을 세우는 방식과 달리, 매 행동 후 관찰로 검증하기 때문에 잘못된 가정이 다음 단계로 누적되지 않음
- 추론 과정이 log로 남아 에이전트의 판단 근거를 추적(해석 가능성)할 수 있다는 장점

> Source: [ReAct Agent Loop: How Reason-and-Act Agents Actually Work](https://futureagi.com/blog/loop-engineering/react-agent-loop/)
