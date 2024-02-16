import math

def sales_prediction():
    all_sales = float(input())
    annual_profit = all_sales*0.19
    print(annual_profit+all_sales)
    pass


def yard_to_meter():
    yard_length = float(input())
    print(0.914*yard_length*1000)
    print(0.914*yard_length)
    print(0.914*yard_length/1000)
    pass


def cashier():
    goods1 = float(input())
    goods2 = float(input())
    goods3 = float(input())
    goods4 = float(input())
    goods5 = float(input())

    sum = goods1 + goods2 + goods3 + goods4 + goods5
    print (sum)
    pdv = sum * 0.14
    print(round(pdv, 2))
    print(round(sum+pdv, 2))
    pass

    
def odometer():
    speed = float(input())
    speed_up = float(input())
    time1 = float(input())
    time2 = float(input())
    print(speed*time1 + abs(speed_up)*time1*time1/2 + (abs(speed_up)*time1+speed)*time2)
    pass


def payment_instalments():
    sum_buy = float(input())
    payments = int(input())
    instalment = 1.05*sum_buy/payments
    print(1.05*sum_buy)
    print(instalment)
    pass


def miles_per_galon():
    miles_driven = float(input())
    gallons_of_gas_used = float(input())
    print(miles_driven/gallons_of_gas_used)
    pass


def cookie():
    amount_of_cookie = int(input())
    print(1.5/48*amount_of_cookie)
    print(1/48*amount_of_cookie)
    print(2.75/48*amount_of_cookie)
    pass


def vineyard():
    length = float(input())
    length_op = float(input())
    length_between = float(input())
    print(int((length-2*length_op)/length_between))
    pass


def compound_interest():
    p = float(input())
    r = float(input())
    n = int(input())
    t = float(input())
    print(p*((1+r/n/100)**(n*t)))
    pass

if __name__ == "__main__":
    eval(input() + "()")