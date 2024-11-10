import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sb

ds = sb.load_dataset(name="tips")
print(ds.head())
ds_total_bill = ds["total_bill"]
ds_tip = ds["tip"]
print(ds_total_bill)
print(ds_tip)
corr_total_bill_tip = ds_total_bill.corr(ds_tip)
print(corr_total_bill_tip)

plt.scatter(ds_total_bill, ds_tip)
plt.title("Взаимосвязь между признаками 'total_bill' и 'tip")
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.show()



