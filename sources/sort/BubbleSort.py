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


class BubbleSort():

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

        tab[adex], tab[bdex] = tab[bdex], tab[adex]

    def sort(self) -> None:

        """
        Sort self._tab using bubble sorting algorithm.
        """

        for i in range(self._tablen-1, 0, -1):
            for j in range(i):
                self._icmp += 1
                if self._tab[j] < self._tab[j+1]:
                    self.swap(j, j+1, self._tab)

    def showResult(self) -> None:

        """
        Print nb of comparison done.
        """

        print("Bubble sort: {} comparisons".format(self._icmp))

    def run(self) -> None:

        """
        Run sorting algorithm and print result.
        """

        self.sort()
        self.showResult()
