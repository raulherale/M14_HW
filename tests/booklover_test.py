import unittest
from BookLover import BookLover

class BookLoverTestSuite(unittest.TestCase):
 

    b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
    print(b1.num_books)
    print(b1.book_list)
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
        b1.add_book('Dune',4)
        book = 'Dune'
        self.assertTrue(b1.has_read(book))
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
        b1.add_book('Dune',4)
        b1.add_book('Dune',4)
        book = 'Dune'
        self.assertEqual(len(b1.book_list[b1.book_list['book_name'] == book]) , 1)
        
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
        b1.add_book('Witcher',4)
        book = 'Witcher'
        self.assertTrue(b1.has_read(book))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
        book = 'Harry Potter'
        self.assertFalse(b1.has_read(book))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
        b1.add_book('Harry Potter',3)
        b1.add_book('Witcher',4)
        b1.add_book('Dune',4)
        expected = 3
        self.assertEqual(b1.num_books,expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        b1 = BookLover('Ashrith', 'Ash@gmail.com','Fantasy')
        b1.add_book('Harry Potter',3)
        b1.add_book('Witcher',4)
        b1.add_book('Dune',4)
        testcase = b1.book_list[b1.book_list.book_name.isin(b1.fav_books())]['book_rating']
        testvalue = min(testcase) > 3
        self.assertTrue(testvalue)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)