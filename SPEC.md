# AI Engineering Slide Deck — Content Spec (internal, for research agents)

This file is the shared spec for all chapter-writing agents. Follow it exactly so the
final Streamlit deck and CSV/DB assemble cleanly without manual reformatting.

## Deliverable

A ~100-slide deck about "AI Engineering" (broad overview: LLM engineering, RAG, agents,
MLOps/LLMOps, fine-tuning, evaluation, security, multimodal, careers, etc.), rendered by
a Streamlit app that pages through one Markdown file per slide.

## Slide file format

One slide = one `.md` file. Put your chapter's slide files in the chapter directory
already created under `C:\Users\playdata2\Desktop\ai-engineering\slides\<NN_chapter_slug>\`.

Filename: `NN_slug.md` where NN is a 2-digit sequence number within the chapter
(01, 02, 03, ...) and slug is a short kebab-case name. Example:
`slides/02_llm_fundamentals/03_tokenization.md`.

Content of each file (plain Markdown, UTF-8, Korean language for body text):

```
# Slide Title (short, punchy)

- Bullet 1 (one idea per bullet, concise)
- Bullet 2
- Bullet 3
- Bullet 4 (3-6 bullets total; not a wall of text — this is a SLIDE, not an essay)

> Source: [Short Source Title](https://actual-url-you-found)
> Source: [Second Source Title](https://actual-url-you-found)
```

Rules:
- Title is a single `#` H1 line.
- Bullets are `-` list items, 3-6 per slide, each one short line (not multi-paragraph).
- End with 1-3 `> Source:` blockquote lines ONLY when the slide states a specific fact,
  stat, product name/version, or claim you got from a real source you searched for.
  Conceptual/definitional slides can skip sources if they're general knowledge, but at
  least half your chapter's slides should carry a real citation.
- NEVER fabricate a URL or title. Only cite pages you actually found via WebSearch/WebFetch.
- Write body content in Korean (한국어). Keep technical terms (RAG, LLM, GPU, API 등) in
  their common form (English acronym or mixed Korean/English as normally written in
  Korean tech writing).
- No emojis.

## Sources CSV (structured data for the DB)

In addition to the inline `> Source:` lines, append every source you used to a CSV file
specific to your batch: `C:\Users\playdata2\Desktop\ai-engineering\data\sources_<batch>.csv`
(batch name given in your task). Create the file with this exact header if it doesn't
exist yet, then append one row per source used (a source used on multiple slides can
appear multiple times, once per slide):

```
chapter_num,chapter_name,slide_file,source_title,source_url,source_type,key_point
```

- `chapter_num`: the 2-digit chapter number (e.g. 02)
- `chapter_name`: the chapter slug (e.g. llm_fundamentals)
- `slide_file`: filename of the slide that cites it (e.g. 03_tokenization.md)
- `source_title`: short title of the source page/video
- `source_url`: the real URL
- `source_type`: `google` for a regular web/article source, `youtube` for a YouTube video
- `key_point`: one short phrase (no commas — use a semicolon if needed, or wrap in
  double quotes) describing what fact this source backs up

Use proper CSV quoting (wrap fields containing commas in double quotes).

## Research approach

For each chapter, do real web research before writing:
1. Use WebSearch for general/Google-style results on the chapter's subtopics (use 2026
   as the current year when searching for "latest"/"current" info).
2. Use WebSearch with queries like `site:youtube.com <topic>` (or just `<topic> youtube
   explained`) to find 1-3 relevant YouTube videos per chapter and cite them where
   relevant (e.g. a conceptual overview slide citing an explainer video).
3. Use WebFetch on the most promising results to pull real facts, numbers, product
   names, and quotes — don't just paraphrase a search snippet blindly.
4. Prefer primary/authoritative sources (official docs, vendor engineering blogs,
   reputable tech publications, arXiv) over random blogspam.

## Slide count target

Hit the target slide count for your assigned chapter(s) given in your task (±1 is fine).
Each chapter's first slide should be a section header slide (title + 1-line description
of what the chapter covers, no citation needed).

## When done

Report back (in your final message) a short summary: chapters completed, slide counts
per chapter, number of sources cited, and the CSV file path you wrote.
