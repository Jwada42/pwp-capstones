"""
Tome Rater Project
Submission: Junichi Wada
Date: 4-1-19

"""

class User(object):
    def __init__(self, name, email):
        # name is a string
        self.name = name
        # email is a string
        self.email = email
        #will contain user's rating of the book
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        return " Your email has been updated with the following email: {email} ".format(email=new_email)
        

    def __repr__(self):
        return " User: {user}, Email: {email}, Books Read: {books} ".format(user=self.name, email=self.email, books=len(self.books)) 
    
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            other_user = self
    
    def read_book(self, book, rating = None):
        self.books[book] = rating
    
                     
class Book(object):
    def __init__(self, title, isbn):
        # title is a string
        self.title = title
        # isbn is a number
        self.isbn = isbn
        # will contain the ratings of the book
        self.rating = []
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return " This book's ISBN: {ISBN} has been updated. ".format(ISBN = new_isbn)
    
    def add_rating(self, rating):
        try:
            if rating >= 0 and rating <= 4:
                self.rating.append(rating)
            else:
                print("Invalid Rating")
        except TypeError:
            "Invalid Type."


    def get_average_rating(self, rating):
        avg_rating = 0
        total_rating = 0
        for rating in self.books.values():
            total_rating += rating
        avg_rating = total_rating / len(self.books)
        return avg_rating

    def __repr__(self):
        return "Title: {book}\n" \
                "ISBN: {isbn}\n"\
                .format(book=self.title,
                        isbn=self.isbn)  
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            other_book = self

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        # author will be a string
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)
    
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        # subject will be a string
        self.subject = subject
        # level will be a string
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
 

class TomeRater:
    def __init__(self):
        # will map a user's email to User 
        self.users = {}
        # will map a Book to number os Users who read it 
        self.books = {}   
    
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title,subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email: {email}".format(email=email))
        if user:
            user.read_book(book, rating)
            book.add_rating(rating)
            self.books[book] = self.books.get(book, 0) + 1

    
    def add_user(self, name, email, user_books = None):
        if email not in self.users:
            self.users[email] = User(name, email)
        if books is not None:
            for book in books:
                self.add_book_to_user(book, email)
    
#Extensions

    def check_user(self, email):
        user = self.users.get(email, "No user with email: {email}".format(email=email))
        if user:
            print("This email is already taken. Please try another!)
        else:
            return self.add_user()
                  
    
    def isbn_check(self, isbn):
        isbn = self.users.get(isbn, 0)
        if isbn not in self.isbn():
           self.set_isbn()


# Analysis Methods
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for user in self.users.values():
            print(user)
                  
    def most_read_book(self):
        return max(self.books, key=self.books.get)
    
    def highest_rated_book(self):
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')
        
    def most_positive_user(self):
        highest_rated = max(rating.get_average_rating() for rating in self.users.values())
        return str([user for user in self.users.values() if user.get_average_rating() == highest_rated]).strip('[]')




                  
