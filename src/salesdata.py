import sys
import os

# Append the parent directory to the system path to allow importing modules from there
sys.path.append(os.path.dirname(__file__) + "/..")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def parsedata(data):
    df = pd.DataFrame(data)
    # Calculate revenue by multiplying units sold by price per unit
    df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    # Calculate profit by applying the discount to the revenue
    df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

    
    summary = df.describe()
    
    print(summary)

    
    print("📊 Sales Data:")

    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Print the date for the current row
        print(f"  - Date: \"{row['Date']}\"")
        # Print the product for the current row
        print(f"    Product: \"{row['Product']}\"")
        # Print the units sold for the current row
        print(f"    Units_Sold: {row['Units_Sold']}")
        # Print the revenue for the current row, converted to integer
        print(f"    Revenue: {int(row['Revenue'])}")
        # Print the profit for the current row
        print(f"    Profit: {row['Profit']}")
        

    # Print a separator line
    print("\n-----------------------------------------")
    print("\nSummary:")
    # Print the total sales by summing all revenue values and converting to integer
    print(f"  Total_Sales: {int(df['Revenue'].sum())}")
    # Print the average profit, formatted to one decimal place
    print(f"  Average_Profit: {df['Profit'].mean():.1f}")
    # Print the best-selling product by finding the product with the maximum total units sold
    print(f"  Best_Selling_Product: \"{df.groupby('Product')['Units_Sold'].sum().idxmax()}\"")
    # Print the top region by finding the region with the maximum total revenue
    print(f"  Top_Region: \"{df.groupby('Region')['Revenue'].sum().idxmax()}\"")
    # Create a line plot showing revenue over time by product using seaborn
    sns.lineplot(data=df, x="Date", y="Revenue", hue="Product")
   
    plt.title("Revenue Over Time by Product")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.legend(title="Product")
    plt.show()

def pdata1(data):
    df = pd.DataFrame(data)
    # Calculate revenue by multiplying units sold by price per unit
    df["Revenue"] = df["Units_Sold"] * df["Price_per_Unit"]
    # Calculate profit by applying the discount to the revenue
    df["Profit"] = df["Revenue"] * (1 - df["Discount"]/100)

   
    summary = df.describe()
    print(summary)

    
    print("📊 Sales Data:")

    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        #Print the date for the current row
        print(f"  - Date: \"{row['Date']}\"")
        #Print the product for the current row
        print(f"    Product: \"{row['Product']}\"")
        #Print the units sold for the current row
        print(f"    Units_Sold: {row['Units_Sold']}")
        #Print the revenue for the current row, converted to integer
        print(f"    Revenue: {int(row['Revenue'])}")
        #Print the profit for the current row
        print(f"    Profit: {row['Profit']}")

    #Print a separator line
    print("\n-----------------------------------------")
    print("\nSummary:")
    print(f"  Total_Sales: {int(df['Revenue'].sum())}")
    print(f"  Average_Profit: {df['Profit'].mean():.1f}")
    print(f"  Best_Selling_Product: \"{df.groupby('Product')['Units_Sold'].sum().idxmax()}\"")
    print(f"  Top_Region: \"{df.groupby('Region')['Revenue'].sum().idxmax()}\"")
    sns.lineplot(data=df, x="Date", y="Revenue", hue="Product")
    plt.title("Revenue Over Time by Product")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.legend(title="Product")
    plt.show()

userinput = input("Enter the sales data file path (or press Enter to use default data): ")
# Check if the user provided a non-empty input
if userinput.strip():
    import data.userinput as ui
else:
    from data.data import data
    pdata1(data)
       
