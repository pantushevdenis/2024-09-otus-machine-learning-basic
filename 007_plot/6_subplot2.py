import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sb

ds = sb.load_dataset(name="tips")
print(ds)
print(ds['sex'].unique())
ds_male = ds.loc[ds["sex"] == 'Male']
print(ds_male)
ds_female = ds.loc[ds["sex"] == 'Female']
print(ds_female)

fig, axes = plt.subplots(2, 1)
plt.suptitle('')
sb.scatterplot(data=ds_male, x='total_bill', y='tip', hue='smoker', ax=axes[0])
axes[0].set_title('total_bill vs tip fr male')
axes[0].set_xlim(0, 50)
axes[0].set_ylim(0, 10)
sb.scatterplot(data=ds_female, x='total_bill', y='tip', hue='smoker', ax=axes[1])
axes[1].set_title('total_bill vs tip fr female')
axes[1].set_xlim(0, 50)
axes[1].set_ylim(0, 10)
plt.show()
