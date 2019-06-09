class User(object):
    def __init__(self, name, email):
        self.name =  name
        self.email = email
        self.books = {}

    def __repr__(self):
        return "User {user}, email:  {email}, books read: {books}".format(user=self.name, email=self.email, books=len(self.books))

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{user}'s email has changed to {email}".format(user=self.name, email=self.email))

    def __eq__(self, other):
        if (self.name == other.name and self.emal == other.email):
            return self.name == other.name and self.email == other.email

    def read_book (self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        rating_values = []
        for value in self.books.values():
            if value != None:
                rating_values.append(value)
        for value in rating_values:
            sum += value
        return sum / len(rating_values)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return self.isbn

    def add_rating(self, rating):
        if rating != None:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid rating!")

    def __eq__(self, other):
        if (self.title == other.title and self.isbn == other.isbn ):
            return self.title == other.title and self.isbn == other.isbn

    def get_average_rating(self):
        sum_rating = 0
        rating_values2 = []
        for rating in self.ratings:
            if rating != None:
                rating_values2.append(rating)
        for rating in rating_values2:
            sum_rating += rating
        return sum_rating / len(rating_values2)

    def	__hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

    def get_author(self):
        return self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email {email}".format(email=email))
        else:
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print("User with email {email} already exist!".format(email=email))
        else:
            self.users[email] = User(name, email)
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        highest_value = 0
        highest_book = ""
        for book, value in self.books.items():
            if value > highest_value:
                highest_book = book
                highest_value = value
        return highest_book

    def highest_rated_book(self):
        highest_rating = 0
        highest_book = ""
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_book = book
        return highest_book

    def most_positive_user(self):
        highest_avg = 0
        positive_user = ""
        for user in self.users.values():
            if user.get_average_rating() > highest_avg:
                highest_avg = user.get_average_rating()
                positive_user = user
        return positive_user
