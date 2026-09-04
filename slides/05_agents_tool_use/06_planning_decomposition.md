# 계획 수립과 작업 분해 전략

- Task decomposition(작업 분해): 복잡한 작업을 더 작고 다루기 쉬운 하위 목표로 쪼개는 것이 에이전트 계획의 핵심
- Chain-of-Thought: 몇 개의 예시나 간단한 지시로 LLM이 단계적으로 추론하도록 유도하는 기본 전략
- Tree of Thoughts: 각 단계에서 여러 추론 경로를 BFS/DFS로 탐색, 막다른 길에서 되돌아가는(backtrack) 것이 가능
- ADaPT(As-needed Decomposition and Planning): 실행 LLM이 직접 처리하지 못할 때만 하위 작업을 재귀적으로 분해 — 과제 난이도와 모델 역량에 동적으로 적응
- 분해 방식은 크게 "먼저 분해 후 계획(decomposition-first)"과 계획과 분해를 번갈아 수행하는 "interleaved" 방식으로 구분

> Source: [Understanding the planning of LLM agents: A survey](https://arxiv.org/pdf/2402.02716)
