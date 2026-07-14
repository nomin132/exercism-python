"""Currency exchange helper functions for Exercism."""

def exchange_money(budget, exchange_rate):
    exchanged_moneh=budget/exchange_rate
    return exchanged_moneh

def get_change(budget, exchanging_value):
    remain_money=budget-exchanging_value
    return remain_money

def get_value_of_bills(denomination, number_of_bills):
    no_bills=denomination*number_of_bills
    return no_bills

def get_number_of_bills(amount, denomination):
    remain_bill=int(amount // denomination)
    return remain_bill

def get_leftover_of_bills(amount, denomination):
    leftover_bills= amount % denomination
    return leftover_bills

def exchangeable_value(budget, exchange_rate, spread, denomination):
    rate_with_fee=exchange_rate*(1 + spread/100)
    exchanged=budget/rate_with_fee
    deno_aft=exchanged // denomination
    value_aft=int(deno_aft*denomination)
    return value_aft
    
