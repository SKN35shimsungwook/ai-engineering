# 콘텐츠 모더레이션과 가드레일 기법

- Llama Guard(Meta): Llama 모델을 파인튜닝한 안전 분류기로, 입출력을 "안전/불안전"으로 판별 —
  Llama Guard 3는 다국어 지원까지 확장
- NVIDIA NeMo Guardrails: 입력·대화흐름·검색결과·도구호출·출력 5단계에 각각 규칙(rail)을 적용하는
  오픈소스(Apache 2.0) 프레임워크
- 그 외 Guardrails AI, Azure Prompt Shields, OpenAI Moderation API, Lakera Guard 등이
  현재 널리 쓰이는 상용/오픈소스 가드레일 도구
- 가드레일은 입력 필터링뿐 아니라 출력 검증, RAG 검색 결과 필터링까지 다층적으로 적용하는 것이 트렌드

> Source: [Essential Guide to LLM Guardrails: Llama Guard, NeMo](https://medium.com/data-science-collective/essential-guide-to-llm-guardrails-llama-guard-nemo-d16ebb7cbe82)
> Source: [NeMo Guardrails 2026: NVIDIA's LLM Safety Toolkit](https://appsecsanta.com/nemo-guardrails)
