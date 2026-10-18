# AI Engineering — 100+ Slide Deck

**🔗 바로 실행해 보기:** https://ai-engineering.streamlit.app

AI 엔지니어링을 한 번에 정리해 보고 싶어서 110장 분량의 슬라이드를 만들고, Streamlit 웹앱으로 넘겨 볼 수 있게 했습니다.
슬라이드는 Markdown 파일로 썼습니다. 근거 없는 내용이 섞이지 않도록 인용한 출처(147개, 그중 YouTube 13개)를 웹과 YouTube 검색으로 모아 CSV로 정리했고, SQLite DB에 넣어 앱 안에서 바로 찾아볼 수 있게 했습니다.

## 다루는 내용

01. AI 엔지니어링 기초 · 02. LLM 기초 · 03. 프롬프트 엔지니어링 · 04. RAG ·
05. AI 에이전트와 도구 사용 · 06. 파인튜닝과 모델 적응 · 07. 평가와 테스트 ·
08. LLMOps와 배포 · 09. 벡터 DB와 데이터 인프라 · 10. 보안·안전·책임 있는 AI ·
11. 비용과 성능 최적화 · 12. 멀티모달 AI · 13. 산업 사례 연구 ·
14. 커리어와 미래 전망 · 15. 결론과 참고자료

## 구조

```
ai-engineering/
├── app.py                  # Streamlit 앱 (슬라이드 뷰어 + 출처 DB 탐색기)
├── requirements.txt
├── slides/                 # 슬라이드 원본 (챕터별 디렉터리, 슬라이드 1개 = .md 파일 1개)
│   ├── 00_intro/
│   ├── 01_foundations/
│   ├── ...
│   └── 15_conclusion_references/
└── data/
    ├── sources_a.csv ...   # 배치별 리서치 원본 (챕터, 출처, URL, 유형, 핵심내용)
    ├── build_db.py         # sources_*.csv를 병합해 sources.csv + sources.db(SQLite) 생성
    ├── sources.csv          # 병합된 최종 CSV
    └── sources.db           # Streamlit 앱이 조회하는 SQLite DB
```

## 슬라이드 작성 규칙

슬라이드 하나 = Markdown 파일 하나. 형식:

```markdown
# 슬라이드 제목

- 핵심 bullet 1
- 핵심 bullet 2
- 핵심 bullet 3

> Source: [출처 제목](https://example.com)
```

`slides/<NN_챕터>/<NN_슬라이드>.md` 순서(디렉터리 정렬 → 파일명 정렬)대로 앱에서 이어서
렌더링됩니다.

## 데이터 파이프라인

1. 챕터별로 Google 웹 검색 / YouTube 검색으로 리서치
2. 슬라이드 Markdown 작성 + 출처를 `data/sources_<batch>.csv`에 기록
3. `python data/build_db.py` 로 모든 배치 CSV를 병합해 `sources.csv` + `sources.db` 생성
4. Streamlit 앱의 "출처 DB" 탭에서 챕터/유형/키워드로 필터링해 조회

## 실행 방법

```bash
pip install -r requirements.txt
python data/build_db.py
streamlit run app.py
```

## 기술 스택

- Python, Markdown (슬라이드 콘텐츠)
- Streamlit (웹 UI, 커스텀 슬라이드 페이저)
- Pandas + SQLite (CSV → DB 파이프라인)
