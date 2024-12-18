import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

# Function to handle the form submission and prediction
def submit_data():
    try:
        # Collect input values
        bathrooms = float(bathrooms_entry.get())
        area = float(area_entry.get())
        rooms = float(rooms_entry.get())
        construction_status = construction_var.get()
        furnishing_status = furnishing_var.get()
        ownership_status = ownership_var.get()
        city = city_var.get()
        property_type = property_type_var.get()

        # Initialize the feature vector with zeros
        feature_vector = [0] * 26

        # Assign input values to the corresponding feature indices
        feature_vector[0] = rooms  # Rooms
        feature_vector[1] = bathrooms  # Bathrooms
        feature_vector[2] = area  # Area

        # Building status (binary values)
        feature_vector[3] = 1 if construction_status == "Ready" else 0  # Ready
        feature_vector[4] = 1 if construction_status == "Under Construction" else 0  # Under Construction

        # Furnishing status (binary values)
        feature_vector[5] = 1 if furnishing_status == "Furnished" else 0  # Furnished
        feature_vector[6] = 1 if furnishing_status == "Unfurnished" else 0  # Unfurnished

        # Ownership status (binary values)
        feature_vector[7] = 1 if ownership_status == "First Residence" else 0  # First Residence
        feature_vector[8] = 1 if ownership_status == "Resale" else 0  # Resale

        # Property type (12 categories, map each to binary values)
        property_type_map = [
            "Apartment", "Cabin", "Chalet", "Duplex", "E-Villa",
            "Hotel Apartment", "Other Residential", "Penthouse",
            "Residential Land", "Room", "Townhouse", "Twin House", "Villa"
        ]
        if property_type in property_type_map:
            property_index = property_type_map.index(property_type) + 9  # Offset by 9 (start from index 9)
            feature_vector[property_index] = 1

        # City (Cairo, Alexandria, Other - encoded as binary values)
        if city == "Cairo":
            feature_vector[22] = 1  # Cairo
        elif city == "Alexandria":
            feature_vector[23] = 1  # Alexandria
        else:
            feature_vector[24] = 1  # Other City

        # Convert the feature vector to a NumPy array and reshape it for prediction
        feature_vector = np.array(feature_vector).reshape(1, -1)

        # Make the prediction
        predicted_price = model.predict(feature_vector)[0]
        messagebox.showinfo("Predicted Price", f"The predicted house price is: {predicted_price:.2f} EGP")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Rooms, Bathrooms, and Area.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("House Pricing Prediction")
root.geometry("800x700")
root.config(bg="#2c3e50")

# Title label with modern font and styling
title_label = ttk.Label(root, text="House Pricing Prediction", font=("Helvetica", 24, "bold"), foreground="#ecf0f1", background="#2c3e50")
title_label.pack(pady=30)

# Frame for form fields with modern styling
form_frame = tk.Frame(root, bg="#34495e", bd=5, relief="solid")
form_frame.pack(pady=20, padx=40, fill="both", expand=True)

# Styling the labels and entry fields
def style_label(label_text, row, col):
    label = ttk.Label(form_frame, text=label_text, font=("Arial", 12), foreground="#ecf0f1", background="#34495e")
    label.grid(row=row, column=col, pady=10, padx=10, sticky="w")

def style_entry():
    entry = ttk.Entry(form_frame, font=("Arial", 12))
    return entry

style_label("Number of Bathrooms:", 0, 0)
bathrooms_entry = style_entry()
bathrooms_entry.grid(row=0, column=1, pady=10, padx=10)

style_label("Area (sq ft):", 1, 0)
area_entry = style_entry()
area_entry.grid(row=1, column=1, pady=10, padx=10)

style_label("Number of Rooms:", 2, 0)
rooms_entry = style_entry()
rooms_entry.grid(row=2, column=1, pady=10, padx=10)

# Drop-down for "Construction Status"
style_label("Construction Status:", 3, 0)
construction_var = tk.StringVar()
construction_status_menu = ttk.Combobox(form_frame, textvariable=construction_var, state="readonly", font=("Arial", 12), width=18)
construction_status_menu["values"] = ["Ready", "Under Construction"]
construction_status_menu.grid(row=3, column=1, pady=10, padx=10)

# Drop-down for "Furnishing Status"
style_label("Furnishing Status:", 4, 0)
furnishing_var = tk.StringVar()
furnishing_menu = ttk.Combobox(form_frame, textvariable=furnishing_var, state="readonly", font=("Arial", 12), width=18)
furnishing_menu["values"] = ["Furnished", "Unfurnished"]
furnishing_menu.grid(row=4, column=1, pady=10, padx=10)

# Drop-down for "Ownership Status"
style_label("Ownership Status:", 5, 0)
ownership_var = tk.StringVar()
ownership_menu = ttk.Combobox(form_frame, textvariable=ownership_var, state="readonly", font=("Arial", 12), width=18)
ownership_menu["values"] = ["First Residence", "Resale"]
ownership_menu.grid(row=5, column=1, pady=10, padx=10)

# Drop-down for "City"
style_label("City:", 6, 0)
city_var = tk.StringVar()
city_menu = ttk.Combobox(form_frame, textvariable=city_var, state="readonly", font=("Arial", 12), width=18)
city_menu["values"] = ["Cairo", "Alexandria", "Other"]
city_menu.grid(row=6, column=1, pady=10, padx=10)

# Drop-down for "Property Type"
style_label("Property Type:", 7, 0)
property_type_var = tk.StringVar()
property_type_menu = ttk.Combobox(form_frame, textvariable=property_type_var, state="readonly", font=("Arial", 12), width=18)
property_type_menu["values"] = [
    "Apartment", "Cabin", "Chalet", "Duplex", "E-Villa",
    "Hotel Apartment", "Other Residential", "Penthouse",
    "Residential Land", "Room", "Townhouse", "Twin House", "Villa"
]
property_type_menu.grid(row=7, column=1, pady=10, padx=10)

# Submit Button with modern design
submit_button = ttk.Button(root, text="Predict Price", command=submit_data)
submit_button.pack(pady=30)

# Apply styling with ttk.Style
style = ttk.Style()

# Define the style for the button
style.configure("TButton",
                font=("Arial", 14),
                padding=10,
                background="#1abc9c",
                foreground="white")

# Hover effect for the button
style.map("TButton",
          foreground=[('pressed', 'white'), ('active', 'black')],
          background=[('pressed', '#16a085'), ('active', '#1abc9c')])

# Run the application
root.mainloop()

