# 멀티모달 RAG/앱 만들기

- 기존 OCR 기반 RAG의 한계: 표, 도면, 차트가 섞인 문서에서 정보가 손실되거나 왜곡됨
- ColPali 같은 문서 검색 모델은 OCR 없이 문서 이미지를 직접 임베딩해 검색
- 검색된 문서 이미지를 VLM(예: Qwen2-VL)에 전달해 답변 생성 — 레이아웃과 시각 정보를 그대로 보존
- 실무에서는 OCR 텍스트 채널 + 시각 의미 설명 채널을 함께 쓰는 하이브리드 구조도 널리 사용
- 좋은 텍스트 설명만 있으면 복잡한 멀티모달 임베딩 없이 표준 텍스트 검색으로도 이미지 검색 가능

> Source: [Multimodal RAG with Document Retrieval (ColPali) and VLMs](https://huggingface.co/learn/cookbook/en/multimodal_rag_using_document_retrieval_and_vlms)
> Source: [Beyond OCR: Building a Truly Multimodal Local RAG Pipeline](https://dev.to/pleymor/beyond-ocr-building-a-truly-multimodal-local-rag-pipeline-2hkd)
