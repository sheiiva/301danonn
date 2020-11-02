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


class InsertionSort():

    def __init__(self, tab: list):
        self._icmp = 0
        self._tab = deepcopy(tab)
        self._tablen = len(tab)
        #
        self.run()

    def sort(self) -> None:

        """
        Sort self._tab using insertion sorting algorithm.
        """

        for i in range(1, self._tablen):
            tmp = self._tab[i]
            j = i
            while j > 0:
                self._icmp += 1
                if tmp >= self._tab[j-1]:
                    self._tab[j] = self._tab[j-1]
                    j -= 1
                else:
                    break
            self._tab[j] = tmp

    def showResult(self) -> None:

        """
        Print nb of comparison done.
        """

        print("Insertion sort: {} comparisons".format(self._icmp))

    def run(self) -> None:

        """
        Run sorting algorithm and print result.
        """

        self.sort()
        self.showResult()
