# LLM 애플리케이션 평가가 어려운 이유

- 같은 입력에도 매번 다른 출력이 나오는 비결정성(non-determinism) — 전통적인 단위 테스트의 "정답과 일치" 방식이 통하지 않음
- 출력이 개방형(open-ended)이라 정답이 하나가 아니라 여러 개의 올바른 답이 존재할 수 있음
- 정확도뿐 아니라 사실성(faithfulness), 어조, 안전성, 형식 준수 등 다차원적 품질을 동시에 평가해야 함
- 에이전트형 시스템은 최종 결과뿐 아니라 추론 경로(trajectory)와 도구 호출까지 평가 대상이 되어 복잡도가 커짐
- Anthropic은 pass@k(1회 이상 성공 확률)와 pass^k(k회 모두 성공할 확률) 같은 지표로 비결정성을 정량화할 것을 권장 — 75% 단일 성공률도 3회 연속 성공 확률은 약 42%에 불과

> Source: [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
