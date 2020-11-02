############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 301dannon            #
#                                          #
############################################

from copy import deepcopy


class MergeSort():

    def __init__(self, tab: list):
        self._icmp = 0
        self._tab = deepcopy(tab)
        #
        self.run()

    def merge(self, arr: list, left: list, right: list) -> None:

        i = j = k = 0

        def concat(arr: list, brr: list, adex: int, bdex: int) -> None:
            while bdex < len(brr):
                arr[adex] = brr[bdex]
                adex += 1
                bdex += 1

        while i < len(left) and j < len(right):
            self._icmp += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        concat(arr, left, k, i)
        concat(arr, right, k, j)

    def sort(self, arr: list) -> None:

        """
        Sort self._tab using merge sorting algorithm.
        """

        if len(arr) == 1:
            return

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        self.sort(left)
        self.sort(right)
        self.merge(arr, left, right)

    def showResult(self) -> None:

        """
        Print nb of comparison done.
        """

        print("Merge sort: {} comparisons".format(self._icmp))

    def run(self) -> None:

        """
        Run sorting algorithm and print result.
        """

        self.sort(self._tab)
        self.showResult()
