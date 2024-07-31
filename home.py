import streamlit as st
from firebase_admin import firestore


def app():
    db = firestore.client()

    if st.session_state.username == "":
        st.markdown("### Login to be able to post")
    else:
        post = st.text_area(label=" :orange[+ New Post]", placeholder="Post your thought", height=None, max_chars=500)
        if st.button("Post", use_container_width=20):
            if post != "":
                info = db.collection("Posts").document(st.session_state.username).get()
                if info.exists:
                    info = info.to_dict()
                    if "Content" in info.keys():
                        pos = db.collection("Posts").document(st.session_state.username)
                        pos.update({"Content": firestore.ArrayUnion([f"{post}"])})
                    else:
                        data = {"Content":[post], "Username":st.session_state.username}
                        db.collection("Posts").document(st.session_state.username).set(data)
                else:
                    data = {"Content": [post], 'Username': st.session_state.username}
                    db.collection('Posts').document(st.session_state.username).set(data)

                st.success("Post uploaded!")


    st.header(" :violet[Latest Posts] ")

    docs = db.collection("Posts").get()
    for doc in docs:
        d=doc.to_dict()
        print(doc)
        print(f"{d=}")
        try:
            # st.markdown("""
            #     <style>
            #
            #     .stTextArea [data-baseweb=base.input] [disabled=""]{
            #         #background-color: #e3d8c8;
            #         -webkit-text-fill-color: white;
            #     }
            #     </style>
            #     """, unsafe_allow_html=True)

            st.text_area(label=":green[Posted by:] "+f":orange[{d['Username']}]",
                         value=d["Content"][-1], height=20, disabled=True)
        except:
            ...


if __name__ == "__main__":
    app()
