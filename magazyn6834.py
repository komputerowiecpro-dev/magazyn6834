class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product_name):
        if product_name and product_name not in self.products:
            self.products.append(product_name)
            return True
        return False

    def remove_product(self, product_name):
        if product_name in self.products:
            self.products.remove(product_name)
            return True
        return False

    def get_products(self):
        return self.products
      mport streamlit as st
from inventory_manager import InventoryManager

# Inicjalizacja menedżera magazynu w sesji Streamlit
if 'inventory_manager' not in st.session_state:
    st.session_state.inventory_manager = InventoryManager()

manager = st.session_state.inventory_manager

st.title("Prosta Aplikacja Magazynowa")

st.header("Dodaj Produkt")
product_to_add = st.text_input("Nazwa produktu do dodania", key="add_input")
if st.button("Dodaj Produkt"):
    if manager.add_product(product_to_add):
        st.success(f"'{product_to_add}' został dodany do magazynu.")
        st.session_state.add_input = "" # Czyści pole tekstowe
    else:
        st.warning(f"Produkt '{product_to_add}' już istnieje lub nazwa jest pusta.")

st.header("Usuń Produkt")
product_to_remove = st.text_input("Nazwa produktu do usunięcia", key="remove_input")
if st.button("Usuń Produkt"):
    if manager.remove_product(product_to_remove):
        st.success(f"'{product_to_remove}' został usunięty z magazynu.")
        st.session_state.remove_input = "" # Czyści pole tekstowe
    else:
        st.error(f"Produkt '{product_to_remove}' nie znaleziono w magazynie.")

st.header("Aktualny Stan Magazynu")
products = manager.get_products()
if products:
    for product in products:
        st.write(f"- {product}")
else:
    st.info("Magazyn jest pusty.")
