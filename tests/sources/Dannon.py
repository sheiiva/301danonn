############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 301dannon            #
#                                          #
############################################

import os
import re
from copy import deepcopy

from sources.ArgumentManager import ArgumentManager
from sources.sort.SelectionSort import SelectionSort
from sources.sort.InsertionSort import InsertionSort
from sources.sort.BubbleSort import BubbleSort
from sources.sort.QuickSort import QuickSort
from sources.sort.MergeSort import MergeSort


class Dannon():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self, filename: str):
        self._filename = os.path.abspath(filename)
        self._arg = ArgumentManager()
        self._elem = []

    def isValidFile(self) -> bool:

        """
        Open 'file' passed as argument and check for its validity.
        """

        def isEmpty(filename: str) -> bool:

            """
            Check whether a file is empty or not.
            """

            if os.stat(filename).st_size == 0:
                return False
            return True

        if isEmpty(self._filename) is False:
            return False
        with open(self._filename) as f:
            for line in f:
                line = line.replace('\t', ' ')
                line = re.sub(' +', ' ', line).lstrip().rstrip()
                self._elem = line.split(' ')
        f.close()
        return True

    def checkElems(self) -> bool:

        """Expect for each element type of self._elem to be a digit."""

        for elem in self._elem:
            if not self._arg.isFloat(elem):
                return False
        self._elem = [float(i) for i in self._elem]
        return True

    def countElements(self) -> None:

        """
        Count and print input elements.
        """

        nb_elem = len(self._elem)

        print("{} element".format(nb_elem), end='')
        if nb_elem > 1:
            print("s")
        else:
            print()

    def run(self) -> None:

        """
        Run computations and process output printing.
        """

        if self.isValidFile() is False:
            print("Error: can't read input file.")
            exit(84)
        if self.checkElems() is False:
            print("Error: at least one element is not a digit.")
            exit(84)
        self.countElements()
        SelectionSort(self._elem)
        InsertionSort(self._elem)
        BubbleSort(self._elem)
        QuickSort(self._elem)
        MergeSort(self._elem)
