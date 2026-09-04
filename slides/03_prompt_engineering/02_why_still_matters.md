# 프롬프트 엔지니어링이 여전히 중요한 이유

- 모델이 아무리 발전해도 "무엇을, 어떻게 요청하는가"가 출력 품질을 좌우하는 가장 값싼 레버로 남아있음
- 파인튜닝이나 재학습 없이 즉시 반복(iterate)할 수 있어 비용 대비 효과가 가장 큰 모델 적응 기법
- Anthropic 공식 가이드: 명확하고 직접적인 지시가 결과 품질을 가장 크게 좌우하며, "맥락이 부족한 신입 동료에게 시키듯" 프롬프트를 검토하라고 권장
- 단순 "프롬프트 작성 기술"에서 스키마 설계, 평가(eval) 체계, 버전 관리를 포함하는 엔지니어링 규율로 성격이 바뀌는 중
- 모델·제공업체마다 시스템 프롬프트를 처리하는 방식이 달라 하나의 프롬프트를 모든 모델에 그대로 재사용하는 것이 2026년 현재도 가장 흔한 실패 원인 중 하나

> Source: [Prompting best practices - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
> Source: [Prompt engineering best practices for 2026 - Claude by Anthropic](https://claude.com/blog/best-practices-for-prompt-engineering)
