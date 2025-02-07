import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def analizar_datos(ticker, data_path='data'):
    """Carga los datos de un ticker, realiza análisis exploratorio y muestra gráficos."""
    
    file_path = os.path.join(data_path, f'{ticker}.csv')
    
    if not os.path.exists(file_path):
        print(f'No se encontró el archivo {file_path}')
        return
    
    # Cargar datos correctamente
    data = pd.read_csv(file_path, index_col=0, parse_dates=True, skiprows=1)
    data.columns = ['Close', 'High', 'Low', 'Open', 'Volume']  # Renombrar columnas
    
    # Calcular medias móviles
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()

    # Calcular retornos logarítmicos
    data['Returns'] = data['Close'].pct_change()

    print("Primeras filas del dataset:")
    print(data.head())  # Verifica que la fecha sea el índice correcto

    # Gráfico del precio de cierre con medias móviles
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['Close'], label='Precio de Cierre', color='blue')
    plt.plot(data.index, data['SMA_50'], label='SMA 50', color='orange', linestyle='dashed')
    plt.plot(data.index, data['SMA_200'], label='SMA 200', color='red', linestyle='dashed')
    plt.title(f'Precio de Cierre y Medias Móviles - {ticker}')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.grid()
    plt.show()

    # Histograma de los retornos
    plt.figure(figsize=(8,5))
    sns.histplot(data['Returns'].dropna(), bins=50, kde=True)
    plt.title(f'Distribución de Retornos - {ticker}')
    plt.xlabel('Retorno')
    plt.ylabel('Frecuencia')
    plt.grid()
    plt.show()

# Ejecutar análisis
analizar_datos('AAPL')
