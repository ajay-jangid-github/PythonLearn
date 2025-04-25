
class BookManagement:
  def __init__(self, book_name, time, price):
    self.book_name = book_name
    self.time = time
    self.price = price

  def borrow_book(self):
      print(f"your borrow {self.book_name} book and time is {self.time} and price is {self.price}")


book1 = BookManagement("Science", "2 hour", "20")
book1.borrow_book()

