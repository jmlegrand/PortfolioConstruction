import pandas as pd
import numpy as np

prices_csv = pd.read_csv('datas/sample_prices.csv')
returns = prices_csv.pct_change().dropna()
print('standard deviation: ', returns.std())
deviations = returns - returns.mean()
deviations_to_the_square = deviations**2

# variance = deviations_to_the_square.mean()
number_of_observations = returns.shape[0]
variance = deviations_to_the_square.sum() / (number_of_observations - 1)

# volatility = variance**0.5
volatility = np.sqrt(variance)
print('variance: ', volatility)

print('annualized volatility: ', volatility * np.sqrt(12))

