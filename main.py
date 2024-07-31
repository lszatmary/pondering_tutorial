import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, trending, your_posts
import firebase_admin
from firebase_admin import credentials

st.set_page_config(page_title="Pondering")

try:
    app = firebase_admin.get_app()
except ValueError as e:
    # cred = credentials.Certificate("pondering-tutorial-2d180-fb24ee2954c1.json")
    firebase_config = dict(st.secrets["firebase"]) #{key: value for key, value in firebase_credentials.items()}
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

# firebase_admin.get_app(name='pondering-tutorial-2d180')

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title="Pondering ",
                options=["Home", "Account", "Trending", "Your Posts", "About"],
                icons=["house-fill", "person-circle", "trophy-fill", "chat-fill"],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == "Home":
            home.app()
        elif app == "Account":
            account.app()
        elif app == "Trending":
            trending.app()
        elif app == "Your Posts":
            your_posts.app()
        else:
            about.app()


if __name__ == "__main__":
    multiapp = MultiApp()
    multiapp.run()

# TODO kicsit játszogatni az option_menu paramétereivel, hgoy lássam mi, mit csinál
