import pandas as pd

class BookLover:
    
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    
    def __init__(self,name,email,fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
    
    def add_book(self,book_name, rating):
        
        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books = self.num_books + 1
    
    def has_read(self,book_name):
        
        if book_name not in list(self.book_list['book_name']):
            return(False)
        else :
            return(True)
    
    def num_books_read(self):
        
        return(len(self.book_list))
    
    
    def fav_books(self):
        
        return(list(self.book_list[self.book_list['book_rating'] > 3]['book_name']))
    
    
        
            