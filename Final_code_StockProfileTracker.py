import tkinter as tk
from tkinter import messagebox

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        ticker = ticker.upper()
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares

    def remove_stock(self, ticker, shares):
        ticker = ticker.upper()
        if ticker in self.portfolio:
            if shares >= self.portfolio[ticker]:
                del self.portfolio[ticker]
            else:
                self.portfolio[ticker] -= shares

    def get_portfolio(self):
        return self.portfolio

class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.portfolio = StockPortfolio()

        self.root.title("Stock Portfolio Tracker")

        # Configure grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        frame = tk.Frame(root)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Add Stock Section
        tk.Label(frame, text="Add Stock", font=("Times New Roman", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(frame, text="Ticker:", font=("Times New Roman", 14)).grid(row=1, column=0, pady=5, sticky="e")
        self.add_ticker_entry = tk.Entry(frame, font=("Times New Roman", 14))
        self.add_ticker_entry.grid(row=1, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Shares:", font=("Times New Roman", 14)).grid(row=2, column=0, pady=5, sticky="e")
        self.add_shares_entry = tk.Entry(frame, font=("Times New Roman", 14))
        self.add_shares_entry.grid(row=2, column=1, pady=5, sticky="w")

        tk.Button(frame, text="Add", font=("Times New Roman", 14), command=self.add_stock).grid(row=3, column=0, columnspan=2, pady=10)

        # Remove Stock Section
        tk.Label(frame, text="Remove Stock", font=("Times New Roman", 16)).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Label(frame, text="Ticker:", font=("Times New Roman", 14)).grid(row=5, column=0, pady=5, sticky="e")
        self.remove_ticker_entry = tk.Entry(frame, font=("Times New Roman", 14))
        self.remove_ticker_entry.grid(row=5, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Shares:", font=("Times New Roman", 14)).grid(row=6, column=0, pady=5, sticky="e")
        self.remove_shares_entry = tk.Entry(frame, font=("Times New Roman", 14))
        self.remove_shares_entry.grid(row=6, column=1, pady=5, sticky="w")

        tk.Button(frame, text="Remove", font=("Times New Roman", 14), command=self.remove_stock).grid(row=7, column=0, columnspan=2, pady=10)

        # View Portfolio Section
        tk.Button(frame, text="View Portfolio", font=("Times New Roman", 14), command=self.view_portfolio).grid(row=8, column=0, columnspan=2, pady=10)

        self.portfolio_text = tk.Text(frame, height=10, width=40, font=("Times New Roman", 14))
        self.portfolio_text.grid(row=9, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.portfolio_text.tag_configure("center", justify="center")

        frame.grid_rowconfigure(9, weight=1)
        frame.grid_columnconfigure(1, weight=1)

    def add_stock(self):
        ticker = self.add_ticker_entry.get().strip()
        shares = self.add_shares_entry.get().strip()

        if not ticker or not shares.isdigit():
            messagebox.showerror("Error", "Please enter valid ticker and shares.")
            return

        self.portfolio.add_stock(ticker, int(shares))
        messagebox.showinfo("Success", f"Added {shares} shares of {ticker}.")
        self.add_ticker_entry.delete(0, tk.END)
        self.add_shares_entry.delete(0, tk.END)

    def remove_stock(self):
        ticker = self.remove_ticker_entry.get().strip()
        shares = self.remove_shares_entry.get().strip()

        if not ticker or not shares.isdigit():
            messagebox.showerror("Error", "Please enter valid ticker and shares.")
            return

        self.portfolio.remove_stock(ticker, int(shares))
        messagebox.showinfo("Success", f"Removed {shares} shares of {ticker}.")
        self.remove_ticker_entry.delete(0, tk.END)
        self.remove_shares_entry.delete(0, tk.END)

    def view_portfolio(self):
        self.portfolio_text.delete(1.0, tk.END)
        portfolio = self.portfolio.get_portfolio()
        if not portfolio:
            self.portfolio_text.insert(tk.END, "Portfolio is empty.", "center")
        else:
            for ticker, shares in portfolio.items():
                self.portfolio_text.insert(tk.END, f"{ticker}: {shares} shares\n", "center")

if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioApp(root)
    root.mainloop()
