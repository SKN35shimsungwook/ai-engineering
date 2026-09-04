# 구조화된 출력: JSON 모드와 함수/도구 호출

- JSON 모드: API 요청 시 파라미터 하나로 항상 유효한 JSON 객체를 반환하도록 강제하는 가장 단순한 방식이지만, 제공업체에 따라 스키마를 강제하지 못해 예상 밖 구조가 나올 수 있음
- 함수 호출(Function Calling / Tool Use): 모델에게 함수 정의를 제공하면 실제로 함수를 실행하는 대신 "이 함수를 이렇게 호출해야 한다"는 JSON 형태의 지시를 반환
- 구조화된 출력(Structured Outputs): JSON 모드의 발전형으로, 실제 JSON 스키마를 전달하면 제약 디코딩(constrained decoding)을 통해 필드명·타입·필수 항목까지 스키마를 100% 준수하도록 보장
- 세 방식 모두 "모델의 자유 텍스트 출력을 신뢰할 수 있는 데이터로 변환"한다는 같은 목적을 가지지만 보장 수준이 다르므로 활용 사례에 맞게 선택해야 함
- 에이전트 시스템에서는 도구 호출이 외부 API·데이터베이스와 LLM을 연결하는 핵심 메커니즘으로 사용됨

> Source: [Structured Outputs with LLMs: JSON Mode, Function Calling, and When to Use Each](https://towardsdatascience.com/structured-outputs-with-llms-json-mode-function-calling-and-when-to-use-each/)
> Source: [How LLM Tool Calling Works (YouTube)](https://www.youtube.com/watch?v=QiRdYCNXAxk)
