import streamlit as st
import streamlit as st

st.title("Hermes StudyBuddy")

st.write("My first AI app")
st.set_page_config(page_title="Hermes StudyBuddy")

st.title("📚 Hermes StudyBuddy")

st.subheader("AI Assistant for Students")

option = st.selectbox(
    "Choose Feature",
    [
        "Study Plan",
        "Interview Tips",
        "Summarize Notes"
    ]
)

if option == "Study Plan":
    subject = st.text_input("Enter subject")

    if subject:
        st.success(f"Study plan created for {subject}")

        st.write("""
        ✅ Morning: Learn concepts  
        ✅ Afternoon: Practice problems  
        ✅ Evening: Revision  
        """)

elif option == "Interview Tips":
    st.write("""
    - Practice communication
    - Learn basics clearly
    - Prepare projects
    - Stay confident
    """)

elif option == "Summarize Notes":
    notes = st.text_area("Paste notes")

    if notes:
        st.info("Summary:")
        st.write(notes[:150])