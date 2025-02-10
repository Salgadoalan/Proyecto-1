import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar dataset
file_path = "../data/AAPL.csv"
data = pd.read_csv(file_path, index_col=0, parse_dates=True, skiprows=1)

# Asegurar que las columnas sean numéricas
data = data.apply(pd.to_numeric, errors='coerce')

# Definir variables predictoras (X) y variable objetivo (y)
X = data[['Open', 'High', 'Low', 'Volume']]  # Variables de entrada
y = data['Close']  # Variable a predecir

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
