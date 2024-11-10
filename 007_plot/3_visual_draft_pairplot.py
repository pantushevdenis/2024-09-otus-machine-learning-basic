import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sb

ds = sb.load_dataset(name="tips")
ds['smoker'] = ds['smoker'].replace(to_replace = {'Yes' : 1, 'No' : 0})
ds['sex'] = ds['sex'].replace(to_replace= {'Female' : 0, 'Male' : 1})
print(ds)
g = sb.pairplot(ds, kind="scatter", vars={'total_bill', 'sex', 'tip', 'size'})
plt.show()



