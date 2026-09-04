# 태스크별 핵심 평가 지표

- RAG 시스템: RAGAS 프레임워크의 충실도(Faithfulness, 답변 내 주장 중 컨텍스트로 뒷받침되는 비율), 답변 관련성, 컨텍스트 정밀도/재현율
- 에이전트 시스템: 태스크 성공률(Task Success Rate), 도구 호출 정확도, 스텝/루프 수, 궤적(trajectory) 일치도, 비용과 지연시간
- 안전성: AgentHarm(11개 유해 카테고리에 대한 순응 여부), Agent-SafetyBench(8개 위험 범주, 2000개 테스트 케이스) 같은 전용 벤치마크 존재
- 중요한 함정: 상당수 에이전트 벤치마크가 주요 지표에서 안전 제약 위반에 불이익을 주지 않아, 성공률은 높지만 배포 불가능한 위험 행동을 놓칠 수 있음
- 지표는 하나만 보지 않고 품질/비용/지연/안전을 동시에 대시보드로 추적하는 것이 실무 표준

> Source: [Ragas vs DeepEval: Measuring Faithfulness and Response Relevancy in RAG Evaluation](https://medium.com/@sjha979/ragas-vs-deepeval-measuring-faithfulness-and-response-relevancy-in-rag-evaluation-2b3a9984bc77)
> Source: [Evaluation and Benchmarking of LLM Agents: A Survey](https://arxiv.org/html/2507.21504v1)
