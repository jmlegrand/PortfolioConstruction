import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datas = pd.read_csv('datas/Portfolios_Formed_on_ME_monthly_EW.csv',
                    header=0, index_col=0, parse_dates=True, na_values=-99.99)
print(datas.head())
columns = ['Lo 10', 'Hi 10']

datas_filtered = datas[columns] / 100
datas_filtered.columns = ['Small Cap', 'Large Cap']
print(datas_filtered.head())
datas_filtered.plot.line()
# plt.show()

print('standard deviation', datas_filtered.std())
annualized_vol = datas_filtered.std() * np.sqrt(12)
print('annualized standard deviation', annualized_vol)

# How to annualize the return
print(datas_filtered)
return_per_month = ((datas_filtered+1).prod())**(1/datas_filtered.shape[0]) - 1
print(return_per_month)
return_per_year = (1+return_per_month)**12 - 1
print(return_per_year)

risk_ratio = return_per_year / annualized_vol
print('risk_ratio', risk_ratio)

risk_free_rate = 0.03
excess_return = return_per_year - risk_free_rate

sharpe_ratio = excess_return / annualized_vol
print(sharpe_ratio)
