# AI 에이전트 한눈에 정리

- 에이전트 = 계획 + 메모리 + 도구 사용을 갖추고 루프 안에서 스스로 판단하는 LLM 시스템
- ReAct 루프(사고-행동-관찰)가 대부분의 실전 에이전트 구현의 기본 골격
- 멀티 에이전트 오케스트레이션(LangGraph, CrewAI, Claude Agent SDK 등)으로 복잡한 워크플로를 분업 처리
- 코딩·고객지원·리서치 등 실전 사례가 빠르게 확산되는 동시에, 과도한 권한과 폭주 루프로 인한 실제 장애 사례도 늘고 있음
- SWE-bench, GAIA, τ-bench 등 벤치마크가 에이전트 신뢰성 평가의 표준으로 자리잡는 중
- 아래 영상은 에이전트의 정의와 도구 사용 개념을 간결하게 설명

> Source: [AI Agents, Clearly Explained](https://www.youtube.com/watch?v=FwOTs4UxQS4)
