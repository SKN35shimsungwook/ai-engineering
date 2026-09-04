# 도구/함수 호출(Tool/Function Calling)의 메커니즘

- LLM이 자연어 대신 구조화된 JSON을 출력해 외부 시스템에 특정 작업을 지시하는 방식
- 모델은 등록된 도구 스키마(이름, 설명, 파라미터)를 보고 어떤 도구를 언제 호출할지 스스로 판단
- 호출 결과(함수 반환값)는 다시 컨텍스트로 들어가 다음 응답 생성에 활용됨
- 정적 벡터 DB 검색으로는 못하는 일 — 이메일 발송, DB 갱신, 실시간 주가 조회 등 실제 행동을 가능하게 함
- 도구 설명이 모호하거나 파라미터 설계가 나쁘면 잘못된 호출로 이어지므로, 도구 자체를 명확하게 설계하는 것이 중요
- 병렬 함수 호출(parallel function calling)을 지원하는 모델이 늘며 여러 도구를 동시에 실행해 지연시간을 줄임

> Source: [Tool Calling Explained: The Core of AI Agents (2026 Guide)](https://composio.dev/content/ai-agent-tool-calling-guide)
> Source: [Writing effective tools for AI agents—using AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
