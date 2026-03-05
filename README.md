# Retail Inventory Subsystem
**Course:** SE102: Software Engineering 2
**Assessment:** Practical Activity Assessment 1 — Demonstrating a Working Subsystem
**Student:** Jane Rio Dela Torre,Justine Duenas, Eric John Borro
**Repository:** https://github.com/janeally/Inventory-Subsystem-SE102.git

---

## Project Overview
A functional retail inventory subsystem built with Python that manages product stock and processes sale transactions. It ensures data integrity by validating sale quantities, preventing over-selling and invalid inputs, and automatically updating product status when stock is depleted. A tkinter GUI provides an interactive interface for selecting products and processing transactions in real time.

---

## Project Structure
```
InventorySubsystem/
│── src/
│   ├── __init__.py
│   ├── inventory_manager.py
│   ├── main.py
│   ├── product.py
│   └── validator.py
│── test/
│   └── test_inventory.py
│── .gitignore
└── README.md
```

---

## Environment Setup
| Tool | Version |
|------|---------|
| Language | Python 3.13.0 |
| IDE | Visual Studio Code |
| Testing Framework | PyTest 9.0.2 |
| GUI Library | tkinter (built-in) |
| Version Control | Git |
| OS | Windows 10 |

---

## How to Run

**Run the GUI application** (from inside the `src/` folder):
```bash
cd src
python main.py
```

**Run unit tests** (from the project root):
```bash
python -m pytest
```

> **Note:** Always run `main.py` from inside `src/` to avoid import errors. Tests must be run from the project root so Python can resolve the `src` package correctly.

---

## Core Classes
- **`Product`** — represents a product with `product_id`, `name`, `stock`, and `status` (`In Stock` / `Out of Stock`)
- **`StockValidator`** — validates sale quantities; rejects zero, negative, or over-stock amounts
- **`InventoryManager`** — processes transactions using `StockValidator` and updates `Product` state
- **`InventoryGUI`** — tkinter interface for selecting products, entering quantities, and viewing results

---

## Testing Strategy
- **Black-box Testing:** Validates outputs for valid and invalid sale transactions without depending on internal implementation
- **White-box Testing:** Verifies internal state changes — stock values and status fields after each transaction
- **TDD Cycle:** Followed the Red-Green-Refactor workflow — wrote failing tests first, implemented logic, then confirmed passing

### Test Results
| Test | Description | Result |
|------|-------------|--------|
| `test_successful_sale` | Deducts stock on valid transaction | ✅ Passed |
| `test_insufficient_stock` | Rejects sale exceeding available stock | ✅ Passed |
| `test_out_of_stock_status` | Updates status to `Out of Stock` at zero stock | ✅ Passed |

**3 / 3 passed — 0.03s**
