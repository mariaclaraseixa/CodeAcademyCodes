# Ground Shipping
def shipping_cost_ground(weight):
    flat_charge = 20
    if weight <= 2:
        shipping_type = "drone shipping"
        rule = "2 lb or less"
        price_per_pound = 1.50
    elif 2 < weight <= 6:
        rule = "Over 2 lb but less than or equal to 6 lb"
        shipping_type = "ground shipping"
        price_per_pound = 3.00
    elif 6 < weight <= 10:
        rule = "Over 6 lb but less than or equal to 10 lb"
        shipping_type = "ground shipping"
        price_per_pound = 4.00
    elif weight >= 10:
        rule = "Over 10 lb"
        shipping_type = "ground shipping"
        price_per_pound = 4.75
    charge_shipping = price_per_pound * weight + flat_charge
    return charge_shipping


# Premium shipping
def shipping_cost_premium(weight):
    return 125.00


def print_answer(method, price):
    print(method, "Shipping: $", price)


# Drone shipping
def shipping_cost_of_drone(weight):
    if weight <= 2:
        shipping_type = "drone shipping"
        rule = "2 lb or less"
        price_per_pound = 4.50
    elif 2 <= weight <= 6:
        shipping_type = "drone shipping"
        rule = "Over 2 lb but less than or equal to 6 lb"
        price_per_pound = 9.00
    elif 6 <= weight <= 10:
        shipping_type = "drone shipping"
        rule = "Over 6 lb but less than or equal to 10 lb"
        price_per_pound = 12.00
    elif weight >= 10:
        shipping_type = "drone shipping"
        rule = "Over 10 lb"
        price_per_pound = 14.25

    return price_per_pound * weight

    print(shipping_cost_of_drone(1.5))


def print_cheapest_shipping_method(weight):
    ground = shipping_cost_ground(weight)
    premium = shipping_cost_premium(weight)
    drone = shipping_cost_of_drone(weight)
    print_answer("premium", premium)
    print_answer("ground", ground)
    print_answer("drone", drone)
    if ground < premium and ground < drone:
        method = "standard ground"
        cost = ground
    elif premium < ground and premium < drone:
        method = "premium ground"
        cost = premium
    else:
        method = "drone"
        cost = drone
    print(method)
    return cost

if __name__ == '__main__':
    print("[Code Academy] Sal's Shipping")
    weight = 41.5
    print(print_cheapest_shipping_method(weight))
