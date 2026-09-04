# 프로덕션 프롬프트/버전 관리

- 프롬프트를 코드처럼 다루어 버전 관리, 테스트, 자동화된 프로세스로 배포 — Git처럼 변경 이력을 추적
- 프롬프트 관리 시스템이 작성/버전관리/테스트를, 기존 CI/CD(GitHub Actions 등)가 배포 단계를 담당하고 둘을 통합 계층으로 연결
- 배포 전 자동 평가(LLM-as-judge 등)를 게이트로 걸어, 평가를 통과하지 못하면 새 프롬프트가 배포되지 않도록 함
- 점진적 롤아웃, 사용자 세그먼트별 A/B 테스트, 개발/스테이징/프로덕션 환경 분리를 지원
- Langfuse, LangSmith 등은 내장 플레이그라운드에서 프롬프트 버전을 비교하고 되돌릴 수 있는 기능을 제공

> Source: [CI/CD for LLM Prompts: How to Build a Prompt Deployment Pipeline](https://agenta.ai/blog/cicd-for-llm-prompts)
