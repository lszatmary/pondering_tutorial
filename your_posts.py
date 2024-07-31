
import streamlit as st
from firebase_admin import firestore

def app():

    db = firestore.client()

    if st.session_state.username == "":
        st.markdown("### Please Login first")
    else:
        st.title(f"Posted by: {st.session_state.username}")

        result = db.collection("Posts").document(st.session_state.username).get()
        r = result.to_dict()
        content = r["Content"]

        def delete_post(c):
            try:
                db.collection("Posts").document(st.session_state.username).update({"Content": firestore.ArrayRemove([c])})
                st.warning("Post deleted")
            except:
                st.write("Something went wrong..")

        for c in content[::-1]:
            st.text_area(label="", value=c)
            st.button("Delete post", on_click=delete_post, args=([c]), key=c)


    # if st.session_state.username == "":
    #     st.markdown("### Please login")
    # else:
    #     info = db.collection("Posts").document(st.session_state.username).get()
    #     if info.exists:
    #         info = info.to_dict()
    #         for post in info["Content"]:
    #             st.text_area(label="Your post", value=post, height=20, disabled=True)



