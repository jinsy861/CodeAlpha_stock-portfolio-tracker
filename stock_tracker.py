
stock_price={
    "APL":57,
    "GPS":89,
    "ORG":56,
    "BNA":67,
    "WTM":79,
    "MST":48
}

portfolio={}
print("Enter the number of shares you own for each stock:")


for stock in stock_price:
    
    try:
      quantity=int(input(f"{stock:}"))
    except ValueError:
       quantity=0
    portfolio[stock]=quantity

total_investment = 0

for stock,quantity in portfolio.items():

   value=quantity*stock_price[stock]
   total_investment += value

   print(f"{stock:}{quantity} share * ${stock_price[stock]} =${value} ")

save = input("\nWould you like to save this to a file? (yes/no): ").strip().lower()

if save=='yes':
    
    with open("portfolio_summary.txt", "w") as file:
       file.write("--- Investment Summary ---\n")

       for stock,quantity in portfolio.items():
          value=quantity*stock_price[stock]
          file.write(f"{stock:}{quantity} share * ${stock_price[stock]} =${value} \n")

       file.write(f"\nTotal Investment: ${total_investment}")
    print("Saved to 'portfolio_summary.txt'")

                  
                  


