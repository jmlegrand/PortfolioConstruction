import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1. how to compute a return from a list of prices
prices_a = np.array([8.70, 8.91, 8.71])
print('prices_a', prices_a)
print('prices_a returns', prices_a[1:]/prices_a[:-1]-1)

prices_b = pd.DataFrame({
    "BLUE": [8.70, 8.91, 8.71, 8.43, 8.73],
    "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]}
)
# solution 1
print('solution 1', prices_b.iloc[1:].values/prices_b.iloc[:-1]-1)

# solution 2
print('solution 2', (prices_b/prices_b.shift(1)-1)[1:])

# solution 3
print('solution 3', (prices_b.pct_change())[1:])


# 2. how to compute multiple returns to a compound return
prices_csv = pd.read_csv('datas/sample_prices.csv')
print('prices_csv', prices_csv)
return_prices_csv = (prices_csv.pct_change())[1:]
print('return_prices_csv', return_prices_csv)
# prices_csv.plot()
# plt.show()
return_prices_csv.plot.bar()
plt.show()
print('prices_csv standard deviation', return_prices_csv.std())
print('prices_csv mean', return_prices_csv.mean())
# solution 1
print('compound return using explicitly np ', (((np.prod(return_prices_csv+1))-1)*100).round(2))

# solution 2
print('compound return wo using np', (((return_prices_csv+1).prod()-1)*100).round(2))

# 3. how to compute annualized return
monthly_return = 0.01
print('annualized return', ((monthly_return+1)**12-1)*100)

quarter_return = 0.04
print('annualized return', ((quarter_return+1)**4-1)*100)
