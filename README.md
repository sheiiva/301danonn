301dannon
===

Time:       2 weeks

Team:       1

Language:   Python


The project
----
You’ve been hired by **Dannon** to **sort all the information from their databases**. There are a few thousand
petabytes of data, and it is critical to implement the most optimal sort possible.

You have to implement and benchmark the following algorithms:
* Selection sort
* Insertion sort
* Bubble sort
* Quicksort
* Merge sort

To ensure you get the proper results, please follow these **implementation guidelines**:
* Whenever you go through the list of elements (whether you are looking for, selecting or inserting an
element), **always go from left to right**.
* **For quicksort**, always pick the first element as pivot, and keep the relative order of the elements in
both partitions.
* **Don’t optimize** the algorithms, or you will skew the results. For example, don’t use a flag to stop bubble
sort early when nothing was swapped.


## USAGE:

```
>> ./301dannon -h
USAGE
    ./301dannon file
DESCRIPTION
    file    file that contains the numbers to be sorted, separated by spaces
```

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva)