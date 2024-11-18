
# PredictRentPrices

## Spis treści

-   [Opis projektu](#opis-projektu)
-   [Problem biznesowy](#problem-biznesowy)
-   [Cel projektu](#cel-projektu)
-   [Źródło danych](#%C5%BAr%C3%B3d%C5%82o-danych)
-   [Charakterystyka danych](#charakterystyka-danych)
-   [Uzasadnienie wyboru zbioru danych](#uzasadnienie-wyboru-zbioru-danych)
-   [Struktura projektu](#struktura-projektu)
-   [Plan pracy](#plan-pracy)
-   [Wymagania techniczne](#wymagania-techniczne)
-   [Autor](#autor)
----------

## Opis projektu

Projekt **PredictRentPrices** ma na celu stworzenie modelu uczenia maszynowego, który przewiduje miesięczny czynsz za wynajem mieszkania na podstawie różnych cech nieruchomości. Dzięki temu narzędziu zarówno najemcy, jak i właściciele będą mogli lepiej zrozumieć rynek i podejmować bardziej świadome decyzje.

## Problem biznesowy

Rynek nieruchomości jest dynamiczny i skomplikowany. Wiele osób ma trudności z oszacowaniem odpowiedniej ceny wynajmu mieszkania, co może prowadzić do nieoptymalnych decyzji finansowych:

-   **Najemcy** mogą przepłacać za wynajem lub tracić okazje przez niedoszacowanie wartości.
-   **Właściciele** mogą ustalać niewłaściwe ceny, co skutkuje dłuższym czasem oczekiwania na najemcę lub utratą potencjalnych zysków.

Stworzenie modelu przewidującego ceny wynajmu pomoże zminimalizować te problemy, dostarczając dokładnych i opartych na danych prognoz.

## Cel projektu

-   **Główny cel**: Zbudowanie dokładnego modelu predykcyjnego do przewidywania miesięcznych czynszów za wynajem mieszkań.
-   **Cele szczegółowe**:
    -   Analiza i przetworzenie dostępnych danych dotyczących wynajmu nieruchomości.
    -   Identyfikacja kluczowych czynników wpływających na cenę wynajmu.
    -   Walidacja i optymalizacja modelu w celu osiągnięcia jak najlepszych wyników.

## Źródło danych

-   **Zbiór danych**: House Rent Dataset
-   **Autor**: Sourav Banerjee
-   **Opis**: Zbiór zawiera informacje o ponad 4700 nieruchomościach dostępnych do wynajęcia w Indiach, w tym takie cechy jak liczba pokoi, powierzchnia, lokalizacja, stan umeblowania i preferencje najemców.

## Charakterystyka danych

-   **Liczba rekordów**: 4 735
-   **Liczba cech**: 12
-   **Główne cechy**:
    -   `Posted On`: Data dodania ogłoszenia.
    -   `BHK`: Liczba sypialni, salonów i kuchni.
    -   `Rent`: Miesięczny czynsz (zmienna docelowa).
    -   `Size`: Powierzchnia w stopach kwadratowych.
    -   `Floor`: Piętro mieszkania i łączna liczba pięter w budynku.
    -   `Area Type`: Typ powierzchni (Super Area, Carpet Area, Build Area).
    -   `Area Locality`: Lokalizacja nieruchomości.
    -   `City`: Miasto.
    -   `Furnishing Status`: Stan umeblowania (Umeblowane, Częściowo umeblowane, Nieumeblowane).
    -   `Tenant Preferred`: Preferowany typ najemcy.
    -   `Bathroom`: Liczba łazienek.
    -   `Point of Contact`: Osoba kontaktowa (agencja, właściciel).

## Uzasadnienie wyboru zbioru danych

-   **Kompletność danych**: Zbiór spełnia wymagania dotyczące liczby rekordów (ponad 2000) i zawiera kluczowe cechy wpływające na cenę wynajmu.
-   **Różnorodność cech**: Dane obejmują zarówno cechy numeryczne, jak i kategoryczne, co pozwala na wszechstronną analizę i modelowanie.
-   **Aktualność**: Dane są stosunkowo aktualne i odzwierciedlają obecne trendy na rynku nieruchomości w Indiach.
-   **Przydatność**: Wyniki projektu mogą mieć praktyczne zastosowanie i dostarczyć wartościowych informacji dla zainteresowanych stron.

## Struktura projektu

1.  **Przetwarzanie danych**
    
    -   Wczytanie i wstępne czyszczenie danych.
    -   Analiza brakujących wartości i outlierów.
    -   Kodowanie zmiennych kategorycznych.
2.  **Eksploracyjna analiza danych (EDA)**
    
    -   Analiza statystyczna cech.
    -   Wizualizacje danych (histogramy, wykresy korelacji).
3.  **Trenowanie modelu**
    
    -   Podział danych na zbiory treningowy i testowy (70/30).
    -   Wybór i trenowanie modeli regresyjnych (np. regresja liniowa, Random Forest).
    -   Optymalizacja hiperparametrów.
4.  **Walidacja i testowanie**
    
    -   Ocena modelu na zbiorze testowym.
    -   Obliczenie metryk (MSE, RMSE, MAE, R²).
5.  **Dokształcanie modelu**
    
    -   Dalsza optymalizacja na podstawie wyników.
    -   Walidacja krzyżowa.
6.  **Publikacja i wdrożenie**
    
    -   Przygotowanie modelu do wdrożenia (np. jako API).
    -   Dokumentacja techniczna.
7.  **Prezentacja i raport końcowy**
    
    -   Przygotowanie prezentacji wyników.
    -   Sporządzenie raportu podsumowującego.

## Plan pracy**
| Etap | Zadania | Tydzień | Estymowany czas |
|--|--|--|--|
|Przetwarzanie danych|Wczytanie danych, Czyszczenie danych, Kodowanie zmiennych|1| 1 dzień|
|Eksporacja danych (EDA)|Analiza statystyczna, Wizualizacje, Wnioski z analizy|1| 1 dzień
|Trenowanie modelu|Wybór modeli, Trenowanie, Optymalizacja| 1 | 1 dzień
|Walidacja i testowanie| Ocena modelu, Obliczenie metryk, Analiza wyników|1| 1 dzień
|Dokształcanie modelu| Dalsza optymalizacja, Walidacja krzyżowa | 1 | 1 dzień
|Publikacja i wdrożenie| Przygotowanie modelu do wdrożenia, Dokumentacja techniczna |1 | 1 dzień
|Prezentacja|Przygotowanie prezentacji, Sporządzenie raportu | 1 | 1 dzień

**- Podlega aktualizacji

**Uwaga**: Wszystkie kody, notatniki i dokumenty będą dostępne w tym repozytorium, uporządkowane w odpowiednich folderach.

## Wymagania techniczne

-   **Język programowania**: Python 3.8+
-   **Biblioteki**:
    -   Analiza danych: `pandas`, `numpy`
    -   Wizualizacja: `matplotlib`, `seaborn`
    -   Modelowanie: `scikit-learn`
-   **Środowisko**: Jupyter Notebook lub JupyterLab

## Autor

-   **Imię i nazwisko**: Mateusz Łaski
-   **Numer studenta**:  s26102
-   **Kontakt**: s26102@pjwstk.edu.pl
---
**Repozytorium zostało utworzone w ramach zajęć na uczelni i jest częścią projektu semestralnego.**