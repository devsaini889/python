# a small library management system using oop

class Library:
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)
    
    def showinfo(self):
        print(f"The number of books is: {self.nobooks} and the books are")
        for book in self.books:
            print(book)



l1=Library()
l1.addbook("spiderman1")
l1.addbook("spiderman2")
l1.addbook("spiderman3")
l1.addbook("spiderman4")
l1.addbook("spiderman5")
l1.addbook("spiderman6")
l1.showinfo()