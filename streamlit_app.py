"""pdf2mbox streamlit app."""
import streamlit as st
import pandas as pd
import xmpdf

title = "pdf2mbox online"
st.set_page_config(page_title=title)
st.title(title)
st.markdown("extract emails from a PDF and convert them to MBOX messages")
st.image('pdf2mbox_diagram.png')


uploaded_pdf = st.file_uploader('upload PDF', type=['pdf'])
if uploaded_pdf:
    xms = xmpdf.Xmpdf(uploaded_pdf)
    st.write(xms.info())
    st.success('MBOX generated')
    with open('test.mbox', 'r') as file:
        btn = st.download_button(label='Download MBOX', data=file,
                                 file_name='test.mbox')
    st.write('Email metadata:')
    df = pd.DataFrame(xms.emails)
    st.write(df)

with st.expander("ℹ️ - More about this app ", expanded=False):
    st.write("""
*  Please report any errors (attaching the PDF if possible) or make feature
   requests by creating a new issue
   [here](https://github.com/history-lab/pdf2mbox/issues).
*  This app and pdf2mbox are free and open-source software distributed under
   the MIT License.
*  You can run pdf2mbox on the command line or in a Python script in your
   computing environment if it has Python 3.8 or higher. You can find
   installation instructions [here](https://pypi.org/project/pdf2mbox/).
    * You should install pdf2mbox in your computing environment if you want to
      process a collection of PDFs or process a PDF file greater than 40 MB in
      size. This app is for demonstration purposes and one-off conversions.
*  You can learn more about the motivation for creating pdf2mbox and use cases
   [here](https://history-lab.github.io/pdf2mbox/).
*  Columbia University's [History Lab](http://history-lab.org) created this
   app and pdf2mbox with support from the Mellon Foundation's [Email Archives:
   Building Capacity and
   Community](https://emailarchivesgrant.library.illinois.edu/) program.""")
