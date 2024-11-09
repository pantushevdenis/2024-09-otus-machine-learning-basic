import pandas as pd
import matplotlib as mp
import seaborn as sb

ds = sb.load_dataset(name="tips")
print(type(ds))
print(ds)
print(ds.head())
print(ds.shape)
# print(ds[1:10])
print(ds.columns)
# print(ds[["total_bill", "smoker"]])
# print(ds["total_bill"].hist())
print(ds["total_bill"].max(axis=0))
#print(ds["smoker"][ds["smoker"] == "Yes"].shape[0])
print(
    ds.groupby("day").agg(
        total_bill_avg=pd.NamedAgg(column="total_bill", aggfunc="mean")
    )
)

print(
    ds.loc[ds["total_bill"] > ds["total_bill"].mean()]
)

filtered = ds.loc[ds["total_bill"] > ds["total_bill"].mean()]
print(filtered.groupby("sex")["tip"].mean())

print(
ds.loc[ds["total_bill"] > ds["total_bill"].mean()].groupby("sex")["tip"].mean()
)

ds['smoker'] = ds['smoker'].replace(to_replace = {'Yes' : 1, 'No' : 0})
print(ds.head())


