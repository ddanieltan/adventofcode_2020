#%% Read input
with open('input.txt','r') as f:
    data=(f
        .read()
        .splitlines())
    
    data = [line.split() for line in data]


# %%
from collections import Counter
def check_rules(line):
    """
    Returns True if the password adheres to the rules
    """
    min_,max_=map(int,line[0].split('-'))
    letter=line[1][0]
    password=line[2]

    dict_ = Counter([letter for letter in password])
    count = dict_.get(letter)
    if count is None:
        return False
    if count<min_ or count>max_:
        return False
        
    return True
# %% Verify with test case
check_rules(['1-3','a:','abcde']) #True
#check_rules(['1-3','b:','cdefg']) #False
#check_rules(['2-9','c:','ccccccccc']) #True
