import yfinance as yf
import pandas as pd
import os

def descargar_datos(tickers, start_date='2020-01-01', end_date='2024-01-01', save_path='data'):
    """Descarga datos históricos de acciones y los guarda en archivos CSV."""
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    for ticker in tickers:
        print(f'Descargando datos para {ticker}...')
        data = yf.download(ticker, start=start_date, end=end_date)
        
        if not data.empty:
            file_path = os.path.join(save_path, f'{ticker}.csv')
            data.to_csv(file_path)
            print(f'Datos guardados en {file_path}')
        else:
            print(f'No se encontraron datos para {ticker}')

# Ejemplo de uso
tickers = ['AAPL', 'MSFT', 'GOOGL']  # Puedes modificar esta lista con las acciones que quieras
descargar_datos(tickers)
 
