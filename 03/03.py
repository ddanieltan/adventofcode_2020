#%%
with open('input.txt','r') as f:
    data=f.read().splitlines()
# %%
def check_for_tree(line,n):
    """
    Returns True if collision with tree

    Inputs
    - line : actual coordinates
    - n: nth line from data
    """

    position = (n*3) % len(line)
    if line[position]=='#':
        return True
    if line[position]=='.':
        return False
    
    return None
# %% Verify against test case
check_for_tree('#...#...#..',1) # False
check_for_tree('.#....#..#.',2) # True
check_for_tree('..#.#...#.#',3) # False
check_for_tree('.#..#...#.#',10) # True

# %% Part 1
num_trees=0
for n,line in enumerate(data):
    if n==0:
        continue
    if check_for_tree(line,n):
        num_trees+=1

print(f'Part 1: {num_trees}')
# %%
def check_for_trees_b(line,n,right):
    """
    Returns True if collision with tree

    Additionally require number of right steps
    """

    position = (n*right) % len(line)
    if line[position]=='#':
        return True
    if line[position]=='.':
        return False
    
    return None
# %%
def count_trees_hit(right):
    num_trees=0
    for n,line in enumerate(data):
        if n==0:
            continue
        if check_for_trees_b(line,n,right):
            num_trees+=1
    return num_trees
# %%
def count_trees_hit_skip():
    """
    Custom func to calculate Right 1, Down 2
    """
    num_trees=0
    data_ = data[::2] 
    for n,line in enumerate(data_):
        if n==0:
            continue
        if check_for_trees_b(line,n,right=1):
            num_trees+=1
    return num_trees


# %%
ans = (count_trees_hit(1) * 
    count_trees_hit(3)  *
    count_trees_hit(5)  *
    count_trees_hit(7)  *
    count_trees_hit_skip()
)
print(f'Part 2: {ans}')
# %%
