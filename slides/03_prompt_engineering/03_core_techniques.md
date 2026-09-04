# 핵심 기법: 제로샷 · 퓨샷 · CoT

- 제로샷(Zero-shot) 프롬프팅: 예시 없이 지시만으로 곧바로 원하는 작업을 요청하는 가장 단순한 형태
- 퓨샷(Few-shot / multishot) 프롬프팅: 몇 개의 입출력 예시를 함께 제공해 원하는 형식·톤·구조를 모델이 패턴으로 학습하게 함 — Anthropic은 3~5개 예시를 권장하며 예시는 관련성과 다양성을 갖춰야 함
- 연쇄적 사고(Chain-of-Thought, CoT): 모델이 최종 답을 내기 전에 단계별 추론 과정을 거치도록 유도해 수학·논리 문제 등에서 정확도를 크게 높이는 기법
- CoT는 종종 퓨샷과 결합되어 "예시 안에서 추론 과정까지 보여주는" 방식으로 쓰이며 효과가 배가됨
- 다만 추론 특화 모델은 이미 내부적으로 사고 과정을 거치므로 명시적 CoT 지시가 오히려 불필요하거나 역효과를 낼 수 있어, 모델 특성에 맞춰 기법을 선택해야 함

> Source: [Prompting best practices - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
> Source: [Master AI Prompting: Zero-Shot, Few-Shot & Chain of Thought Explained (YouTube)](https://www.youtube.com/watch?v=sZIV7em3JA8)
