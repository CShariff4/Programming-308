import sys                                      


#book class
class Book:
    def __init__(self):
        self.authorfirst = input("Type the first name of the author: ")
        self.authorlast = input("Type the last name of the author: ")
        self.title = input('Type the name of the title: ')
        self.url = input('Type the name of the source link: ')
        self.date = input("Type the date of publication: ")

        

    def mybookcite(self):
        print('Here is your book reference:' + self.authorfirst, self.authorlast, self.title, self.url, self.date)

#article class
class Article(Book):
    def __init__(self):
        super().__init__() 
        self.arttitle =  input("Type the first name of the article: ")
        self.jorntitle =  input("Type the first name of the journal: ")

    def myarticlecite(self):
        print('Here is your article reference:' + self.authorfirst, self.authorlast, self.title, self.url, self.date, self.arttitle, self.jorntitle)


#menu to get started
method = input("Enter B for book, Enter A for article, Enter q to quit: ")
if (method.lower() == 'b'):
    print('we got this far')
    b1 = Book()
    b1.mybookcite()
elif method.lower() == ('a'):
    a1 = Article()
    a1.myarticlecite()
elif method.lower() == ('q'):
    print(f'Program ended') 
    exit()



