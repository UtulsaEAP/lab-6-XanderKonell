def calculate_car_wash_price(service_1, service_2):
    prices = {
        "Base car wash": 10,
        "Tire shine": 2,
        "Wax": 3,
        "Rain repellent": 2
    }
   #type your code here 
    total_price = prices.get("Base car wash", 0)
    if service_1 in prices:
        total_price += prices[service_1]
    if service_2 in prices:
        total_price += prices[service_2]

    # Call the function to calculate car wash price
    print("ZyCar Wash")
    print("Base car wash - $10")
    if service_1 != "-":
        print(f"{service_1} - ${prices.get(service_1, 0)}")
    if service_2 != "-":
        print(f"{service_2} - ${prices.get(service_2, 0)}")
    print("-----")
    print(f"Total price: ${total_price}")