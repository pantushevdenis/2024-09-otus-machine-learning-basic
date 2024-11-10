import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset(name="tips")
print(df)
print(df['time'].unique())
ds_tip_dinner = df.loc[df["time"] == 'Dinner']['tip']
print(ds_tip_dinner)
ds_tip_lunch = df.loc[df["time"] == 'Lunch']['tip']
print(ds_tip_lunch)

fig, axes = plt.subplots(2, 1)
plt.suptitle('Dataset Tips')
sns.histplot(ds_tip_dinner, ax=axes[0])
axes[0].set_title('tip on dinner')
sns.histplot(ds_tip_lunch, ax=axes[1])
axes[1].set_title('tip on lunch')
plt.show()