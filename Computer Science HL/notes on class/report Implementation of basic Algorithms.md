wordcount of analysis (excluding wordcount itself): 490

## Hash search with linear and binary search

Hash search refers to a search technique that uses a hash table to store and retrieve data efficiently based on a key. In a hash table, data is stored in key-value pairs, where a hash function is applied to compute the key. (O'Reilly) When two hashed elements happen to share the same hash value, hash collision accors. ("Hash Collision.") Approaches like open hashing and closed hashing are used to avoid hash collision. (Programming.Guide)

Its space complexity is $O(k)$ where $k$ is the length of the hash table. Usually it is a huge prime. (Design Gurus Team)

| **Search Algorithm** | **Time Complexity (Best Case)** | **Time Complexity (Worst Case)** | **Space Complexity** | **Key Characteristics**                                                                                       |
|-----------------------|---------------------------------|-----------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------|
| **Hash Search**       | $O(1)$                       | $O(1)$ (with perfect hash) or $O(n)$ (with collisions) | $O(K)$             | - Requires additional space($K$) for the hash table.|
| **Linear Search**     | $O(1)$                       | $O(n)$                         | $O(1)$             | - Simple to implement. <br> - No additional space required.                          |
| **Binary Search**     | $O(1)$                       | $O(\log n)$                    | $O(1)$ or $O(\log n)$ (recursive) | - Requires sorted data. <br> - Can use iterative or recursive approaches.                        |

Comparing the application of hash search with linear search and binary search, hash search is highly effective for applications requiring precise lookups, such as KV based cache database like Redis, or managing large datasets where quick access to elements is essential. (Geeksforgeeks, "Application of") In contrast, linear search is used in simpler applications with unsorted datasets, where direct comparison of elements fit the need (Geeksforgeeks, "Where"), and binary search is suited for sorted datasets, such as searching in ordered arrays or directories (Geeksforgeeks, "Applications, Advantages"). While both linear and binary searches have their own advantages, hash search stands out in environments demanding rapid, key-based data retrieval.

## Bucket sort with bubble and selection sort

Bucket sort(Bin sort) is a sorting algorithm that distribute elements into buckets based on certain criteria or rule, and sorts each bucket individually (recursively). Finally, the sorted buckets are combined to produce the final sorted array. ("Bucket Sort.")

| **Sort Algorithm** | **Time Complexity (Best Case)** | **Time Complexity (Worst Case)** | **Space Complexity** | **Key Characteristics** |
|---------------------|--------------------------------|----------------------------------|-----------------------|--------------------------|
| **Bucket Sort**     | $O(n)$                       | $O(n+\frac{n^2}{k}+k)$          | $O(K)$               | Efficient for uniformly distributed data. |
| **Bubble Sort**     | $O(n)$                       | $O(n^2)$                        | $O(1)$               | Efficient for saving memory. |
| **Selection Sort**  | $O(n^2)$                     | $O(n^2)$                        | $O(1)$               |  Same as above. |

To make a comparison of their usage, bucket Sort is ideal for sorting uniformly distributed numerical data, such as percentages, though it requires extra memory. ("Bucket Sort: Algorithm, Time Complexity, Code, More.") In contrast, Bubble Sort is primarily used for educational purposes, as it demonstrates basic sorting concepts through repeated adjacent swaps. ("Bubble Sort.") Selection Sort, while also inefficient for large datasets, is useful when memory is limited and a straightforward algorithm is needed to organize small amounts of data. (Geeksforgeeks, "Selection")

## Code Snippet

Authorship can be found in comments.
Test code by Ifesinachi.
The video used [Interactive Python & JavaScript Code Visualization | Learn DSA](https://staying.fun/en/features/algorithm-visualize) to visualize the code process.

```Python
# Ifesinachi
def bubble_sort(input_list):
    #outer loop to iterate through the list n times.
    length = len(input_list)
    for i in range(0,length):
        for j in range(0,length-1):
            if input_list[j]>input_list[j+1]:
                input_list[j],input_list[j+1]=input_list[j+1],input_list[j]
    print(f"sorted list: {input_list}")
    return input_list

# bubble_sort([5, 2, 9, 1, 5, 6])  # Normal case: Unsorted list with multiple elements
# bubble_sort([3, 3, 3, 3, 3])     # Edge case: List with all identical elements
# bubble_sort([1])                 # Edge case: Single element list
# bubble_sort([])                  # Edge case: Empty list

# Richard
def selection_sort(input_list):
    length = len(input_list)
    for i in range(0,length):
        min_index = i
        for j in range(i+1, length):
            if input_list[j]<input_list[min_index]:
                min_index = j
        input_list[i],input_list[min_index] = input_list[min_index],input_list[i] # swap
    print(f"sorted list: {input_list}")
    return input_list

# selection_sort([5, 2, 9, 1, 5, 6])  # Normal case: Unsorted list with multiple elements
# selection_sort([3, 3, 3, 3, 3])     # Edge case: List with all identical elements
# selection_sort([1])                 # Edge case: Single element list
# selection_sort([])                  # Edge case: Empty list

# Ifesinachi
def seq_search(input_list, target):
    length=len(input_list)
    for i in range(0, length):
        if str(target) == str(input_list[i]):
            print(f"Target found at index {i}")
            return
    print("Target not found")

# seq_search([5, 2, 9, 1, 5, 6], 9)    # Normal case: Target present in the list
# seq_search([3, 3, 3, 3, 3], 3)      # Normal case: Target is the only element and repeated
# seq_search([1], 1)                  # Edge case: Single element list where the target is present
# seq_search([1], 2)                  # Edge case: Single element list where the target is not present
# seq_search([], 5)                   # Edge case: Empty list
# seq_search([7, 5, 3, 8, 10], "3")   # Normal case: Target is a string representation of an integer


# Richard
def binary_search(input_list, target):
    target = int(target)
    length = len(input_list)
    for i in range(1,length):
        if input_list[i-1]>input_list[i]:
            print("the array should be sorted in ascending order!")
            print(f"current array: {input_list}")
            return
    l = 0
    r = length-1
    found = -1
    while(l<=r):
        mid = l + (r-l)//2
        if input_list[mid] == target:
            found = mid
            break
        elif input_list[mid] < target:
            l = mid+1
        else:
            r = mid-1
    if found>=0:
        print(f"target found at index {found}.")
    else:
        print("target not found in the array.")

# binary_search([1, 2, 3, 4, 5, 6], 4)     # Normal case: Target found in sorted array
# binary_search([1, 2, 3, 4, 5, 6], 10)    # Normal case: Target not in the array
# binary_search([5, 3, 1, 4, 2], 3)        # Edge case: Unsorted array (error should be printed)
# binary_search([], 5)                    # Edge case: Empty array

# Richard
def set_list():
    user_list = input("enter the array, split element in `,`\n> ").split(',')
    is_str = False
    for element in user_list:
        if element.isdigit()==False:
            is_str = True
            break
    if not is_str:
        user_list = [int(i) for i in user_list]
    print(f"defined array: {user_list}")
    type_ = "string" if is_str else "int"
    print(f"type of list: {type_}")
    return user_list

def help(lst):
    instructions = """
===============================================================================
Instructions:
Use the following commands to interact with the program:
  q  - Quit the program.
  h  - Display this help message.
  a  - Set a new list. Enter elements separated by commas.
  f  - Find an element in the list:
       s  - Sequential search.
       b  - Binary search (ensure the list is sorted in ascending order).
       h  - Hash-based search.
  s  - Sort the list in ascending order:
       bu - Bubble sort.
       s  - Selection sort.
       bi - Bin sort (only for integer arrays within a valid range).

Note:
  - Ensure the list is set (using 'a') before performing searches or sorting.
  - Binary search requires the list to be sorted in ascending order.
  - Bin sort supports only non-negative integers within the specified range.
"""
    print(instructions)
    print(f"current list: {lst}")
    print("===============================================================================")

def quit():
    print("See you next time!")
    exit(0)

PRIME = 737927 # generated through https://bigprimes.org/

def custom_hash(value): # perform a hash
    if isinstance(value, int):
        return value%PRIME
    else:
        # Ensure the value is a string
        value_str = str(value)
        # Compute a simple hash
        hash_value = 0
        for char in value_str:
            hash_value = (hash_value * 52 + ord(char)) % PRIME
        return hash_value

# Richard
def hash_search(user_list, target):
    if isinstance(target, str) and target.isnumeric():
        target = int(target)
    hash_map = [[] for _ in range(PRIME)] # [[index1, index2], [index], ...] for open hash
    for index,value in enumerate(user_list):
        hash_map[custom_hash(value)].append(index)
    found = hash_map[custom_hash(target)]
    for index in found:
        # print(user_list[index])
        if user_list[index] == target:
            print(f"target found at index {index}.")
            return
    print("target not found in the array.")

# hash_search([10, 20, 30, 40, 50], 30)   # Normal case: Target found in list
# hash_search([], 10)                     # Edge case: Empty list
# hash_search([737927, 1475854, 2213801], 737927)  # Edge case: Simulated hash collision
# # Testing with non-integer target and list elements (non-integer values should be properly hashed)
# hash_search(["apple", "banana", "cherry"], "banana")  # Normal case: String target found
# hash_search(["apple", "banana", "cherry"], "grape")   # Edge case: String target not found

BUCKET_SIZE = 99999
# Richard
def bin_sort(user_list):
    if len(user_list)==0 or not isinstance(user_list[0], int):
        print("This algorithm only supports int array.")
        return user_list
    if max(user_list) > BUCKET_SIZE or min(user_list) < 0:
        print("Number in the array too big or negative.")
        print(f"Valid range: [0, {BUCKET_SIZE-1}]")
        return user_list
    buckets = [0]*BUCKET_SIZE
    for num in user_list:
        buckets[num]+=1
    cursor = 0
    for index,num in enumerate(buckets):
        for i in range(0,num):
            user_list[cursor] = index
            cursor+=1
    print(f"sorted list: {user_list}")
    return user_list

# bin_sort([1, 1, 3, 3, 2, 2, 2, 1])     # Normal case: List with duplicates
# bin_sort([0, 5, 10, 0, 5])             # Normal case: List with values within range [0, 99998]

# # Edge cases
# bin_sort([])                          # Edge case: Empty list
# bin_sort([99999, 100000])              # Edge case: Number out of valid range (above BUCKET_SIZE)
# bin_sort([-1, 0, 5, 8])                # Edge case: Negative number in the list

# Richard
def router(user_input, lst):
    if user_input == "q":
        quit()
    elif user_input == "h":
        help(lst)
    elif user_input == "a":
        lst = set_list()
    elif user_input == "f":
        user_input = input("\n`s` for sequential search\n`b` for binary search(makesure the list is in ascending order)\n`h` for hash search> ")
        target = input("enter the value to find>")
        if user_input == "s":
            seq_search(lst,target)
        elif user_input == "b":
            binary_search(lst, target)
        elif user_input == "h":
            hash_search(lst,target)
        else:
            print("Invalid command selection.")
            # help()
    elif user_input == "s":
        user_input = input("\n`bu` for bubble sort\n`s` for selection sort\n`bi` for bin sort> ")
        if user_input == "bu":
            lst = bubble_sort(lst)
        elif user_input == "s":
            lst = selection_sort(lst)
        elif user_input == "bi":
            lst = bin_sort(lst)
        else:
            print("Invalid command selection.")
            # help()
    else:
        print("Invalid command selection.")
    return lst

def main():
    lst = []
    while(114==114):
        help(lst)
        user_input = input("> ")
        lst = router(user_input, lst)
    return 0

if __name__ == "__main__":
    main()
```

snippet from OI wiki:

The snippet demonstrates a hash table and hash lookup. It uses a static list to store the nodes, while I used a dynamic one. Thus OI wiki has a better performance.

```Python
# [哈希表 - OI Wiki](https://oi-wiki.org/ds/hash/#__tabbed_1_2)
M = 999997
SIZE = 1000000


class Node:
    def __init__(self, next=None, value=None, key=None):
        self.next = next
        self.value = value
        self.key = key


data = [Node() for _ in range(SIZE)]
head = [0] * M
size = 0


def f(key):
    return key % M


def get(key):
    p = head[f(key)]
    while p:
        if data[p].key == key:
            return data[p].value
        p = data[p].next
    return -1


def modify(key, value):
    p = head[f(key)]
    while p:
        if data[p].key == key:
            data[p].value = value
            return data[p].value
        p = data[p].next


def add(key, value):
    if get(key) != -1:
        return -1
    size = size + 1
    data[size] = Node(head[f(key)], value, key)
    head[f(key)] = size
    return value

```

The snippet below demonstrates a bucket sort. It is less efficient, as it sorts buckets after sorting elements inside each bucket, while my implementation avoids the sorting of buckets, making the time complexity a constant.

```Python
# [桶排序 - OI Wiki](https://oi-wiki.org/basic/bucket-sort/#__tabbed_1_2)
N = 100010
w = n = 0
a = [0] * N
bucket = [[] for i in range(N)]


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


def bucket_sort():
    bucket_size = int(w / n + 1)
    for i in range(0, n):
        bucket[i].clear()
    for i in range(1, n + 1):
        bucket[int(a[i] / bucket_size)].append(a[i])
    p = 0
    for i in range(0, n):
        insertion_sort(bucket[i])
        for j in range(0, len(bucket[i])):
            a[p] = bucket[i][j]
            p += 1
```

## Testing the code

This test will apply numerical data. The program also accepts string. The usage is roughly the same with integers, so we will not test on string.

### launch program

![[UWC/CS/_resources/Pasted image 20250118173042.png]]

### setting the list

![[UWC/CS/_resources/Pasted image 20250118173422.png]]

### performing search

enter `f` to search mode, select a method(`s` for sequential search, `b` for binary search, `h` for hash search).

![[UWC/CS/_resources/Pasted image 20250118173653.png]]

#### Sequential search

search successful:

![[UWC/CS/_resources/Pasted image 20250118173723.png]]

handle failure:

![[UWC/CS/_resources/Pasted image 20250118173744.png]]

#### Binary search

when data is not sorted

![[UWC/CS/_resources/Pasted image 20250118173856.png]]

after sort, if found

![[UWC/CS/_resources/Pasted image 20250118173935.png]]

if not found:

![[UWC/CS/_resources/Pasted image 20250118174012.png]]

#### Hash search

search successful:

![[UWC/CS/_resources/Pasted image 20250118174224.png]]

search fails:

![[UWC/CS/_resources/Pasted image 20250118174312.png]]

handle hash collision (the hash prime is 737927):

![[UWC/CS/_resources/Pasted image 20250118174429.png]]

### performing sort

enter `s` to sort mode, select a method(`bu` for bubble sort, `s` for selection sort, `bi` for bin sort).

![[UWC/CS/_resources/Pasted image 20250118174700.png]]

#### Bubble sort

![[UWC/CS/_resources/Pasted image 20250118174730.png]]

#### Selection sort

![[UWC/CS/_resources/Pasted image 20250118174905.png]]

#### Bin sort

![[UWC/CS/_resources/Pasted image 20250118175159.png]]

### Displaying the instruction

type `h` to show the instruction again. It is not useful, because instruction is printed everytime after any instruction.

![[UWC/CS/_resources/Pasted image 20250118175351.png]]

typing `h`:

![[UWC/CS/_resources/Pasted image 20250118175428.png]]

### Quit

type `q`

![[UWC/CS/_resources/Pasted image 20250118175504.png]]

## Additional Note

The planned program logic and division of work:

![[UWC/CS/_resources/major.png]]
