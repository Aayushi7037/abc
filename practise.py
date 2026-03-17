import pandas as pd

index = [
    ('Amritsar', 2000), ('Amritsar', 2010),
    ('Hoshiarpur', 2000), ('Hoshiarpur', 2010),
    ('Ludhiana', 2000), ('Ludhiana', 2010)
]

populations = [
    2123656, 2490656,
    1234625, 1586625,
    2898739, 3498739
]
pop = pd.Series(populations, index=index)


print(pop)

index = pd.MultiIndex.from_tuples(index)
print(index)

import pandas as pd
index=[
   ('haridwar',2000),('laksar',8900)
   ('') 

]
