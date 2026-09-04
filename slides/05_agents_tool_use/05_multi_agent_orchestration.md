# 멀티 에이전트 시스템과 오케스트레이션

- 2026년 기준 6대 주요 프레임워크: LangGraph, Claude Agent SDK, OpenAI Agents SDK, AWS Strands Agents, CrewAI, AG2(구 AutoGen)
- LangGraph: 방향성 그래프와 조건부 엣지 기반, 감사·결정론적 제어가 중요한 규제 산업의 프로덕션 멀티 에이전트에 강점
- CrewAI: 역할 기반(role-based) 크루 구조로 아이디어에서 프로토타입까지 가장 빠르게 도달, Fortune 500의 60%가 사용
- Claude Agent SDK: Claude Code를 구동하는 하부 프레임워크를 그대로 노출, 서브에이전트 체인과 컴퓨터 조작이 필요한 안전 중시 영역에 적합
- AutoGen/Semantic Kernel은 유지보수 모드로 전환되어 신규 프로젝트의 기반으로는 권장되지 않음
- 6개 프레임워크 모두 도구 상호운용을 위한 MCP(Model Context Protocol)를 지원하는 방향으로 수렴

> Source: [LangGraph vs CrewAI vs Claude Agent SDK: Comparing the Best Agent Orchestration Framework in 2026](https://appinventiv.com/blog/multi-agent-frameworks/)
