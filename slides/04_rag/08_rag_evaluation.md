# RAG 평가: 무엇을 어떻게 측정하나

- Faithfulness(충실도): 생성된 답변의 주장이 검색된 컨텍스트로부터 실제로 추론 가능한가
- Context Precision/Recall: 검색된 청크가 질의와 관련 있는지, 필요한 정보를 빠짐없이 담았는지
- Answer Relevance(답변 관련성): 생성된 답변이 실제 질문에 부합하는지
- RAGAS(Retrieval-Augmented Generation Assessment) 프레임워크가 가장 널리 쓰이는 오픈소스 평가 도구
- DeepEval, TruLens, ARES 등도 동일한 4대 지표(충실도·답변 관련성·컨텍스트 정밀도/재현율)를 구현
- 표준 평가지표는 "검색 인덱스 자체가 신뢰할 수 있다"고 가정하는 한계가 있어, 데이터 신선도·출처 등 신뢰성 검증이 다섯 번째 평가축으로 논의됨

> Source: [Metrics | Ragas](https://docs.ragas.io/en/v0.1.21/concepts/metrics/)
> Source: [RAG Evaluation Metrics in 2026: Faithfulness & More](https://futureagi.com/blog/rag-evaluation-metrics-2025/)
