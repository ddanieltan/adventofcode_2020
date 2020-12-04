#%% Read in inputs
with open('input.txt','r') as f:
    data=(f
        .read()
        .splitlines()
    )
    data = [int(num) for num in data]
    

# %% Part 1
from itertools import combinations
combis = combinations(data, r=2)
for combi in combis:
    x, y = combi
    if x+y == 2020:
        print(f'Part 1: {x*y}') 
# %% Part 2
combis = combinations(data, r=3)
for combi in combis:
    x, y, z = combi
    if x+y+z == 2020:
        print(f'Part 2: {x*y*z}') 

# %%
