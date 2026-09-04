# 실전 활용 사례

- 코딩 에이전트: Claude Code(개발자 곁에서 실행되는 터미널 기반 에이전트)와 Devin(Cognition AI, 클라우드 위임형 플랫폼)이 2026년 대표 사례
- 실무에서는 판단이 많이 필요한 복잡한 작업은 Claude Code로 직접 운전하고, 정형화된 티켓 처리는 Devin에 위임하는 조합이 흔함
- 고객지원 에이전트: 티켓 이해 → 도구 호출로 실제 컨텍스트(주문, 과거 문의, 문서) 조회 → 답변 작성/라우팅/환불 실행 → 확신 없으면 사람에게 에스컬레이션하는 루프로 구성
- 리서치 에이전트: 웹 검색, 코드 인터프리터, 문서 분석 도구를 조합해 다단계 추론이 필요한 실제 업무형 질문에 대응 (GAIA 벤치마크가 이 유형을 평가)
- 에이전트 SDK를 활용해 지원 티켓 도구, RAG 연동, 평가 하네스의 초기 골격을 코딩 에이전트 스스로 생성하는 워크플로도 확산 중

> Source: [Devin vs Claude Code: Which Ships Your Backlog?](https://snowmanlabs.com/insights/devin-vs-claude-code)
> Source: [How to Build an AI Customer Support Agent with Claude (2026)](https://www.getmacha.com/blog/build-ai-customer-support-agent-with-claude)
