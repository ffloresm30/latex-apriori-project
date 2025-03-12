import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder

# Ejemplo base de datos
transactions = [['manzana', 'plátano'],
                ['manzana', 'zanahoria', 'limón'],
                ['manzana', 'plátano', 'zanahoria'],
                ['plátano', 'limón'],
                ['manzana', 'plátano', 'zanahoria']]

# Paso 1: Codificar las transacciones en formato binario
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_array, columns=te.columns_)

print("Matriz binaria de las transacciones:")
print(df)

# Paso 2: Generar los conjuntos frecuentes utilizando Apriori
min_support = 0.3  # Soporte mínimo
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)

print("\nConjuntos frecuentes generados:")
print(frequent_itemsets)

# Paso 3: Generar reglas de asociación a partir de los conjuntos frecuentes
min_confidence = 0.5
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

print("\nReglas de asociación generadas (con confianza mínima):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Filtrar reglas con lift >= 1.0
filtered_rules = rules[rules['lift'] >= 1.0]

print("\nReglas filtradas (lift >= 1.0):")
print(filtered_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
