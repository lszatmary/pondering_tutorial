import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# cred = credentials.Certificate("pondering-tutorial-2d180-fb24ee2954c1.json")
# firebase_admin.initialize_app(cred)


def app():
    st.title("Welcome to :violet[Pondering] :smiley:")

    if "username" not in st.session_state:
        st.session_state.username = ""
    if "useremail" not in st.session_state:
        st.session_state.useremail = ""
    if "signedin" not in st.session_state:
        st.session_state.signedin = False

    def sign_in():
        try:
            user = auth.get_user_by_email(email)
            st.write(f"Login successful. Welcome {user.uid}!")
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedin = True
        except:
            st.warning("Login Failed")

    def sign_out():
        st.session_state.signedin = False
        st.session_state.username = ""
        st.session_state.useremail = ""

    if not st.session_state.signedin:
        choice = st.selectbox(label="Login/Signup", options=["Login", "Sign up"])
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        if choice == "Login":
            st.button("Login", on_click=sign_in)
        else:
            username = st.text_input("Enter your unique username")
            if st.button("Create my account"):
                user = auth.create_user(email=email, password=password, uid=username)

                st.success("Account created successfully!")
                st.markdown("Please Login using your email and password")
                st.balloons()
    else:
        st.write(f"Name: {st.session_state.username}")
        st.write(f"Email: {st.session_state.useremail}")
        st.button("Sign out", on_click=sign_out)
