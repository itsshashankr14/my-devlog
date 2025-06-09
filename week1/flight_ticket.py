#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    rate_per_adult = 37550.0
    rate_per_child = rate_per_adult / 3
    base_fare = (no_of_adults * rate_per_adult) + (no_of_children * rate_per_child)
    total_with_tax = base_fare + (0.07 * base_fare)
    final_total = total_with_tax - (0.10 * total_with_tax)
    total_ticket_cost = round(final_total, 2)
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)