import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sb

ds = sb.load_dataset(name="tips")
# ds['sex'] = ds['sex'].replace(to_replace= {'Female' : 0, 'Male' : 1})
print(ds.head())

sb.boxplot(x='day', y='total_bill', data=ds)
plt.title("Взаимосвязь между признаками 'day' и 'total_bill'")
plt.show()



