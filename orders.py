import csv
from datetime import datetime

def read_csv_file(csv_filename):
    """
    Reads a CSV file and returns its contents as a list of lists.
    """
    with open(csv_filename, encoding='latin-1') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

def compute_monthly_revenue(csv_filename):
    monthly_revenue = {}
    with open(csv_filename, encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = datetime.strptime(row['date'], '%Y-%m-%d')
            month = date.strftime('%Y-%m')
            revenue = float(row['revenue'])
            if month not in monthly_revenue:
                monthly_revenue[month] = 0
            monthly_revenue[month] += revenue
    return monthly_revenue

def compute_product_revenue(csv_filename):
    product_revenue = {}
    with open(csv_filename, encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = row['product']
            revenue = float(row['revenue'])
            if product not in product_revenue:
                product_revenue[product] = 0
            product_revenue[product] += revenue
    return product_revenue

def compute_customer_revenue(csv_filename):
    customer_revenue = {}
    with open(csv_filename, encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer = row['customer']
            revenue = float(row['revenue'])
            if customer not in customer_revenue:
                customer_revenue[customer] = 0
            customer_revenue[customer] += revenue
    return customer_revenue

def top_10_customers_by_revenue(csv_filename):
    customer_revenue = {}
    with open(csv_filename, encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customer = row['customer']
            revenue = float(row['revenue'])
            if customer not in customer_revenue:
                customer_revenue[customer] = 0
            customer_revenue[customer] += revenue
    sorted_customers = sorted(customer_revenue.items(), key=lambda x: x[1], reverse=True)
    top_10_customers = dict(sorted_customers[:10])
    return top_10_customers


def main():
    print("Script starts from here!\nPlease give you response to check results.")
    response = input("Enter a number (1-5) to select a function to execute: ")

    function_map = {
        "1": read_csv_file('csv_filename.csv'),
        "2": compute_monthly_revenue('csv_filename.csv'),
        "3": compute_product_revenue('csv_filename.csv'),
        "4": compute_customer_revenue('csv_filename.csv'),
        "5": top_10_customers_by_revenue('csv_filename.csv')
    }

    if response in function_map:
        function_map[response]()
    else:
        print("Invalid response. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
