# 프로덕션 RAG의 함정

- 대부분의 RAG 실패는 모델 품질이 아니라 데이터 레이어 설계 부족에서 비롯됨
- 리랭킹을 지연시간 절약을 위해 생략했더니 답변의 40%가 주제는 비슷하지만 무관한 청크를 인용
- 임베딩 모델 업그레이드보다 청킹 전략 개선(고정 512자 분할 → 시맨틱 청킹)이 답변 품질을 더 크게 향상
- 애플리케이션 레벨 접근 제어(access control) 필터링 버그는 가장 심각하고 발견하기 어려운 프로덕션 실패 유형 중 하나
- 사용자는 느린 응답은 참아도, 확신에 찬 오답에는 신뢰를 잃으며 이는 회복이 매우 어려움
- Docker, CircleCI, Reddit 등 100개 이상 기업 사례 분석 결과 대다수 RAG 프로젝트가 PoC 단계에서 좌초

> Source: [Six Lessons Learned Building RAG Systems in Production](https://towardsdatascience.com/six-lessons-learned-building-rag-systems-in-production/)
> Source: [RAG Best Practices: Lessons from 100+ Technical Teams](https://www.kapa.ai/blog/rag-best-practices)
> Source: [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/pdf/2401.05856)
