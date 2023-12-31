import streamlit as st
import requests
import json
import base64
import countrywrangler as cw
from datetime import date
from translate import Translator
from congif import API_KEY

st.set_page_config(page_title="News One",page_icon = "icon.png",layout="centered",initial_sidebar_state="auto",menu_items=None)
st.header("Today's News")
translator= Translator(to_lang="en")

st.markdown(
    """
    <meta name="Top Headline" content="News One">
    <meta name="keywords" content="Top Headline, News One, Country News">
    <meta name="author" content="Pranav Nalawade">
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <link rel="canonical" href=https://newsone.onrender.com">
    """,
    unsafe_allow_html=True
)
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def add_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.5),rgba(1,1,1,0.5)), url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def hideAll():
    hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """   
    st.markdown(hide, unsafe_allow_html=True)

def remove_underline():
    st.markdown(
        """
        <style>
        a {
            text-decoration: none;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def headLine(country):
    try:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
        response = requests.get(url)
        data = json.loads(response.text)
        news = data
        for new in news['articles']:
            try:
                if new['title'] is None or new['description'] is None or new['urlToImage'] is None:
                    pass
                else:
                    st.subheader("Title")
                    st.write(translator.translate(str(new['title'])))
                    st.image(str(new['urlToImage']))
                    st.subheader("Description")
                    st.write(translator.translate(str(new['description'])))
                    name = str(new['title'])
                    Time = str(new['publishedAt'])[:10]
                    st.write("Published at : ",Time)
                    name = name.replace(" ", "+") 
                    name = name.replace(":", "")
                    st.markdown(f"[For more info...](https://www.google.com/search?q={name})", unsafe_allow_html=True)
                    st.write("---")
            except:
                st.write("got an error")
    except:
        pass


def India():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
        response = requests.get(url)
        data = json.loads(response.text)
        news = data
        for new in news['articles']:
            try:
                if new['title'] is None or new['description'] is None or new['urlToImage'] is None:
                    pass
                else:
                    
                    st.subheader("Title")
                    st.write(translator.translate(str(new['title'])))
                    st.image(str(new['urlToImage']))
                    st.subheader("Description")
                    st.write(translator.translate(str(new['description'])))
                    name = str(new['title'])
                    Time = str(new['publishedAt'])[:10]
                    st.write("Published at : ",Time)
                    name = name.replace(" ", "+") 
                    name = name.replace(":", "")
                    st.markdown(f"[For more info...](https://www.google.com/search?q={name})", unsafe_allow_html=True)
                    st.write("---")
            except:
                st.write("got an error")
    except:
        pass


def main():
    hideAll()
    remove_underline()
    user_input = st.text_input("Enter the name of Country : ")
    if user_input:
        try:
            codes = cw.Normalize.name_to_alpha2(user_input)
            headLine(codes)
        except:
            st.write("Invalid country name.")
    else:
        India()
    st.markdown("""
        ## Thanks for using our Services
    """)

    st.markdown(
        """
        <meta name="description" content="A Streamlit app that shows top headlines from different countries.">
        """,
        unsafe_allow_html=True,
    ) 
if __name__ == '__main__':
    main()
