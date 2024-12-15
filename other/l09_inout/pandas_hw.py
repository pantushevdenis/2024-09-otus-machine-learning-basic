import pandas as pd
import seaborn as sb
from sys import stdout

ds = sb.load_dataset(name="tips")
ds.to_csv(stdout, lineterminator='\r')
