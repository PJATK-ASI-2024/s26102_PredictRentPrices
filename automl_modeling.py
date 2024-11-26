# automl_modeling.py

# Import niezbędnych bibliotek
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport


def main():
    try:
        # Wczytaj oczyszczone dane
        df = pd.read_csv('data/cleaned_data_no_outliers.csv')

        # Wygeneruj raport profilowania
        profile = ProfileReport(df, title="Raport Profilowania", explorative=True)

        # Zapisz raport do pliku HTML
        profile.to_file("raport_profilowania.html")

        print("Raport został wygenerowany i zapisany jako 'raport_profilowania.html'.")

    except Exception as e:
        print("Wystąpił błąd podczas generowania raportu:")
        print(e)


if __name__ == "__main__":
    main()
