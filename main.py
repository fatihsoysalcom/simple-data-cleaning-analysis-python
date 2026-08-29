import collections

# Simulate raw data, similar to what you might find in an Excel sheet
# with inconsistencies and potential errors.
raw_sales_data = [
    {"product": "Laptop", "quantity": "2", "price": "1200.50"},
    {"product": "Mouse", "quantity": "5", "price": "25.00"},
    {"product": "Keyboard", "quantity": "1", "price": "75.99"},
    {"product": "Laptop ", "quantity": "1", "price": "1200.50"}, # Inconsistent product name (whitespace)
    {"product": "Monitor", "quantity": "3", "price": "250.00"},
    {"product": "Mouse", "quantity": "N/A", "price": "25.00"}, # Invalid quantity
    {"product": "Keyboard", "quantity": "2", "price": ""},     # Missing price
    {"product": "laptop", "quantity": "1", "price": "1200.50"}, # Inconsistent product name (case)
    {"product": "Webcam", "quantity": "1", "price": "50.00"},
    {"product": "Mouse", "quantity": "3", "price": "25.00"},
]

cleaned_data = []

# --- Data Cleaning Phase ---
print("--- Data Cleaning ---")
for i, record in enumerate(raw_sales_data):
    # Standardize product names by stripping whitespace and converting to lowercase
    # (Excel equivalent: TRIM() and LOWER() functions)
    product = record.get("product", "").strip().lower()
    
    # Handle quantity: convert to integer, defaulting to 0 if the value is invalid or missing
    # (Excel equivalent: IFERROR(VALUE(cell), 0) or similar logic)
    quantity_str = record.get("quantity", "0").strip()
    try:
        quantity = int(float(quantity_str)) # Use float first to handle "2.0" or similar string formats
    except ValueError:
        quantity = 0
    
    # Handle price: convert to float, defaulting to 0.0 if the value is invalid or missing
    # (Excel equivalent: IFERROR(VALUE(cell), 0.0) or similar logic)
    price_str = record.get("price", "0.0").strip()
    try:
        price = float(price_str)
    except ValueError:
        price = 0.0
        
    # Calculate total for the row
    # (Excel equivalent: a simple cell multiplication formula like =C2*D2)
    total_sale = quantity * price

    cleaned_data.append({
        "product": product,
        "quantity": quantity,
        "price": price,
        "total_sale": total_sale
    })
    print(f"Record {i+1}: Original Product='{record.get('product')}', Cleaned Product='{product}', Quantity={quantity}, Price={price:.2f}, Total={total_sale:.2f}")

# --- Data Analysis Phase ---
print("\n--- Data Analysis ---")

# Calculate total revenue from the cleaned data
# (Excel equivalent: SUM() function on a column)
total_revenue = sum(item["total_sale"] for item in cleaned_data)

# Calculate average sale value per record
# (Excel equivalent: AVERAGE() function)
average_sale_value = total_revenue / len(cleaned_data) if cleaned_data else 0

# Aggregate sales and quantities by product
# (Excel equivalent: Pivot Table or SUMIF() functions)
product_sales = collections.defaultdict(float)
product_quantities = collections.defaultdict(int)

for item in cleaned_data:
    product_sales[item["product"]] += item["total_sale"]
    product_quantities[item["product"]] += item["quantity"]

print(f"\nTotal Revenue: ${total_revenue:.2f}")
print(f"Average Sale Value per Record: ${average_sale_value:.2f}")

print("\nSales Summary by Product:")
for product, total_sale in sorted(product_sales.items()):
    quantity_sold = product_quantities[product]
    print(f"- {product.capitalize()}: Total Sales = ${total_sale:.2f}, Total Quantity = {quantity_sold}")
