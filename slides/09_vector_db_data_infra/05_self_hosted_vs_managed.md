# 셀프호스팅 vs 매니지드, 무엇을 고를까

- 매니지드(Pinecone 등): 운영 부담이 거의 없고 빠르게 시작 가능, 대신 사용량 기반 비용이 규모가 커지면 부담
- 셀프호스팅(Milvus, Qdrant 등): 인프라·보안·업그레이드를 직접 책임지지만 대규모에서 비용 통제력이 큼
- 예시: 월 5천만 벡터 규모에서 Milvus 자체 호스팅은 인프라 비용 월 500~1,000달러 수준인 반면
  Pinecone은 동일 규모에서 약 3,500달러로 추정되는 사례가 보고됨
- 월 8천만~1억 쿼리를 넘는 고정 트래픽 구간부터 셀프호스팅이 비용상 유리해지는 경향
- 초기 단계·불확실한 트래픽에는 매니지드로 시작하고, 트래픽이 안정화되면 재검토하는 전략이 일반적

> Source: [When Self Hosting Vector Databases Becomes Cheaper Than SaaS](https://openmetal.io/resources/blog/when-self-hosting-vector-databases-becomes-cheaper-than-saas/)
