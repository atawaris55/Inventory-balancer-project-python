import streamlit as st
import json
from pathlib import Path

# ---------- Configuration ----------
DATABASE = "data.json"

# ---------- Load Data ----------
def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)

data = load_data()

# ---------- Helper ----------
def find_item(name):
    for item in data:
        if item["name"].lower() == name.lower():
            return item
    return None

# ---------- UI ----------
st.title("📦 Inventory Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Item", "View Items", "Update Item", "Delete Item"]
)

# ---------- Add Item ----------
if menu == "Add Item":
    st.subheader("Add New Item")

    name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    price = st.number_input("Price", min_value=0.0, step=0.1)
    category = st.selectbox(
        "Category",
        ["Electronics", "Clothing", "Food", "Books", "Grocery", "Other"]
    )

    if st.button("Add Item"):
        existing = find_item(name)

        if existing:
            existing["quantity"] += quantity
            st.success("Item already exists. Quantity updated!")
        else:
            data.append({
                "name": name,
                "quantity": quantity,
                "price": price,
                "category": category
            })
            st.success("Item added successfully!")

        save_data(data)

# ---------- View Items ----------
elif menu == "View Items":
    st.subheader("Inventory Items")

    if data:
        st.table(data)
    else:
        st.warning("No items found in inventory.")

# ---------- Update Item ----------
elif menu == "Update Item":
    st.subheader("Update Item")

    item_names = [item["name"] for item in data]

    if item_names:
        selected_name = st.selectbox("Select Item", item_names)
        item = find_item(selected_name)

        new_quantity = st.number_input(
            "New Quantity", value=item["quantity"], step=1
        )
        new_price = st.number_input(
            "New Price", value=item["price"], step=0.1
        )
        new_category = st.selectbox(
            "New Category",
            ["Electronics", "Clothing", "Food", "Books", "Grocery", "Other"],
            index=["Electronics", "Clothing", "Food", "Books", "Grocery", "Other"].index(item["category"])
        )

        if st.button("Update Item"):
            item["quantity"] = new_quantity
            item["price"] = new_price
            item["category"] = new_category
            save_data(data)
            st.success("Item updated successfully!")

    else:
        st.warning("No items available to update.")

# ---------- Delete Item ----------
elif menu == "Delete Item":
    st.subheader("Delete Item")

    item_names = [item["name"] for item in data]

    if item_names:
        selected_name = st.selectbox("Select Item to Delete", item_names)

        if st.button("Delete Item"):
            item = find_item(selected_name)
            data.remove(item)
            save_data(data)
            st.success("Item deleted successfully!")

    else:
        st.warning("No items available to delete.")
