﻿# Проект по курсу *IT для финансистов*

**Цель проекта:** исследовать работу торговых правил:

- Моментум (momentum);
- Возврат к среднему (mean reversion);
- Hurst Rule

## Терминология

Пусть $\vec{r}$ – массив предшествующих торговому периоду доходностей (обучающая выборка для среднего); **long**, **short**, **nothing** – рекомендация занять длинную, короткую или не занимать позицию соответственно. Тогда

- Моментум (*momentum*) – стратегия, основанная на выборе позиции в соответствии со знаком скользящей средней предыдущих доходностей.
- Возврат к среднему (*mean reversion*) – стратегия, основанная на выборе позиции противоположной знаку скользящей средней предыдущих доходностей.
- *Hurst Rule* – мета-правило выбора между momentum и mean reversion в зависимости от значения экспоненты Хёрста $H$.

## Результаты

На примере нескольких окон мы получили, что наибольшую прибыль приносит стратегия **momentum**.
