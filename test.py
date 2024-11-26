import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie oczyszczonego zestawu danych
df = pd.read_csv('data/cleaned_data.csv')

# Odtworzenie kolumny 'City', jeśli jej nie ma
city_columns = [col for col in df.columns if 'City_' in col]
if 'City' not in df.columns:
    def get_city(row):
        for col in city_columns:
            if row[col] == 1:
                return col.replace('City_', '')
        return 'Other'


    df['City'] = df.apply(get_city, axis=1)

# Odtworzenie kolumny 'Furnishing Status', jeśli jej nie ma
furnishing_columns = [col for col in df.columns if 'Furnishing Status_' in col]
if 'Furnishing Status' not in df.columns:
    def get_furnishing_status(row):
        for col in furnishing_columns:
            if row[col] == 1:
                return col.replace('Furnishing Status_', '')
        return 'Furnished'


    df['Furnishing Status'] = df.apply(get_furnishing_status, axis=1)

# Odtworzenie kolumny 'Tenant Preferred', jeśli jej nie ma
tenant_columns = [col for col in df.columns if 'Tenant Preferred_' in col]
if 'Tenant Preferred' not in df.columns:
    def get_tenant_preferred(row):
        for col in tenant_columns:
            if row[col] == 1:
                return col.replace('Tenant Preferred_', '')
        return 'Bachelors'


    df['Tenant Preferred'] = df.apply(get_tenant_preferred, axis=1)


# Funkcja do generowania obserwacji dla zmiennej docelowej (czynsz)
def generate_rent_observations(df):
    rent_stats = df['Rent'].describe()
    rent_median = df['Rent'].median()

    observations = []
    observations.append(f"Czynsz wynosi średnio {rent_stats['mean']:.2f} INR z medianą {rent_median:.2f} INR.")
    observations.append(
        f"Minimalny czynsz wynosi {rent_stats['min']:.2f} INR, a maksymalny {rent_stats['max']:.2f} INR.")
    observations.append(
        f"Większość czynszów znajduje się w zakresie od {rent_stats['25%']:.2f} do {rent_stats['75%']:.2f} INR.")

    return observations


# Funkcja do generowania obserwacji dla cech numerycznych
def generate_numeric_feature_observations(df, features):
    observations = []
    for feature in features:
        stats = df[feature].describe()
        observations.append(
            f"Cecha {feature}: średnia wartość wynosi {stats['mean']:.2f}, a mediana {df[feature].median():.2f}.")
        observations.append(f"Zakres wartości cechy {feature}: od {stats['min']:.2f} do {stats['max']:.2f}.")
    return observations


# Funkcja do generowania obserwacji dla cech kategorycznych
def generate_categorical_feature_observations(df, category_col, target_col):
    grouped = df.groupby(category_col)[target_col].median().sort_values()
    observations = [f"Wartości mediany czynszu dla {category_col}: "]
    for category, median_value in grouped.items():
        observations.append(f"{category}: {median_value:.2f} INR")
    return observations


# Przykładowe zastosowanie
numeric_features = ['Size', 'Floor Level', 'Total Floors', 'BHK', 'Bathroom']

# Generowanie i wyświetlanie obserwacji
print("=== Obserwacje dla czynszu ===")
print("\n".join(generate_rent_observations(df)))

print("\n=== Obserwacje dla cech numerycznych ===")
print("\n".join(generate_numeric_feature_observations(df, numeric_features)))

print("\n=== Obserwacje dla cechy 'City' ===")
print("\n".join(generate_categorical_feature_observations(df, 'City', 'Rent')))

print("\n=== Obserwacje dla cechy 'Furnishing Status' ===")
print("\n".join(generate_categorical_feature_observations(df, 'Furnishing Status', 'Rent')))

print("\n=== Obserwacje dla cechy 'Tenant Preferred' ===")
print("\n".join(generate_categorical_feature_observations(df, 'Tenant Preferred', 'Rent')))
