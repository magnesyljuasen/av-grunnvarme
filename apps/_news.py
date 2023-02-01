import streamlit as st

from scripts._utils import Tweet

def news():
    st.title("Nyheter")
    c1, c2 = st.columns(2)
    with c1:
        Tweet("https://twitter.com/EGEC_geothermal").component()
        st.markdown("---")
        Tweet("https://twitter.com/SGehlin?ref_src=twsrc%5Etfw").component()
    with c2:
        Tweet("https://twitter.com/ProfSpitler").component()
        st.markdown("---")
        Tweet("https://twitter.com/BeingSaqibJaved").component()
