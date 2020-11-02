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


class SelectionSort():

    def __init__(self, tab: list):
        self._icmp = 0
        self._tab = deepcopy(tab)
        self._tablen = len(tab)
        #
        self.run()

    def swap(self, adex: int, bdex: int, tab: list) -> list:

        """
        Swap tab's elements at index adex and bdex.
        """

        tmp = tab[adex]
        tab[adex] = tab[bdex]
        tab[bdex] = tmp

    def sort(self) -> None:

        """
        Sort self._tab using selection sorting algorithm.
        """

        for i in range(self._tablen):
            imin = i
            for j in range(i+1, self._tablen):
                self._icmp += 1
                if self._tab[j] < self._tab[imin]:
                    imin = j
            if imin != i:
                self.swap(imin, i, self._tab)

    def showResult(self) -> None:

        """
        Print nb of comparison done.
        """

        print("Selection sort: {} comparisons".format(self._icmp))

    def run(self) -> None:

        """
        Run sorting algorithm and print result.
        """

        self.sort()
        self.showResult()
