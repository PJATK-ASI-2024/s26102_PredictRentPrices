import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
df = pd.read_csv('data/cleaned_data.csv')

# Statystyki opisowe
print(df['Rent'].describe())

# Obliczenie 99 percentyla
upper_limit = df['Rent'].quantile(0.99)

# Filtrowanie danych
df_filtered = df[df['Rent'] <= upper_limit]

# Histogram po usunięciu wartości odstających
plt.figure(figsize=(10,6))
sns.histplot(df_filtered['Rent'], bins=50, kde=True)
plt.title('Rozkład czynszu po usunięciu wartości odstających')
plt.xlabel('Czynsz (INR)')
plt.ylabel('Liczba nieruchomości')
plt.show()

# Transformacja logarytmiczna
df['Rent_Log'] = np.log1p(df['Rent'])

# Histogram z transformacją logarytmiczną
plt.figure(figsize=(10,6))
sns.histplot(df['Rent_Log'], bins=50, kde=True)
plt.title('Rozkład logarytmiczny czynszu')
plt.xlabel('Log(Czynsz)')
plt.ylabel('Liczba nieruchomości')
plt.show()

# Histogram z zastosowaniem skali logarytmicznej
plt.figure(figsize=(10,6))
sns.histplot(df['Rent'], bins=50, kde=True)
plt.title('Rozkład czynszu (skala logarytmiczna)')
plt.xlabel('Czynsz (INR)')
plt.ylabel('Liczba nieruchomości')
plt.xscale('log')
plt.show()
