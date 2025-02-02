import streamlit as st

# Pages navigation
def main():
    st.sidebar.title("Zomata Food Delivery Management System")
    st.sidebar.image(r"C:\Users\Hp\OneDrive\Documents\Streamlit\test\Scripts\ZOMATA\image\Gemini_Generated_Image_txgo0ytxgo0ytxgo.jpeg")

    page = st.sidebar.radio("Select the Page", ["HOME","CRUD", "QUERY"])

    if page == "HOME":
        import HOME
        HOME.main()
    elif page == "CRUD":
        import CRUD
        CRUD.main()
    elif page == "QUERY":
        import QUERY
        QUERY.main()
        
    

if __name__ == "__main__":
    main()
