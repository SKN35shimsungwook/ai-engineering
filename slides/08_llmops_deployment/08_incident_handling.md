# 장애와 실패 대응: 실제 사례

- Air Canada 사례: 챗봇이 사별 운임(bereavement fare) 정책을 잘못 안내(환각)해 고객이 소송을 제기, 캐나다 소액 사건 재판소는 항공사에 환불과 비용 지급을 명령
- 법원은 "챗봇도 웹사이트의 일부이므로 회사가 그 정보에 책임이 있다"는 항공사의 면책 주장을 기각 — AI 출력에 대한 법적 책임 소재의 중요한 선례
- 원인 분석: 챗봇이 학습된 내용과 항공사의 실제 공식 정책 문서 사이의 불일치가 근본 원인으로 지목됨
- 실전 대응 체계: 관측가능성으로 이상 응답을 조기 탐지, 온라인 평가로 회귀를 감지, 문제 프롬프트/모델 버전을 즉시 롤백할 수 있는 배포 파이프라인 필요
- 고위험 도메인(법률, 의료, 금액 관련 안내)에서는 확인 문구, 사람 검토 단계, 출처 인용 강제 등 가드레일을 추가하는 것이 표준

> Source: [Air Canada Held Responsible for Chatbot's Hallucinations](https://aibusiness.com/nlp/air-canada-held-responsible-for-chatbot-s-hallucinations-)
> Source: [What Air Canada Lost In 'Remarkable' Lying AI Chatbot Case](https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/)
