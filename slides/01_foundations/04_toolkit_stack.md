# AI 엔지니어의 도구·기술 스택

- LLM API: OpenAI, Anthropic, Google 등 파운데이션 모델 제공업체의 API가 기본 재료
- 오케스트레이션 프레임워크: LangChain·LangGraph가 가장 널리 쓰이며, LangGraph는 상태를 가진 그래프 실행으로 멀티 에이전트 조율을 지원 (2025년 10월 v1.0 출시, Uber·JPMorgan·LinkedIn 등에서 실사용)
- 벡터 데이터베이스: Pinecone, pgvector, Weaviate, Qdrant, Chroma 등이 임베딩 저장·검색을 담당하며 RAG의 핵심 인프라
- 표준 프로토콜: Anthropic이 제안한 MCP(Model Context Protocol)가 에이전트와 외부 도구·데이터를 연결하는 표준으로 자리잡음
- 그 외 CrewAI(역할 기반 멀티 에이전트), AutoGen(대화형 멀티 에이전트) 등 특화 프레임워크도 함께 사용됨

> Source: [The AI Agents Stack (2026 Edition) - O'Reilly Radar](https://www.oreilly.com/radar/the-ai-agents-stack-2026-edition/)
> Source: [The best AI agent frameworks in 2026 - LangChain](https://www.langchain.com/resources/ai-agent-frameworks)
