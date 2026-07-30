# Healthcare AI Response Evaluator — Version 3.0

## What changed

- Fixed the duplicated `st.set_page_config()` startup block that caused invalid Python syntax.
- Added professional sidebar navigation.
- Added dedicated Home, Evaluate Response, Compare Responses, Clinical Case Library, QA Analytics, Methodology, and About pages.
- Added a product-style landing page with calls to action, platform features, and a transparent review workflow.
- Added searchable and filterable clinical case-library navigation.
- Added a “Why this score?” panel with dimension-by-dimension interpretation.
- Preserved Markdown, JSON, CSV, comparison, and analytics functionality.
- Added Version 3 release notes, project positioning, roadmap, and responsible-use boundaries.
- Kept both `app.py` and `streamlit_app.py` so either Streamlit entry-point configuration can run the same Version 3 application.

## Deployment

Upload both `app.py` and `streamlit_app.py` to the root of the GitHub repository. The Streamlit deployment should continue using its existing entry-point filename.
