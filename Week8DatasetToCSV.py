import pandas as pd

# Define synthetic Indian retail sales data
data = {
    "OrderID": list(range(1001, 1021)),
    "Product": ["Laptop", "Smartphone", "Jeans", "LED TV", "Kurta", "Washing Machine", "Mixer Grinder", "Sports Shoes",
                "Microwave", "Earphones", "Refrigerator", "Sandals", "Tablet", "Hoodie", "Air Fryer", "Chappal",
                "Smartwatch", "Saree", "Jacket", "Toaster"],
    "Category": ["Electronics", "Electronics", "Clothing", "Electronics", "Clothing", "Appliances", "Appliances", 
                 "Footwear", "Appliances", "Electronics", "Appliances", "Footwear", "Electronics", "Clothing",
                 "Appliances", "Footwear", "Electronics", "Clothing", "Clothing", "Appliances"],
    "Quantity": [1, 2, 3, 1, 4, 1, 2, 2, 1, 3, 1, 2, 2, 1, 2, 1, 2, 3, 1, 2],
    "PricePerUnit": [60000, 20000, 1500, 45000, 800, 25000, 3000, 4000, 10000, 1500, 55000, 1200, 25000, 2000, 7000, 
                     500, 7000, 2500, 3500, 2000],
    "TotalPrice": [60000, 40000, 4500, 45000, 3200, 25000, 6000, 8000, 10000, 4500, 55000, 2400, 50000, 2000, 14000, 
                   500, 14000, 7500, 3500, 4000],
    "Date": pd.date_range(start="2024-01-01", periods=20, freq='D').strftime("%Y-%m-%d").tolist(),
    "CustomerID": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010", 
                   "C011", "C012", "C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"],
    "City": ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Lucknow",
             "Surat", "Nagpur", "Indore", "Bhopal", "Vadodara", "Ludhiana", "Patna", "Kanpur", "Kochi", "Nashik"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("Week8_sales_data_india.csv", index=False)  # index = False will prevent pandas from writing the DataFrame’s index (the row labels) to the CSV file 

print("Indian retail sales dataset saved as 'sales_data_india.csv'")
