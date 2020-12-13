#%%
with open('input.txt','r') as f:
   data=f.read().split('\n\n')
# %%
def create_dict(line):
    pairs=line.strip('\n')
    pairs=line.split()
    pairs=[p.split(':') for p in pairs]
    dict_={p[0]:p[1] for p in pairs}
    return dict_
    
# %%
VALID_KEYS=set(['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid',])
# %%
def check_valid(line):
    dict_ = create_dict(line)
    dict_keys=[key for key in dict_]
    if all(key in dict_keys for key in VALID_KEYS):
        return True
    return False
# %% Verify with test cases
check_valid('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm') #True
check_valid('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929') #True
check_valid('hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm') #True
# %% Part 1
print(sum([check_valid(line) for line in data]))

# %%
def check_valid_b(line):
    dict_ = create_dict(line)
    
    try:
        # Valid keys
        dict_keys = [key for key in dict_]
        cond1 = all(key in dict_keys for key in VALID_KEYS)

        # byr
        cond2=1920 < int(dict_['byr']) <= 2002

        # iyr
        cond3=2010 < int(dict_['iyr']) <= 2020

        # eyr
        cond4=2020 < int(dict_['eyr']) <= 2030

        # hgt
        cond5 = check_hgt(dict_['hgt'])

        # hcl
        cond6 = check_hcl(dict_['hcl'])

        # ecl
        cond7 = dict_['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        # pid
        cond8 = len(dict_['pid'])==9

        if all([cond1,cond2,cond3,cond4,cond5,cond6,cond7,cond8]):
            return True


    except KeyError as e:
        print(f'Key error: {e}')
    
    return False

#%%
def check_hgt(hgt):
    if hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            return True
    if hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            return True
    return False
        
# %%
def check_hcl(hcl):
    if hcl[0] != '#':
        return False
    if len(hcl) != 7:
        return False
    
    VALID_CHARS=['0','1','2','3','4','5',
    '6','7','8','9','a','b','c','d','e','f'
    ]
    for i in range(1,6):
        if hcl[i] not in VALID_CHARS:
            return False
    
    return True
# %% Part 2
print(sum([check_valid_b(line) for line in data]))


# %%
