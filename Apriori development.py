
# Ejemplo base de datos para verificar cómo trabaja el algoritmo Apriori

# Tenemos las facturas con las siguientes transacciones:
# Ejemplo base de datos para verificar cómo trabaja el algoritmo Apriori
transactions = [['manzana', 'plátano'],
                ['manzana', 'zanahoria', 'limón'],
                ['manzana', 'plátano', 'zanahoria'],
                ['plátano', 'limón'],
                ['manzana', 'plátano', 'zanahoria']]

# Función para contar transacciones
def count_transactions(itemset, transactions):
    count = 0
    for transaction in transactions:
        match = True
        for item in itemset:
            if item not in transaction:  # Si algún ítem no está, no es un match
                match = False
                break
        if match:
            count += 1
    return count  # Retornar el conteo

# Crear lista de productos únicos
all_items = []
for transaction in transactions:
    for item in transaction:
        if item not in all_items:
            all_items.append(item)
print("Productos únicos:", all_items)

# Definir umbrales mínimos
min_support = 0.3       # Porcentaje mínimo de transacciones
min_confidence = 0.5    # Probabilidad condicional mínima
min_lift = 1.0          # Relación mínima significativa

# Número total de transacciones
total_transactions = len(transactions)

# Función para generar combinaciones de un tamaño dado
def generate_combinations(items, size):
    combinations = []
    n = len(items)
    if size == 2:  # Generar pares
        for i in range(n):
            for j in range(i + 1, n):
                combinations.append([items[i], items[j]])
    elif size == 3:  # Generar tripletas
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    combinations.append([items[i], items[j], items[k]])
    return combinations

# Calcular reglas para diferentes tamaños
print("\nResultados del Algoritmo Apriori (Pares y Tripletas Filtradas):\n")

# Iterar sobre pares (tamaño 2) y tripletas (tamaño 3)
for size in [2, 3]:
    combinations = generate_combinations(all_items, size)
    for combination in combinations:
        antecedent = combination[:-1]  # Todo menos el último elemento como antecedente
        consequent = [combination[-1]]  # El último elemento como consecuente

        # Contar transacciones
        count_antecedent = count_transactions(antecedent, transactions)
        count_consequent = count_transactions(consequent, transactions)
        count_both = count_transactions(antecedent + consequent, transactions)

        # Calcular métricas
        support = count_both / total_transactions if total_transactions > 0 else 0
        confidence = count_both / count_antecedent if count_antecedent > 0 else 0
        lift = confidence / (count_consequent / total_transactions) if count_consequent > 0 else 0

        # Aplicar filtros de umbral
        if support >= min_support and confidence >= min_confidence and lift >= min_lift:
            # Mostrar solo las reglas que cumplen con los umbrales
            print(f"Regla: {antecedent} → {consequent}")
            print(f"  Soporte: {support:.2f}")
            print(f"  Confianza: {confidence:.2f}")
            print(f"  Lift: {lift:.2f}")
            print("-" * 40)
