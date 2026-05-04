## Hash search with linear and binary search

- hash search
	- **definition**: refers to a search technique that uses a **hash table** to store and retrieve data efficiently based on a key. In a hash table, data is stored in key-value pairs, where a **hash function** is applied to the key to compute an index that determines where the value is stored. ([5.4. Hash-based Search - Algorithms in a Nutshell [Book]](https://www.oreilly.com/library/view/algorithms-in-a/9780596516246/ch05s04.html)) When two hashed elements happen to share the same hash value, hash collision accors. ([Hash collision - Wikipedia](https://en.wikipedia.org/wiki/Hash_collision)) Several approaches are used to avoid hash collision, and two of them are open hashing and closed hashing. ([Hash Tables: Open vs Closed Addressing | Programming.Guide](https://programming.guide/hash-tables-open-vs-closed-addressing.html)) The code here performs an open hashing. Improving the hash function also reduce the chance of hash collision.
	- **time complexity**: $O(n \times L)$ for preparation, where $n$ is the number of element in the searched list. $L$ is the hash function's time complexity, and it is usually a rather small constant coefficient. The time complexity for searching is typically $O(1)$, but hash collisions may cause the complexity to reach $O(n)$ for the worst case.
	- **space complexity**: $O(k)$ where $k$ is the length of the hash table. Usually it is a huge prime. ([Why should hash functions use a prime number modulus?](https://www.designgurus.io/answers/detail/why-should-hash-functions-use-a-prime-number-modulus)) It has to be big enough to reduce the chance of hash collision. 
- linear search
	- **definition**: checks each element in a list sequentially until the target is found or the list ends. ([David Slide])
- binary search
	- **definition**: divides a sorted list into halves, eliminating half the search space at each step, until the target is found or the search space is empty. ([David Slide])
- **comparing time complexity**: $O(n)$ and $O(\log_{2}{n})$ respectively where $n$ is the length of the array, slower for each query than hash search.
- **space complexity**: Both do not take space except the original array, better than hash search.
- **application**: ==not finished==Hash search is highly effective for applications requiring fast and efficient lookups, such as dictionary operations, database indexing, or managing large datasets where quick access to elements is essential. Its ability to retrieve data using unique keys makes it ideal for scenarios like caching, implementing hash tables, or handling user authentication systems. In contrast, linear search is used in simpler applications with unsorted or small datasets, where direct comparison of elements suffices, and binary search is suited for sorted datasets, such as searching in ordered arrays or directories. While both linear and binary searches have niche uses, hash search stands out in environments demanding rapid, key-based data retrieval.


## Bucket sort with bubble and selection sort

- bucket sort(bin sort)
	- **definition**: a sorting algorithm that distribute elements into buckets based on certain criteria or rule, and sorts each bucket individually (recursively). Finally, the sorted buckets are combined to produce the final sorted array. ([Bucket sort - Wikipedia](https://en.wikipedia.org/wiki/Bucket_sort))
	- **time complexity**: Average complexity of $O(n+\frac{n^2}{k}+k)$ where $k$ is the number of buckets and $n$ is the length of sorted list. %%In our code, the complexity is $O(max(n,k))$. ==maybe need more explanation==%%
	- **space complexity**: $O(k)$ where $k$ is the number of bucket.
- bubble sort
	- **definition**: Repeatedly swaps adjacent elements if they are in the wrong order, gradually "bubbling" the largest (or smallest) element to its correct position. ([David Slide])
- selection sort
	- **definition**: Repeatedly selects the smallest (or largest) element from the unsorted portion and swaps it with the first unsorted element. ([David Slide])
- **comparing time complexity**: Both have $O(n^2)$, less efficient than bucket sort.
- **space complexity**: Both do not take additional space, more effective in memory usage.
- **application**: Bucket Sort is ideal for sorting uniformly distributed numerical data, such as percentages, as it efficiently categorizes values into buckets for sorting, though it requires extra memory. In comparison, Bubble Sort is primarily used for educational purposes, as it demonstrates basic sorting concepts through repeated adjacent swaps. Selection Sort, while inefficient for large datasets, is useful when memory is limited and a straightforward algorithm is needed to organize small amounts of data. ==not finished==
