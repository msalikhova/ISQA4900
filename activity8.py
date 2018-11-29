import csv

# Class Customer defines  attributes,  methods and a constructor that initializes all attributes
class Customer:
    def __init__(self,cust_id=0,first_name="",last_name="",company_name="", address="",city="",state="",zip=""):
        self.cust_id = cust_id
        self.firstName=first_name
        self.lastName=last_name
        self.company_name=company_name
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip

def display_title():
    print("Customer viewer")
    print()


def csv_reader():
    FILENAME = "customers.csv"
    customers = []

    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)

        for row in reader:
                # convert row to Customer object
            customer = Customer(row[0], (row[1]), (row[2]), (row[3]), (row[4]), (row[5]), (row[6]), (row[7]))
            customers.append(customer)
        return customers

def find_customer(cust_id):
    customers = csv_reader()
    for customer in customers:
        if (customer.cust_id == cust_id ):
            return customer
    else:
        #print("No customer with that specified ID.")
        return "No customer with that specified ID."

def main():
    display_title()

    while True:
        cust_id= input("Enter customer ID:  ")
        customer = find_customer(cust_id)
        print(customer.firstName + " " + customer.lastName)
        print(customer.address)
        print(customer.city + " " + customer.state + " " + customer.zip)
        print()

        ask = input("Continue? (y/n):  ")
        print()
        if ask!="y":
            print ("Bye!")
            break

if __name__ == "__main__":
    main()


