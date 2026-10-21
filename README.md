# CFA Franc vs Floating Currencies: Does a Fixed Peg Protect Against Instability?

Statistical comparison of inflation, economic growth and exchange-rate volatility between countries of the CFA franc zone (WAEMU) and countries with floating currencies, 2000-2024.

## Research question
Do CFA zone countries experience lower and more stable inflation than countries with floating currencies?

## Hypotheses
- H0: inflation has the same median and the same variance in both groups.
- H1: the groups differ in level and/or stability.

## Data
- World Bank API: annual inflation (CPI) and GDP growth.
- yfinance / FRED: exchange rates (later steps).

Country groups:
- CFA zone: Burkina Faso, Cote d'Ivoire, Senegal, Mali, Benin.
- Floating: Nigeria, Ghana, Kenya, South Africa.

Note: "floating" is a simplification (Kenya is a managed float; Nigeria operated multiple exchange rates before 2023).

## Methods
Descriptive statistics, normality tests, Mann-Whitney, Levene, chi-square test of independence, bootstrap confidence intervals.

## Status
Work in progress.