class Book:
    def __init__(self,title,page_count) -> None:
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
    # book = Book("The World According to Garp", 69)
        print("Flipping the page...wow, you read fast!")



book = Book("And Then there Were None", 272)


    


        