#define a function called hotel_cost with one argument nights as input
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los angeles" == city:
        return 475
    
#Define a function called rental car cost with an argument called days
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else: 
        return 40*days
    
def trip_cost(City, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(City) + spending_money

print("cost of car rental: ", rental_car_cost(5))

print("cost of plane ride: ", plane_ride_cost("los angeles"))

print("cost of hotel room: ", hotel_cost(7))

print("total cost of the trip:", trip_cost("Los Angeles", 7,500))

print(trip_cost("Tampa", 6,500 ))