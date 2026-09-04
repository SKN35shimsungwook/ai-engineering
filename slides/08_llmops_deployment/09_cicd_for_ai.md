# AI 애플리케이션을 위한 CI/CD

- 프롬프트와 평가 세트를 코드처럼 버전 관리하고, 커밋마다 자동으로 회귀 평가를 실행하는 것이 핵심 아이디어
- Promptfoo, DeepEval 같은 오픈소스 도구를 GitHub Actions/GitLab CI에 연결해 "평가 실패 시 배포 중단" 게이트를 구현
- 보안 테스트(프롬프트 인젝션, 탈옥 시도, 데이터 유출 시나리오)도 CI/CD 파이프라인에 포함해 배포 전 자동으로 점검
- 배포 후에도 프로덕션 데이터로 주기적 품질 평가를 실행하고, 관측가능성 도구로 지연시간/비용/사용자 피드백을 지속 추적
- 품질 저하나 회귀가 감지되면 이전 프롬프트/모델 버전으로 즉시 롤백할 수 있는 절차를 CI/CD에 내장

> Source: [CI/CD Integration for LLM Eval and Security](https://www.promptfoo.dev/docs/integrations/ci-cd/)
> Source: [How Teams Integrate LLM Testing into Real CI/CD Pipelines](https://dzone.com/articles/llm-testing-cicd)
