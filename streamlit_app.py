"""pdf2mbox streamlit app."""
import os
import streamlit as st
import pandas as pd
import xmpdf
import pdf2mbox

title = "pdf2mbox online"
st.set_page_config(page_title=title)
st.title(title)
st.markdown("extract emails from a PDF and convert them to MBOX messages")
st.image('pdf2mbox_diagram.png')


uploaded_pdf = st.file_uploader('upload PDF', type=['pdf'])
if uploaded_pdf:
    xms = xmpdf.Xmpdf(uploaded_pdf)
    if xms.emails:
        fname = os.path.splitext(os.path.basename(uploaded_pdf.name))[0]
        mbox_fname = fname + '.mbox'
        if os.path.exists(mbox_fname):
            os.remove(mbox_fname)               # in case of multiple runs
        mbox = pdf2mbox.Mbox(mbox_fname)
        for e in xms.emails:
            mbox.addmsg(e)
        st.success(f'MBOX with {len(xms.emails)} emails generated')
        with open(mbox_fname, 'r') as file:
            btn = st.download_button(label='download MBOX', data=file,
                                     file_name=mbox_fname)
        st.write('email metadata')
        df = pd.DataFrame(xms.email_metadata())
        st.write(df)
    else:
        st.warning(f'No emails found in {uploaded_pdf.name}.')

with st.expander("ℹ️ - more about this app ", expanded=True):
    st.write("""
*  Please report any errors (attaching the PDF if possible) by creating a new
   issue [here](https://github.com/history-lab/pdf2mbox/issues).
*  This app and pdf2mbox are free and open-source software distributed under
   the MIT License.
*  You can run pdf2mbox on the command line or in a Python script. You can find
   installation instructions [here](https://pypi.org/project/pdf2mbox/).
*  Best to install pdf2mbox in your computing environment if you plan to
   process an extensive collection of PDFs or PDFs > 200 MB.
*  You can learn more about the motivation for creating pdf2mbox and use cases
   [here](https://history-lab.github.io/pdf2mbox/).
*  Columbia University's [History Lab](http://history-lab.org) created this
   app and pdf2mbox with support from the Mellon Foundation's [Email Archives:
   Building Capacity and
   Community](https://emailarchivesgrant.library.illinois.edu/) program.""")
