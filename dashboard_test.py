import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dummy Dashboard", layout="wide")

# -------------------------
# DATA
# -------------------------
workflows = [
    "CustomerOnboardingWF",
    "LoanApprovalWF",
    "TransactionProcessingWF",
    "DocumentArchivalWF",
    "RiskAssessmentWF"
]

methods = [
    "start",
    "in progress",
    "archive start",
    "archive completed",
    "end"
]

rows = []
for wf in workflows:
    for m in methods:
        rows.append({
            "Workflow Class": wf,
            "Method": m,
            "Failed": 1,
            "Retry": 0,
            "Stalled": 0,
            "Archived": 100
        })

data = pd.DataFrame(rows)

st.title("Dummy Dashboard")

# -------------------------
# LAYOUT
# -------------------------
left_panel, center_panel, right_panel = st.columns([1, 5, 1])

# -------------------------
# LEFT PANEL (NAVIGATION)
# -------------------------
with left_panel:
    

    menu = st.radio(
        "",
        ["Access", "Workflow Status", "Workflow Details"]
    )

# -------------------------
# RIGHT PANEL (FILTERS)
# -------------------------
with right_panel:
    st.subheader("Filters")

    workflow_selected = st.selectbox(
        "Workflow Class",
        ["All"] + workflows
    )

   

    show_failed = st.checkbox("Show only failed/retrystalled")
    show_favorites = st.checkbox("Show only favorites")
    show_methods = st.checkbox("Show methods")
    include_archive = st.checkbox("Include for archive")
    auto_refresh = st.checkbox("Auto refresh")
    exclude_disabled = st.checkbox("Exclude disabled")

# -------------------------
# FILTER LOGIC (UNCHANGED)
# -------------------------
filtered = data.copy()

if workflow_selected != "All":
    filtered = filtered[filtered["Workflow Class"] == workflow_selected]



if show_failed:
    filtered = filtered[(filtered["Failed"] > 0) | (filtered["Retry"] > 0)]

if not include_archive:
    filtered = filtered[filtered["Archived"] < 200]

# -------------------------
# CENTER PANEL (PAGE LOGIC ADDED)
# -------------------------
with center_panel:
    st.subheader(menu)

    if menu == "Access":
        st.success("Welcome to Dashboard")

    elif menu == "Workflow Status":
        st.table(filtered)

    elif menu == "Workflow Details":
        st.table(pd.DataFrame({"Workflow Class": workflows}))

# -------------------------
# BOTTOM BUTTONS
# -------------------------
st.markdown("---")


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("Show All")

with c2:
    st.button("Show Exceptions")

with c3:
    st.button("Show Stalled")

with c4:
    st.button("Favorites")