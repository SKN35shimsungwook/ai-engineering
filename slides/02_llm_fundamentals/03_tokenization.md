# 토큰화(Tokenization)

- 토큰은 LLM이 처리하는 텍스트의 최소 단위이며, 단어 전체가 아니라 부분 단어(subword) 단위로 쪼개지는 경우가 많음
- 대부분의 모델(GPT, Llama, Mistral 등)은 바이트 페어 인코딩(BPE)을 사용해 자주 등장하는 문자열 쌍을 반복적으로 병합하는 방식으로 토크나이저를 구성
- API 요금은 토큰 단위로 부과되며, 입력·출력 토큰 가격이 다르게 책정됨 — 출력 토큰이 입력 토큰보다 2~4배 비싼 것이 일반적
- 같은 의미라도 토큰 수가 다르면 비용·응답 속도·컨텍스트 소비량이 달라지므로 프롬프트를 간결하게 쓰는 것이 실질적 최적화
- 영어 중심으로 학습된 BPE 토크나이저 특성상 비영어권 언어(예: 중국어)는 같은 의미를 표현하는 데 약 2배 많은 토큰이 필요할 수 있음

> Source: [Let's build the GPT Tokenizer - Andrej Karpathy (YouTube)](https://www.youtube.com/watch?v=zduSFxRajkE)
> Source: [LLM Tokenization Explained: English vs Other Languages Cost Difference](https://promptcost.org/en/blog/llm-tokenization-explained/)
