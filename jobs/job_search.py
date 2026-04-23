```python
import streamlit as st
from .job_portals import JobPortal
from .suggestions import JOB_SUGGESTIONS, LOCATION_SUGGESTIONS

def render_job_search():
    st.title("🔍 Smart Job Search (Europe Edition)")

    col1, col2 = st.columns(2)

    with col1:
        job_query = st.text_input(
            "Job Title",
            placeholder="Software Engineer"
        )

    with col2:
        location = st.text_input(
            "Location",
            value="Dublin",
            placeholder="Dublin, Ireland"
        )

    if st.button("SEARCH JOBS"):
        if job_query:
            portal = JobPortal()
            results = portal.search_jobs(job_query, location)

            st.subheader("Results")

            for r in results:
                st.markdown(f"""
                **{r['portal']}**
                
                {r['title']}
                
                [View Jobs]({r['url']})
                """)
        else:
            st.warning("Enter job title")
```
