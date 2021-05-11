import sys                                      #printing citation
                                                #calling book case? or calling function?


#book class
class book:
    def __init__(self, authorfirst, authorlast, title, source, pub):
        self.authorfirst = authorfirst
        self.authorlast = authorlast
        self.title = title
        self.source = source
        self.pub = pub

        def mybookcite(self):
                print('Here is your book reference:' + book(authorfirst, authorlast, title, source, pub))

#article class
class article:
   def __init__(self, arttitle, jorntitle, jorndate):
        self.arttitle = arttitle
        self.jorntitle = jorntitle
        self.jorndate = jorndate    

        def myarticlecite(self):
            print('Here is your article reference:' + article(arttitle, jorntitle, jorndate))


#menu to get started
method = input("Enter B for book, Enter A for article, Enter q to quit: ")
if method.lower == str(f'b'):
        b1 = mybookcite()
        print(f'Book Citing: ')
elif method.lower == str(f'a'):
        print(f'Article Citing: ')
elif method.lower == str(f'q'):
    print(f'Program ended') 
    exit()



#book variables 
authorfirst = input("Type the first name of the author: ")
authorlast = input("Type the last name of the author: ")
title = input('Type the name of the title: ')
source = input('Type the name of the source link: ')
pub = input("Type the date of publication: ")

#b1 = [firstname, lastname, workname, link, pubdate]
#print(b1)
b1 = book(authorfirst,authorlast,title,source,pub)
print(b1)

