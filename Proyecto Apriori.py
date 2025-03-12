import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Cargar los datos desde los archivos CSV
import pandas as pd

# URLs de los archivos
url_products = "https://github.com/it-ces/Rules-puj/blob/main/products.csv?raw=true"
url_orders = "https://github.com/it-ces/Rules-puj/blob/main/order_products__train.csv?raw=true"

# Cargar los datos
products = pd.read_csv(url_products)
orders = pd.read_csv(url_orders)

# EDA 
print("Productos:")
print(products.head())

print("\nÓrdenes:")
print(orders.head())
print(products.info())
print(orders.info())

#Haciendo merge en los datos 
merged = orders.merge(products, on="product_id", how="inner")
print(merged.head())

transactions = merged.groupby("order_id")["product_name"].apply(list).tolist()
print(transactions[:5]) 

# 4. Codificar las transacciones a formato binario
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_array, columns=te.columns_)
print(df.head())

min_support = 0.01  # Soporte mínimo (porcentaje de transacciones)
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
print("\nConjuntos frecuentes encontrados:")
print(frequent_itemsets.head())

min_confidence = 0.3  # Umbral mínimo de confianza
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
print("\nReglas de asociación generadas (primeras filas):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())

#Filtrar las reglas por lift (opcional)
filtered_rules = rules[rules['lift'] >= 1.0]
print("\nReglas filtradas (lift >= 1.0):")
print(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
