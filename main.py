import streamlit as st
import pandas as pd
from datetime import datetime
import time
# from delete_book import delete_book_from_lib
from delete_book import delete_book_from_lib
from insert import add_book
from select2 import get_all_books
import plotly.express as px


st.set_page_config(
    page_title="LibraTrack",
    page_icon="📚",
    layout="centered"
)

def search_books(query, field):
    all_books = get_all_books()
    
    field_map = {
        "Title": "title",
        "Author": "author", 
        "Genre": "genre",
        "Year": "publication_year"
    }
    column = field_map.get(field, "title")
    return all_books[all_books[column].str.contains(query, case=False, na=False)]

st.title("🏛️📚 LibraTrack ")
st.subheader("Your Personalized Library 📕🔍")
tabs = st.tabs(["📗👀 View Books", "📚➕ Add Book", "📘🔍 Search Books", "❌📕 Remove Book", "Analytics"])

# Tab 1: View Books
with tabs[0]:
    st.header("📚 Library Collection")
    
    all_books = get_all_books()
    
    if not all_books.empty:
        if st.button("Refresh Book List", key = 'button'):
            with st.spinner("Refreshing page..."):
                time.sleep(5)
                all_books = get_all_books()
                st.divider()
                for i, book in all_books.iterrows():
                    col1, col2, col3 = st.columns([3, 2, 1])
                    with col1:
                        st.subheader(f"📖 {book['title']}")
                        st.write(f"✍️ Author: {book['author']}")
                    with col2:
                        st.write(f"🎭 Genre: {book['genre']}")
                        st.write(f"🗓️ Year: {book['publication_year']}")
                    with col3:
                        is_read = "🟢 Read" if book["is_read"] else "🔴 Unread"
                        st.write(is_read)
                    st.divider()
                    
        else:
            st.divider()
            for i, book in all_books.iterrows():
                col1, col2, col3 = st.columns([3, 2, 1])
                with col1:
                    st.subheader(f"📖 {book['title']}")
                    st.write(f"✍️ Author: {book['author']}")
                with col2:
                    st.write(f"🎭 Genre: {book['genre']}")
                    st.write(f"🗓️ Year: {book['publication_year']}")
                with col3:
                    is_read = "🟢 Read" if book["is_read"] else "🔴 Unread"
                    st.write(is_read)
                st.divider()
                
    else:
        st.info("No books in the library. Add some books to get started!")


# Tab 2: Add Book
with tabs[1]:
    st.header("📚➕ Add New Book")

    with st.form(key='add_book_form', clear_on_submit=True):
        title = st.text_input("📖 Book Title", max_chars=100, key='title')
        author = st.text_input("✍️ Author", max_chars=100, key='author')
        genre = st.selectbox("🎭 Genre", [
            "Fiction", "Non-Fiction", "Science Fiction", "Fantasy", 
            "Mystery", "Biography", "History", "Romance", "Science", 
            "Technology", "Philosophy", "Self-Help", "Thriller", "Other",
        ], key='genre')
        year = st.number_input("🗓️ Publication Year", min_value=1000, max_value=datetime.now().year, value=2020, key='year')
        is_read = st.checkbox("📖🤔 Have you read this book?", value=False, key='is_read')
        
        submit_button = st.form_submit_button(label='➕ Add Book')
                    
        if submit_button:
            if title and author and genre and year:
                with st.spinner(f"Adding Book '{title}' to your library..."):
                    add_book(title, author, genre, year, is_read)
                    time.sleep(3)
                    st.success(f"Book '{title}' added successfully!")
                    
            else:
                st.error("All fields are required!")
        

# Tab 3: Search Books
with tabs[2]:
    st.header("🔍📕 Search Books")
    col1, col2 = st.columns(2)
    with col1:
        search_query = str(st.text_input("📝 Search for a book", placeholder="Enter search term..."))
    with col2:
        search_field = st.selectbox("Search in field:", [ "📖 Title", "✍️ Author", "🎭 Genre"])
    
    if search_query:
        results = search_books(search_query, search_field)
        st.subheader(f"🔍 Found {len(results)} results")
        st.divider()
        if not results.empty:
            for i, book in results.iterrows():
                col1, col2, col3 = st.columns([3, 2, 1])
                with col1:
                    st.subheader(f"📖 {book['title']}")
                    st.write(f"✍️ Author: {book['author']}")
                with col2:
                    st.write(f"🎭 Genre: {book['genre']}")
                    st.write(f"🗓️ Year: {book['publication_year']}")
                with col3:
                    is_read = "🟢 Read" if book["is_read"] else "🔴 Unread"
                    st.write(is_read)
                st.divider()
                
        else:
            st.info("No books found matching your search criteria.")

#Tab 4: Remove Book
with tabs[3]:

        col1, col2 = st.columns(2)
        with col1:
            st.header("🗑️📕 Remove Book")
            st.divider()
            remove_input = str(st.text_input("📝 Enter book title:", placeholder="Enter book title..."))
            remove_book = remove_input.lower()
            if st.button("Remove Book", key=f"{book['id']}"):
                with st.spinner(f"Deleting Book '{remove_book.title()}' from library..."):
                    delete_book_from_lib(book["title"])
                    time.sleep(5)
                    st.success(f"Book '{remove_book.title()}' is deleted from library")
        with col2:
            st.image("books.png")
       
with tabs[4]:

    st.subheader("📊 Read/Unread Analytics")
    read_count = all_books[all_books["is_read"] == True].shape[0]
    unread_count = all_books[all_books["is_read"] == False].shape[0]
    pie_data = pd.DataFrame({
        "is_read": ["Read", "Unread"],
        "Count": [read_count, unread_count]
    })
    print(pie_data)
    fig_pie = px.pie(pie_data, values="Count", names="is_read", title="Read vs Unread Books")
    st.plotly_chart(fig_pie)

# Add footer
st.markdown("---")
st.markdown("📚 Library Management System - Created with Streamlit")