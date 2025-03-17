# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# import datetime
# import json
# from collections import Counter

# # Initialize session state for book analytics
# if 'books' not in st.session_state:
#     # Sample book data with read status
#     st.session_state.books = [
#         {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "status": "available", "read_status": "read", "genre": "Fiction", "date_added": "2023-01-15"},
#         {"id": 2, "title": "1984", "author": "George Orwell", "status": "available", "read_status": "unread", "genre": "Science Fiction", "date_added": "2023-02-20"},
#         {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "status": "checked_out", "read_status": "read", "genre": "Fiction", "date_added": "2023-03-10"},
#         {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "status": "available", "read_status": "unread", "genre": "Romance", "date_added": "2023-04-05"},
#         {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "status": "available", "read_status": "read", "genre": "Fiction", "date_added": "2023-05-12"},
#         {"id": 6, "title": "The Hobbit", "author": "J.R.R. Tolkien", "status": "available", "read_status": "read", "genre": "Fantasy", "date_added": "2023-06-18"},
#         {"id": 7, "title": "Brave New World", "author": "Aldous Huxley", "status": "available", "read_status": "unread", "genre": "Science Fiction", "date_added": "2023-07-22"},
#         {"id": 8, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "status": "checked_out", "read_status": "unread", "genre": "Fantasy", "date_added": "2023-08-30"},
#         {"id": 9, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "status": "available", "read_status": "unread", "genre": "Fiction", "date_added": "2023-09-14"},
#         {"id": 10, "title": "Jane Eyre", "author": "Charlotte Brontë", "status": "available", "read_status": "read", "genre": "Romance", "date_added": "2023-10-25"}
#     ]

# if 'reading_history' not in st.session_state:
#     # Sample reading history
#     st.session_state.reading_history = [
#         {"book_id": 1, "date_read": "2023-03-10", "rating": 4},
#         {"book_id": 3, "date_read": "2023-06-15", "rating": 5},
#         {"book_id": 5, "date_read": "2023-08-20", "rating": 3},
#         {"book_id": 6, "date_read": "2023-11-05", "rating": 4}
#     ]

# # Function to toggle read status
# def toggle_read_status(book_id):
#     for book in st.session_state.books:
#         if book['id'] == book_id:
#             if book['read_status'] == 'read':
#                 book['read_status'] = 'unread'
#                 # Remove from reading history if exists
#                 st.session_state.reading_history = [h for h in st.session_state.reading_history if h['book_id'] != book_id]
#             else:
#                 book['read_status'] = 'read'
#                 # Add to reading history
#                 today = datetime.datetime.now().strftime("%Y-%m-%d")
#                 st.session_state.reading_history.append({"book_id": book_id, "date_read": today, "rating": None})
#             break

# def library_analytics():
#     st.title("Library Analytics Dashboard")
    
#     # Create DataFrame from books
#     books_df = pd.DataFrame(st.session_state.books)
    
#     # Total counts
#     total_books = len(books_df)
#     read_books = len(books_df[books_df['read_status'] == 'read'])
#     unread_books = len(books_df[books_df['read_status'] == 'unread'])
    
#     # Display metrics
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("Total Books", total_books)
#     with col2:
#         st.metric("Read Books", read_books)
#     with col3:
#         st.metric("Unread Books", unread_books)
    
#     # Create tabs for different analytics views
#     tab1, tab2, tab3, tab4 = st.tabs(["Read vs Unread", "Reading by Genre", "Reading History", "Book List"])
    
#     with tab1:
#         st.subheader("Read vs Unread Books")
        
#         # Create pie chart
#         fig = px.pie(
#             names=['Read', 'Unread'],
#             values=[read_books, unread_books],
#             title="Read vs Unread Books",
#             color_discrete_sequence=['#4CAF50', '#F44336']
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
#         # Completion rate
#         completion_rate = (read_books / total_books) * 100 if total_books > 0 else 0
#         st.subheader(f"Library Completion Rate: {completion_rate:.1f}%")
        
#         # Progress bar
#         st.progress(completion_rate/100)
    
#     with tab2:
#         st.subheader("Reading Progress by Genre")
        
#         # Group by genre and read status
#         genre_stats = books_df.groupby(['genre', 'read_status']).size().unstack(fill_value=0)
        
#         if 'read' not in genre_stats.columns:
#             genre_stats['read'] = 0
#         if 'unread' not in genre_stats.columns:
#             genre_stats['unread'] = 0
            
#         genre_stats['total'] = genre_stats['read'] + genre_stats['unread']
#         genre_stats['completion_rate'] = (genre_stats['read'] / genre_stats['total'] * 100).round(1)
        
#         # Create bar chart
#         fig = go.Figure()
#         fig.add_trace(go.Bar(
#             name='Read',
#             x=genre_stats.index,
#             y=genre_stats['read'],
#             marker_color='#4CAF50'
#         ))
#         fig.add_trace(go.Bar(
#             name='Unread',
#             x=genre_stats.index,
#             y=genre_stats['unread'],
#             marker_color='#F44336'
#         ))
        
#         fig.update_layout(
#             title='Books by Genre and Read Status',
#             barmode='stack',
#             xaxis={'title': 'Genre'},
#             yaxis={'title': 'Number of Books'}
#         )
        
#         st.plotly_chart(fig, use_container_width=True)
        
#         # Display table with completion rates
#         st.subheader("Genre Completion Rates")
#         genre_display = genre_stats[['read', 'unread', 'total', 'completion_rate']].reset_index()
#         genre_display.columns = ['Genre', 'Read', 'Unread', 'Total', 'Completion Rate (%)']
#         st.dataframe(genre_display.sort_values('Completion Rate (%)', ascending=False))
    
#     with tab3:
#         st.subheader("Reading History")
        
#         if st.session_state.reading_history:
#             # Create history dataframe
#             history_df = pd.DataFrame(st.session_state.reading_history)
            
#             # Add book titles
#             title_map = {book['id']: book['title'] for book in st.session_state.books}
#             history_df['book_title'] = history_df['book_id'].map(title_map)
            
#             # Convert dates
#             history_df['date_read'] = pd.to_datetime(history_df['date_read'])
#             history_df = history_df.sort_values('date_read')
            
#             # Books read per month
#             history_df['month'] = history_df['date_read'].dt.strftime('%Y-%m')
#             monthly_counts = history_df.groupby('month').size().reset_index(name='books_read')
            
#             # Line chart
#             fig = px.line(
#                 monthly_counts, 
#                 x='month', 
#                 y='books_read',
#                 markers=True,
#                 title="Books Read per Month"
#             )
#             st.plotly_chart(fig, use_container_width=True)
            
#             # Display recent reads
#             st.subheader("Recent Reads")
#             recent_df = history_df[['book_title', 'date_read', 'rating']].sort_values('date_read', ascending=False)
#             recent_df.columns = ['Book Title', 'Date Read', 'Rating']
#             recent_df['Date Read'] = recent_df['Date Read'].dt.strftime('%Y-%m-%d')
#             st.dataframe(recent_df)
#         else:
#             st.info("No reading history available yet")
    
#     with tab4:
#         st.subheader("Book List with Read Status")
        
#         # Filter options
#         status_filter = st.selectbox(
#             "Filter by Status", 
#             options=["All", "Read", "Unread"]
#         )
        
#         # Apply filters
#         filtered_df = books_df.copy()
#         if status_filter == "Read":
#             filtered_df = filtered_df[filtered_df['read_status'] == 'read']
#         elif status_filter == "Unread":
#             filtered_df = filtered_df[filtered_df['read_status'] == 'unread']
        
#         # Display books with action buttons
#         for index, book in filtered_df.iterrows():
#             col1, col2 = st.columns([3, 1])
#             with col1:
#                 st.write(f"**{book['title']}** by {book['author']}")
#                 st.write(f"Genre: {book['genre']} | Status: {book['read_status'].title()}")
            
#             with col2:
#                 if book['read_status'] == 'read':
#                     button_label = "Mark as Unread"
#                 else:
#                     button_label = "Mark as Read"
                
#                 if st.button(button_label, key=f"toggle_{book['id']}"):
#                     toggle_read_status(book['id'])
#                     st.rerun()

# # Run the app
# library_analytics()