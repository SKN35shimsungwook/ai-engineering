# 에이전트는 일반 LLM 호출과 무엇이 다른가

- 일반 LLM 호출: 입력 한 번에 출력 한 번, 사람이 매 단계마다 다시 프롬프트를 넣어야 함
- 에이전트: 루프 안에서 스스로 도구를 호출하며 작업이 끝날 때까지 반복 수행
- Anthropic은 Workflow(사전 정의된 코드 경로로 LLM과 도구를 조율)와 Agent(LLM이 스스로 프로세스와 도구 사용을 동적으로 결정)를 구분
- 에이전트를 구성하는 핵심 요소: 계획(Planning), 메모리(Memory), 도구 사용(Tool use), 자율성(Autonomy)
- 에이전트 시스템의 기본 단위는 검색·도구·메모리 등으로 증강된 LLM

> Source: [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
