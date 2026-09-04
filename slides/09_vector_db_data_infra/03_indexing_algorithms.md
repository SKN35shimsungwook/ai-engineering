# 인덱싱 알고리즘: HNSW와 IVF

- 벡터가 많아지면 전수 비교(brute-force)는 느려서, 근사 검색 인덱스가 필수
- HNSW(계층적 탐색 가능 소규모 세계): 벡터를 다층 그래프로 연결해 상위 레이어에서 대략적으로,
  하위 레이어로 갈수록 정밀하게 탐색 — 재현율이 높고 삽입이 유연하지만 메모리 사용량이 큼
- IVF(역파일 인덱스): K-평균으로 벡터를 클러스터링한 뒤 질의와 가까운 클러스터만 탐색 —
  메모리 효율이 좋지만 고차원에서 정확도가 상대적으로 떨어짐
- 실무에서는 HNSW가 기본값으로 널리 쓰이고, IVF(+PQ 양자화)는 초대규모·저메모리 환경에서 선택
- 두 방식 모두 "정확도 vs 속도 vs 메모리"의 트레이드오프를 파라미터로 조절

> Source: [Vector Database Indexing Methods: IVF, HNSW, and Product Quantization](https://medium.com/@kiranvutukuri/95-vector-database-indexing-methods-ivf-hnsw-and-product-quantization-c4a6243929db)
> Source: [HNSW vs IVFFlat: How to Choose the Right Vector Index](https://bigdataboutique.com/blog/hnsw-vs-ivfflat-how-to-choose-the-right-vector-index)
