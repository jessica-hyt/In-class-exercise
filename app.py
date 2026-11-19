"""
In-Class Exercise 5 - Streamlit Retail Business Dashboard
Course: ISOM3400 2026 Fall
Assessment: In-Class Exercise 5 (Effort ICE - a genuine attempt counts even if imperfect)
Weight: 2%
Duration: 30 minutes
Due: Thursday 19 November 2026 (lecture day)
Environment: VS Code / local Python

Student information (fill in):
Name: ______________________________
Student ID: ________________________
Email: _____________________________

How to use:
1. Fill in your name / ID / email above.
2. In this folder, install packages:  pip install -r requirements.txt
3. Complete the fill-in-the-blank lines below so the app matches the expected UI
   (see Retail_Business_Dashboard.png). Use only the allowed Streamlit calls
   shown in streamlit_functions.png.
4. Run the app:  streamlit run app.py
5. Click Submit and check the summary (try the default target, then a target
   above 100000 for the Challenge).
6. Zip ONLY app.py and requirements.txt. The zip filename must include your
   Student ID, for example {StudentID}_InclassEx5.zip.
7. Submit the zip on Canvas, or email both the course instructor and the TA.

Scope:
- Allowed Streamlit functions only: st.title, st.header, st.write,
  st.number_input, st.selectbox, st.button, st.success.
- Do NOT wrap the program in functions (no def, no main()). All code stays at
  top level.
- Do not add pandas, matplotlib, numpy, or other libraries.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Retail Business Dashboard
# ---------------------------------------------------------------------------
# A retail manager enters a monthly sales target, selects a region, then
# clicks Submit to see a summary.
# Replace each ______ with the missing code. Do not pre-write answers in
# functions — keep everything at top level.

# Blank A: page title (match the screenshot).
______  # hint: st.title("...")

# Blank B: section header (match the screenshot).
______  # hint: st.header("...")

# Blank C: short instruction under the header (match the screenshot).
______  # hint: st.write("...")

# Blank D: monthly sales target (USD). Default 50000. Minimum 0. (match the screenshot)
# Do not set a maximum (the Challenge uses a target above 50000).
sales_target = ______  # hint: st.number_input("...")

# Blank E: region dropdown (match the options shown in the document).
region = ______  # hint: st.selectbox("...")

# Blank F: Submit button, then show the entered values and a success message (match the screenshot).
if ______:  # hint: st.button("...")
    ______  # hint: st.write("...")  — sales target, include a $
    ______  # hint: st.write("...")  — region selected
    ______  # hint: st.success("...")

    # Challenge: if the sales target is greater than 100000, show an extra message (match the screenshot).
    if ______:  # hint: compare sales_target with 100000
        ______  # hint: st.write("...")
