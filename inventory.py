inventory = {
    "laptop":   {"price": 899.99, "quantity": 4},
    "mouse":    {"price": 19.99,  "quantity": 50},
    "keyboard": {"price": 49.99,  "quantity": 8},
    "monitor":  {"price": 229.50, "quantity": 2},
    "webcam":   {"price": 39.99,  "quantity": 15},
}

def check_low_stock(threshold):
    found = False
    print("Items below stock threshold of", threshold, ":")
    for item_name, details in inventory.items():
        if details["quantity"] < threshold:
            print("•", item_name, "- quantity:", details["quantity"],
                  "- price: $" + str(details["price"]))
            found = True
    if not found:
        print("No items are running low.")

check_low_stock(10)
