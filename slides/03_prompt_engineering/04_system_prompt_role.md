# 시스템 프롬프트와 역할 부여

- 시스템 프롬프트는 모델의 어조·행동 범위를 설정하는 별도 채널이며, 제공업체마다 우선순위와 처리 방식이 다름
- Claude는 시스템 파라미터가 실질적으로 특권을 가지며 사용자 턴보다 우선시되고, XML 유사 태그 구조를 신뢰성 있게 따름
- OpenAI 계열은 시스템 역할의 우선순위가 상대적으로 낮아 사용자 프롬프트로 재정의될 수 있어, 강제 규칙에는 별도의 개발자 메시지·응답 형식 제약을 함께 사용하는 것이 권장됨
- 역할 부여(role prompting)는 시스템 프롬프트 한 문장만으로도 효과가 있지만, 최신 모델은 정교해져 무거운 페르소나 설정보다 "원하는 관점을 명시적으로 요청"하는 편이 더 효과적
- 정적인 내용(시스템 지시, 예시, 도구 정의)을 프롬프트 앞쪽에 배치하고 가변적인 사용자 입력을 뒤에 두면 프롬프트 캐싱을 활용해 비용을 최대 90%, 지연시간을 최대 85%까지 줄일 수 있음

> Source: [Prompting best practices - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
