class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.__class__.all_authors.append(self)
    
    def contracts(self):
        return self.contracts_list
    
    def books(self):
        books = []
        for contract in self.contracts_list:
            books.append(contract.book)
        return books
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        self.contracts_list.append(new_contract)
        book.contracts_list.append(new_contract)
        return new_contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts_list:
            total += contract.royalties
        return total

class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        self.__class__.all_books.append(self)
    
    def contracts(self):
        return self.contracts_list

    def authors(self):
        authors = []
        for contract in self.contracts_list:
            authors.append(contract.author)
        return authors

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception
        if not isinstance(book, Book):
            raise Exception
        if not isinstance(date, str):
            raise Exception
        if not isinstance(royalties, int):
            raise Exception
        self.__class__.all_contracts.append(self)

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        author.contracts_list.append(self)
        book.contracts_list.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all_contracts, key=lambda c: c.date)
