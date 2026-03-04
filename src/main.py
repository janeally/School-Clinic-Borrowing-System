import tkinter as tk
from tkinter import messagebox
from product import Product
from inventory_manager import InventoryManager

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Inventory Subsystem")
        self.root.geometry("500x450")
        self.root.configure(bg="#2c3e50")  # Dark professional theme

        # Core Subsystem Logic
        self.products = [
            Product("SKU-102", "DJI Camera", 20),
            Product("SKU-103", "Wireless Earbuds", 100),
            Product("SKU-104", "Mini Drone - FlyCam 2.0", 10)
        ]
        self.manager = InventoryManager()

        # UI Header
        self.header = tk.Label(root, text="RETAIL INVENTORY SYSTEM", 
                               font=("Helvetica", 16, "bold"), 
                               bg="#2c3e50", fg="white", pady=20)
        self.header.pack()

        # Product Selector
        self.selected_product = tk.StringVar()
        self.selected_product.set(self.products[0].name)  # Default selection

        tk.Label(root, text="Select Product:", bg="#2c3e50", fg="white").pack(pady=(10,0))
        self.product_menu = tk.OptionMenu(root, self.selected_product, *[p.name for p in self.products])
        self.product_menu.pack(pady=5)

        # Bind dropdown change to update dashboard
        self.selected_product.trace("w", lambda *args: self.update_display())

        # Dashboard Display
        self.stats_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10)
        self.stats_frame.pack(pady=10, fill="x", padx=20)

        self.info_label = tk.Label(self.stats_frame, text=self.get_status_text(), 
                                   font=("Courier", 12), bg="#34495e", fg="#ecf0f1", justify="left")
        self.info_label.pack()

        # Input Section
        tk.Label(root, text="Enter Sale Quantity:", bg="#2c3e50", fg="white").pack(pady=(20,0))
        self.qty_entry = tk.Entry(root, font=("Arial", 12), width=10)
        self.qty_entry.pack(pady=5)

        # Buttons
        self.btn_process = tk.Button(root, text="Process Transaction", 
                                     command=self.handle_transaction, 
                                     bg="#27ae60", fg="white", font=("Arial", 10, "bold"),
                                     padx=10, pady=5)
        self.btn_process.pack(pady=20)

    def get_status_text(self):
        # Display the status of the currently selected product
        current_product = next(p for p in self.products if p.name == self.selected_product.get())
        return f"Product: {current_product.name}\nStock:   {current_product.stock}\nStatus:  {current_product.status}"

    def update_display(self):
        # Update dashboard info when product selection changes
        self.info_label.config(text=self.get_status_text())

    def handle_transaction(self):
        try:
            qty = int(self.qty_entry.get())
            current_product = next(p for p in self.products if p.name == self.selected_product.get())
            
            # Process the transaction
            result = self.manager.process_transaction(current_product, qty)
            
            # Update the UI
            self.update_display()
            
            # Show pop-up feedback
            if "Success" in result:
                messagebox.showinfo("System Success", result)
            else:
                messagebox.showwarning("Validation Error", result)
            
            self.qty_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a whole number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()