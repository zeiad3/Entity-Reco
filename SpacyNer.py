import streamlit as st 
import spacy 
from spacy import displacy 
nlp = spacy.load("en_core_web_sm")

def main():
    st.title("Named Entity Reco")
    st.write("Enter some Text to Identify named Entities ")
    
    text=st.text_area("Input Text")
    
    if st.button("Analyze"):
        if text:
            doc=nlp(text)
            html=displacy.render(doc,style="ent",page=True)
            st.write(html,unsafe_allow_html=True)
        else:
            st.write("Please Input Text first")
if __name__=="__main__":
    main()