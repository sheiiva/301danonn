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


class QuickSort():

    def __init__(self, tab: list):
        self._icmp = 0
        self._tab = deepcopy(tab)
        #
        self.run()

    def sort(self, arr: list) -> None:

        """
        Sort self._tab using insertion sorting algorithm.
        """

        length = len(arr)
        pivot = 0
        left, right = [], []

        if length <= 1:
            return
        for i in range(1, length):
            self._icmp += 1
            if arr[i] < arr[pivot]:
                left.append(arr[i])
            else:
                right.append(arr[i])
        self.sort(right)
        self.sort(left)

    def showResult(self) -> None:

        """
        Print nb of comparison done.
        """

        print("Quicksort: {} comparisons".format(self._icmp))

    def run(self) -> None:

        """
        Run sorting algorithm and print result.
        """

        self.sort(self._tab)
        self.showResult()
