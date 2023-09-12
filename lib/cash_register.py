#!/usr/bin/env python3


class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.items = []
    self.transactions = []
    self.discount = discount

  def add_item(self, title, price, quantity=1):
      # self.items.append(name)
      for i in range(0, quantity):
        self.items.append(title)
        self.total += price
      # self.last_price = price
      self.transactions.append({"title": title, "price": price, "quantity": quantity})

  def apply_discount(self):
    if self.discount > 0 :
      self.total = self.total - (self.total * (self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else :
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if len(self.transactions) == 0:
      self.total = 0.0
    else :
      last_transaction = self.transactions.pop()
      self.total = self.total - (last_transaction["price"] * last_transaction["quantity"])
    
    

