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
check_rules(['1-3','b:','cdefg']) #False
check_rules(['2-9','c:','ccccccccc']) #True

# %% Part 1
num_valid=0
for line in data:
    if check_rules(line):
        num_valid+=1
print(f'Part 1: {num_valid}')
# %%
def check_rules_b(line):
    """
    Returns True if password adheres to new rules from Part 2
    """
    # Convert min/max to index positions x and y
    min_,max_=map(int,line[0].split('-'))
    x = min_-1
    y = max_-1
    letter=line[1][0]
    password=line[2]

    first = password[x]
    second = password[y]
    if first==None or second==None:
        return False
    
    if (first==letter and second!=letter) or (first!=letter and second==letter):
        return True 
    return False
# %% Verify with test cases
check_rules_b(['1-3','a:','abcde']) #True
check_rules_b(['1-3','b:','cdefg']) #False
check_rules_b(['2-9','c:','ccccccccc']) #Fale
# %% Part 2
num_valid=0
for line in data:
    if check_rules_b(line):
        num_valid+=1

print(f'Part 2: {num_valid}')

