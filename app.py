"""AI Engineering — a ~100-slide Streamlit deck rendered from Markdown files.

Each slide lives as one .md file under slides/<NN_chapter>/<NN_slide>.md.
This app walks that directory tree to build the slide order, renders each
slide as a card, and provides a second "source DB" tab backed by the
SQLite database built by data/build_db.py from the researched sources.
"""

from __future__ import annotations

import os
import re
import sqlite3
from dataclasses import dataclass

import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SLIDES_DIR = os.path.join(BASE_DIR, "slides")
DB_PATH = os.path.join(BASE_DIR, "data", "sources.db")
CSV_PATH = os.path.join(BASE_DIR, "data", "sources.csv")

st.set_page_config(page_title="AI 엔지니어링", page_icon="🧠", layout="wide")


@dataclass
class Slide:
    chapter_dir: str
    chapter_title: str
    file_name: str
    path: str
    title: str
    bullets: list[str]
    sources: list[tuple[str, str]]


def chapter_title_from_dir(dir_name: str) -> str:
    # "02_llm_fundamentals" -> "02. Llm Fundamentals"
    num, _, slug = dir_name.partition("_")
    words = slug.replace("_", " ").title()
    return f"{num}. {words}"


def parse_slide(path: str, chapter_dir: str) -> Slide:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else os.path.basename(path)

    bullets = re.findall(r"^-\s+(.+)$", text, re.MULTILINE)

    sources = []
    for line in re.findall(r"^>\s*Source:\s*(.+)$", text, re.MULTILINE):
        link_match = re.match(r"\[(.+?)\]\((.+?)\)", line.strip())
        if link_match:
            sources.append((link_match.group(1), link_match.group(2)))
        else:
            sources.append((line.strip(), ""))

    return Slide(
        chapter_dir=chapter_dir,
        chapter_title=chapter_title_from_dir(chapter_dir),
        file_name=os.path.basename(path),
        path=path,
        title=title,
        bullets=bullets,
        sources=sources,
    )


@st.cache_data(show_spinner=False)
def load_slides(mtime_key: float) -> list[Slide]:
    slides: list[Slide] = []
    if not os.path.isdir(SLIDES_DIR):
        return slides
    for chapter_dir in sorted(os.listdir(SLIDES_DIR)):
        chapter_path = os.path.join(SLIDES_DIR, chapter_dir)
        if not os.path.isdir(chapter_path):
            continue
        for file_name in sorted(os.listdir(chapter_path)):
            if file_name.endswith(".md"):
                slides.append(parse_slide(os.path.join(chapter_path, file_name), chapter_dir))
    return slides


def slides_mtime_key() -> float:
    latest = 0.0
    for root, _dirs, files in os.walk(SLIDES_DIR):
        for f in files:
            latest = max(latest, os.path.getmtime(os.path.join(root, f)))
    return latest


@st.cache_data(show_spinner=False)
def load_sources_df(mtime_key: float) -> pd.DataFrame:
    if os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            return pd.read_sql("SELECT * FROM sources", conn)
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame(
        columns=[
            "id",
            "chapter_num",
            "chapter_name",
            "slide_file",
            "source_title",
            "source_url",
            "source_type",
            "key_point",
        ]
    )


def render_slide_view(slides: list[Slide]) -> None:
    total = len(slides)
    if total == 0:
        st.warning("slides/ 아래에 슬라이드(.md) 파일이 없습니다.")
        return

    if "idx" not in st.session_state:
        st.session_state.idx = 0
    st.session_state.idx = max(0, min(st.session_state.idx, total - 1))

    current_slide_chapter = slides[st.session_state.idx].chapter_dir

    with st.sidebar:
        st.markdown("### 목차")
        chapters: dict[str, list[tuple[int, Slide]]] = {}
        for i, s in enumerate(slides):
            chapters.setdefault(s.chapter_dir, []).append((i, s))

        for chapter_dir, items in chapters.items():
            chapter_title = items[0][1].chapter_title
            with st.expander(chapter_title, expanded=(chapter_dir == current_slide_chapter)):
                for i, s in items:
                    label = f"{'➤ ' if i == st.session_state.idx else ''}{s.title}"
                    if st.button(label, key=f"nav_{i}", use_container_width=True):
                        st.session_state.idx = i

    slide = slides[st.session_state.idx]

    col_prev, col_mid, col_next = st.columns([1, 6, 1])
    with col_prev:
        if st.button("◀ 이전", disabled=st.session_state.idx == 0, use_container_width=True):
            st.session_state.idx -= 1
            st.rerun()
    with col_mid:
        st.progress((st.session_state.idx + 1) / total)
        st.caption(
            f"{slide.chapter_title}  ·  슬라이드 {st.session_state.idx + 1} / {total}"
        )
    with col_next:
        if st.button("다음 ▶", disabled=st.session_state.idx == total - 1, use_container_width=True):
            st.session_state.idx += 1
            st.rerun()

    st.markdown(
        """
        <style>
        .slide-card {
            background: var(--secondary-background-color);
            border-radius: 16px;
            padding: 2.5rem 3rem;
            margin-top: 1rem;
            min-height: 420px;
        }
        .slide-card h1 { font-size: 2.1rem; margin-bottom: 1.5rem; }
        .slide-card ul { font-size: 1.25rem; line-height: 2.1; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    bullets_html = "\n".join(f"<li>{b}</li>" for b in slide.bullets)
    st.markdown(
        f'<div class="slide-card"><h1>{slide.title}</h1><ul>{bullets_html}</ul></div>',
        unsafe_allow_html=True,
    )

    if slide.sources:
        with st.container():
            st.markdown("&nbsp;")
            for title, url in slide.sources:
                if url:
                    st.caption(f"출처: [{title}]({url})")
                else:
                    st.caption(f"출처: {title}")


def render_source_db_view(df: pd.DataFrame) -> None:
    st.markdown("### 출처 DB (`data/sources.db`)")
    st.caption("웹 리서치로 수집한 모든 출처를 SQLite DB에서 조회합니다.")

    if df.empty:
        st.info("아직 출처 데이터가 없습니다. `python data/build_db.py`를 먼저 실행하세요.")
        return

    col1, col2, col3 = st.columns([2, 2, 3])
    with col1:
        chapters = ["전체"] + sorted(df["chapter_num"].unique().tolist())
        chapter_filter = st.selectbox("챕터", chapters)
    with col2:
        types = ["전체"] + sorted(df["source_type"].unique().tolist())
        type_filter = st.selectbox("출처 유형", types)
    with col3:
        query = st.text_input("검색 (제목/핵심내용)", "")

    filtered = df.copy()
    if chapter_filter != "전체":
        filtered = filtered[filtered["chapter_num"] == chapter_filter]
    if type_filter != "전체":
        filtered = filtered[filtered["source_type"] == type_filter]
    if query:
        mask = filtered["source_title"].str.contains(query, case=False, na=False) | filtered[
            "key_point"
        ].str.contains(query, case=False, na=False)
        filtered = filtered[mask]

    m1, m2, m3 = st.columns(3)
    m1.metric("전체 출처 수", len(df))
    m2.metric("필터 결과", len(filtered))
    m3.metric("유튜브 출처", int((df["source_type"] == "youtube").sum()))

    st.dataframe(
        filtered[
            [
                "chapter_num",
                "chapter_name",
                "source_title",
                "source_url",
                "source_type",
                "key_point",
            ]
        ],
        column_config={
            "source_url": st.column_config.LinkColumn("URL"),
            "chapter_num": "챕터",
            "chapter_name": "챕터명",
            "source_title": "출처 제목",
            "source_type": "유형",
            "key_point": "핵심 내용",
        },
        hide_index=True,
        use_container_width=True,
        height=520,
    )


def main() -> None:
    st.markdown(
        "<h2 style='margin-bottom:0'>🧠 AI 엔지니어링 — 100 Slide Deck</h2>",
        unsafe_allow_html=True,
    )

    tab_slides, tab_db = st.tabs(["📑 슬라이드", "🗂️ 출처 DB"])

    with tab_slides:
        slides = load_slides(slides_mtime_key())
        render_slide_view(slides)

    with tab_db:
        df = load_sources_df(
            os.path.getmtime(DB_PATH) if os.path.exists(DB_PATH) else 0.0
        )
        render_source_db_view(df)


if __name__ == "__main__":
    main()
