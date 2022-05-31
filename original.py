"""
    Developer: Pete Coutros
    Course: CMIS 102

    Description:
        This program will calculate the weekly pay for a paper carrier
        The user will input the number of paper on the route,
        the number of days the paper is delivered per week,
        and the amount of tips received for the week

        The calculations will be done with a "hard-coded" newspaper cost of $1,
        and a commission rate of 25%
"""


def main():
    """ <String describing the main() function here> """

    #Initialize Variables (newpaperCost = $1, commissionRate = 25%)
    newspaperCost = 1
    commissionRate = 0.25

    #Display welcome message
    name = input("Hello, what is your name?\t")
    print("\nHello " + name + ", this program will assist you in calculating your weekly pay as a paper carrier.")
    print("To get started we will first need some information from you:")

    #Prompt user for number of papers on route
    numPapersOnRoute = int(input("\nHow many papers do you delivere on your route?\t"))

    #Prompt user for number of days paper is delivered per week
    numDaysPerWeek = int(input("How many days a week do you deliver papers?\t"))

    #Prompt user for amount of tips received z week
    numTipsPerWeek = int(input("How much did you receive in tips this week?\t"))

    #Calculate total number of papers per week (number of papers * number of days)
    totalPapersPerWeek = numPapersOnRoute * numDaysPerWeek

    #Calculate weekly salary (total number of papers per week * cost of newspaper * commission rate)
    weeklySalary = totalPapersPerWeek * newspaperCost * commissionRate

    #Calculate total pay (weekly salary + tips for the week)
    totalPay = weeklySalary + numTipsPerWeek

    #Display the results (total number of papers delivered for the week, the weekly salary, the tips for the week, and the total pay for the week)
    print("\nThe total number of papers you delivered for the week was " + str(totalPapersPerWeek) + " papers.")
    print("Using a predetermined newspaper cost of $1 and a commission rate of 25%, your weekly salary is $" + str(weeklySalary))
    print("The total amount you collected in tips was $" + str(numTipsPerWeek))
    print("Therefore making your total pay for the week $" + str(totalPay))
    print("\nThank you " + name + ", enjoy the rest of your day!")

#----------Execute-------------------
main()
