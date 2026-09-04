# 프롬프트 인젝션이란

- 공격자가 악의적 지시를 입력에 심어 모델이 원래 지시를 무시하고 다른 행동을 하게 만드는 공격
- 직접 인젝션: 공격자가 채팅창 등에 직접 악성 지시를 입력하는 방식
- 간접 인젝션: 검색된 문서, 이메일, 웹페이지 등 모델이 나중에 읽는 콘텐츠에 지시를 숨기는 방식 —
  RAG·에이전트형 AI에서 특히 위험
- 실제 사례: 2025년 Microsoft 365 Copilot을 겨냥한 제로클릭 데이터 유출 공격 "EchoLeak"이 보안 연구진에 의해 공개됨
- 2025~2026년 GitHub Copilot(CVE-2025-53773), Cursor IDE(CVE-2025-54135) 등에서도
  간접 프롬프트 인젝션이 원격 코드 실행으로 이어진 사례가 보고됨

> Source: [EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit](https://arxiv.org/pdf/2509.10540)
> Source: [The Comprehensive Guide to Prompt Injection Attacks in 2026](https://www.sysdig.com/learn-cloud-native/prompt-injection)
