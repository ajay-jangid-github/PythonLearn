
class User:
  def __init__(self, userName):
    self.userName = userName

  
  def show_profile(self):
    print(f"User: {self.userName}")

class Seller(User):
  def __init__(self, userName, shopName):
    super().__init__(userName)
    self.shopName = shopName

  def list_product(self):
      print(f"Product {self.shopName} added a product")

# seller1 = User("ajay_seller", "ajay shop", "ajay_product")
seller1 = Seller("ajay_seller", "ajay shop")
seller1.show_profile()
seller1.list_product()