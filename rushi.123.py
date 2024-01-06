import tkinter as tk

# Mock portfolio data
portfolio = []

# Function to add a stock to the portfolio
def add_stock():
    stock_name = entry_stock_name.get()
    stock_quantity = entry_stock_quantity.get()
    buying_price = entry_buying_price.get()
    selling_price = entry_selling_price.get() or 0  # If selling price is empty, assume 0
    buying_date = entry_buying_date.get()
    selling_date = entry_selling_date.get()

    if stock_name and stock_quantity and buying_price and buying_date:
        buying_price = float(buying_price)
        selling_price = float(selling_price)
        profit_loss = (selling_price - buying_price) * float(stock_quantity) if selling_price else None
        stock_info = {
            "Stock": stock_name,
            "Quantity": int(stock_quantity),
            "Buying Price": buying_price,
            "Selling Price": selling_price,
            "Buying Date": buying_date,
            "Selling Date": selling_date
        }
        if profit_loss is not None:
            stock_info["Profit/Loss"] = profit_loss
        portfolio.append(stock_info)
        display_portfolio()

# Function to delete a stock from the portfolio
def delete_stock():
    selected_stock = listbox_portfolio.curselection()
    if selected_stock:
        index = selected_stock[0]
        del portfolio[index]
        display_portfolio()

# Function to clear input fields
def clear_fields():
    entry_stock_name.delete(0, tk.END)
    entry_stock_quantity.delete(0, tk.END)
    entry_buying_price.delete(0, tk.END)
    entry_selling_price.delete(0, tk.END)
    entry_buying_date.delete(0, tk.END)
    entry_selling_date.delete(0, tk.END)

# Function to display portfolio and summary
def display_portfolio():
    listbox_portfolio.delete(0, tk.END)
    for item in portfolio:
        stock_info = f"{item['Stock']} - Quantity: {item['Quantity']} - Buying Price: ${item['Buying Price']:.2f} - Buying Date: {item['Buying Date']}"
        if item['Selling Price']:
            stock_info += f" - Selling Price: ${item['Selling Price']:.2f} - Selling Date: {item['Selling Date']} - Profit/Loss: ${item['Profit/Loss']:.2f}"
        listbox_portfolio.insert(tk.END, stock_info)

    total_profit_loss = sum(item['Profit/Loss'] for item in portfolio if 'Profit/Loss' in item) if any('Profit/Loss' in item for item in portfolio) else 0
    label_summary.config(text=f"Total Stocks: {len(portfolio)} | Total Profit/Loss: ${total_profit_loss:.2f}")

# Create GUI
root = tk.Tk()
root.title("Portfolio Tracker")



label_heading = tk.Label(root, text="Portfolio Tracker", font=("Arial", 20, "bold"), bg='lightblue')
label_heading.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

label_stock_name = tk.Label(root, text="Stock Name:", bg='lightblue')
label_stock_name.grid(row=1, column=0, padx=10, pady=5, sticky="W")

entry_stock_name = tk.Entry(root)
entry_stock_name.grid(row=1, column=1, padx=10, pady=5)

label_stock_quantity = tk.Label(root, text="Quantity:", bg='lightblue')
label_stock_quantity.grid(row=2, column=0, padx=10, pady=5, sticky="W")

entry_stock_quantity = tk.Entry(root)
entry_stock_quantity.grid(row=2, column=1, padx=10, pady=5)

label_buying_price = tk.Label(root, text="Buying Price:", bg='lightblue')
label_buying_price.grid(row=3, column=0, padx=10, pady=5, sticky="W")

entry_buying_price = tk.Entry(root)
entry_buying_price.grid(row=3, column=1, padx=10, pady=5)

label_selling_price = tk.Label(root, text="Selling Price:", bg='lightblue')
label_selling_price.grid(row=4, column=0, padx=10, pady=5, sticky="W")

entry_selling_price = tk.Entry(root)
entry_selling_price.grid(row=4, column=1, padx=10, pady=5)

label_buying_date = tk.Label(root, text="Buying Date (YYYY-MM-DD):", bg='lightblue')
label_buying_date.grid(row=5, column=0, padx=10, pady=5, sticky="W")

entry_buying_date = tk.Entry(root)
entry_buying_date.grid(row=5, column=1, padx=10, pady=5)

label_selling_date = tk.Label(root, text="Selling Date (YYYY-MM-DD):", bg='lightblue')
label_selling_date.grid(row=6, column=0, padx=10, pady=5, sticky="W")

entry_selling_date = tk.Entry(root)
entry_selling_date.grid(row=6, column=1, padx=10, pady=5)

button_add_stock = tk.Button(root, text="Add Stock", command=add_stock, bg='lightgreen')
button_add_stock.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

listbox_portfolio = tk.Listbox(root, height=10, width=75)
listbox_portfolio.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

button_delete_stock = tk.Button(root, text="Delete Stock", command=delete_stock, bg='salmon')
button_delete_stock.grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

label_summary = tk.Label(root, text="Total Stocks: 0 | Total Profit/Loss: $0.00", bg='lightblue')
label_summary.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

button_clear_fields = tk.Button(root, text="Clear Fields", command=clear_fields, bg='orange')
button_clear_fields.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="WE")

root.mainloop()

