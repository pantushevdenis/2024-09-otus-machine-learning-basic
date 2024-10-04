import itertools as it

data = "aaabbbbccccc"
encoding = "".join([ch + str(sum(1 for _ in gr)) for ch, gr in it.groupby(data)])
print(encoding)

    
