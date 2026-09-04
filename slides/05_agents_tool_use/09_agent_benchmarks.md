# 에이전트 벤치마크의 현재 상황

- SWE-bench(Verified): 실제 GitHub 이슈 2,294건에 대해 실행 기반 테스트로 코드 수정 능력을 평가
- GAIA: 웹 브라우저·코드 인터프리터·문서 분석 등 도구 사용과 다단계 추론이 필요한 실제 업무형 질문 466개로 구성, 사람과 AI 간 77%의 성능 격차를 보임
- τ-bench(Tau-bench, Princeton·Sierra): 소매·항공 도메인에서 정책 준수를 요구하는 멀티턴 사용자 상호작용을 평가하며 pass@k로 신뢰성 문제를 드러냄
- 2026년에는 주요 LLM 랩들이 SWE-bench와 GAIA 점수를 경쟁적으로 공개하며 에이전트 역량의 표준 지표로 자리잡음
- 단일 정확도 지표를 넘어 안전성, 비용 효율, 정책 준수 등을 함께 보는 다차원 평가 프레임워크 논의가 확산 중

> Source: [AI Agent Benchmarking Infrastructure on GPU Cloud: Run SWE-bench, GAIA, Terminal-Bench, and OSWorld at Scale (2026 Guide)](https://www.spheron.network/blog/ai-agent-benchmarking-gpu-cloud-swebench-gaia/)
> Source: [Tau Bench: The 2026 Enterprise Evaluation Guide](https://www.automationanywhere.com/company/blog/product-insights/ai-agent-benchmark)
