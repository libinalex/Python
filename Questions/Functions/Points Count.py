'''
PointsCount
You went to a book fair held in Chennai. You decided to buy a number of books.

You need to write a function (Name of the function: book_purchase) 
to take the price of the books and find the Total Cost of the purchase you made on that day.

Input: #Cost of the books you purchased.

12 330 1288 55

Output: # Total Cost

1685

Input: #Cost of the books you purchased.

20 100 250 350 1000 550

Output: # Total Cost

2270
'''


def book_purchase(*prices):
    prices=list(map(int,amount.split()))
    cost=0
    for price in prices:
        cost = cost + price
    print("The total cost is:",cost)
amount=input("Enter the cost of books you purchased: ")
book_purchase(amount)