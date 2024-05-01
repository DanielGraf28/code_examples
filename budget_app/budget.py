class Catergory:
  def __init__(self, name):
      self.name = name
      self.ledger = []
  def __str__(self):
      title = f"{self.name:*^30}\n"
      items = ""
      total = 0
      for item in self.ledger:
          items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
          total += item['amount']
      output = title + items + "Total: " + str(total)
      return output
  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})
  def withdraw(self, amount, description=""):
      if self.check_funds(amount):
          self.ledger.append({"amount": -amount, "description": description})
          return True
      return False
  def get_balance(self):
      total_cash = 0
      for item in self.ledger:
          total_cash += item["amount"]
      return total_cash
  def transfer(self, amount, category):
      if self.check_funds(amount):
          self.withdraw(amount, "Transfer to " + category.name)
          category.deposit(amount, "Transfer from " + self.name)
          return True
      return False
  def check_funds(self, amount):
      if self.get_balance() >= amount:
          return True
      return False
def create_spend_chart(categories):
  spend_amounts = []
  for category in categories:
      spent = 0
      for item in category.ledger:
          if item["amount"] < 0:
              spent += abs(item["amount"])
      spend_amounts.append(round(spent, 2))
  total = round(sum(spend_amounts), 2)
  spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spend_amounts))
  header = "Percentage spent by category\n"
  chart = ""
  for value in reversed(range(0, 101, 10)):
      chart += str(value).rjust(3) + '|'
      for percent in spent_percentage:
          if percent >= value:
              chart += " o "
          else:
              chart += "   "
      chart += " \n"
  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda category: category.name, categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
  for x in zip(*descriptions):
      footer += "    " + "".join(map(lambda s: s.center(3), x)) + "\n"
  return (header + chart + footer).rstrip("\n")
