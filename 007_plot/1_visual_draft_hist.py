import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sb

ds = sb.load_dataset(name="tips")
ds_total_bill = ds["total_bill"]
print(ds.head())
print(ds_total_bill)
plt.hist(ds_total_bill)
plt.title("Гистограмма распределения total_bill")
plt.xlabel("total_bill, $")
plt.ylabel("Количество")
plt.show()



