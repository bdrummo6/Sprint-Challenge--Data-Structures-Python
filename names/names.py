import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Improved implementation best runtime out of 3 was 0.19088363647460938 seconds (64 duplicates)
# Create Binary Search Tree and initialize the root node with the first line in list names_1
bst_names1 = BSTNode(names_1[0])

# loop through names_1 and insert each line into the bst_names1
for name_1 in names_1:
    bst_names1.insert(name_1)
# loop through names_2 and check if each name is in bst_names1
for name_2 in names_2:
    # Use the BST contain method to check if name_2 is in bst_names1
    if bst_names1.contains(name_2):
        # if the name is in both list then append the name to duplicates
        duplicates.append(name_2)

"""
# Original code best runtime out of 3 was 6.940738677978516 seconds (64 duplicates)
# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
            
"""

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n{(', '.join(duplicates))}\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
