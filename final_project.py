"""
This program is trying to determine a person's weekly pay
he or she receives time and a half for overtime work beyond 40 hours
The main function should call 3 function for input 
Then calculate the value
Calculate the ouput 
"""

"""
Get the wages and hours rate = input()
determine pay for the week = pay(wages)
display earnings

Get the wages and hours = input()
Worked hours = input()
hourly wage = input()


Pay()  # calculate weekly pay with time and a half
    if hours is greater than or equal 40
        amount is wages times hours
    else:
        amount equals wages times 40 + (1.5) times wages times (hours-40)

display earnings
    Print()

"""

def main ():
    (wages, hours) = getWageAndHours()
    payforweek = pay(wage, hours)
    displayEarnings(payForWeek)
    
def getWageAndHours():
    hourswroked = eval(input("Enter hours worked: "))
    hourlywage = eval(input ("Enter hourly pay: "))
    return(hourlywage, hoursworked)

def pay (wage, hours):
    if hours <= 40:
        amount = wage * hoursworked
    else: 
        amount = (wage * 40) + ((1.5) * wage * (hours-40))
    return amount
def displayEarnings(payForWeek)
    print("Week's pay: ${0:,2f}" .format(payForWeek))
main()