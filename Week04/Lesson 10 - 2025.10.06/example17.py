class Bill:
    header = "Halil Marketing"
    payment = True
    content = {}

    def __init__(self, mName, tax_number, date):
        self.mName = mName
        self.tax_number = tax_number
        self.date = date
        self.total = 0

    def add_product(self):
        product_name = input("Please enter the product name: ")
        product_quantity = int(input("Please enter the product quantity: "))
        product_price = float(input("Please enter the unit price od product: "))
        product_amount = product_quantity * product_price
        self.content[product_name] = [product_amount, product_price, product_amount]
        self.total += product_amount
        print(f"{self.content[product_name]} has been added to the cart")
        return self.invoice_amount()

    def remove_product(self):
        product_name = input("Please enter the product name: ")
        product_amount = self.content[product_name][2]
        self.total -= product_amount
        print(f"{self.content[product_name]} has been removed to the cart")
        del self.content[product_name]
        return self.invoice_amount()

    def invoice_amount(self):
        print("Current invoice amount: {:.2f}".format(self.total))
        return self.total


customer = Bill("Jack", 123456, 2024)
customer.add_product()
