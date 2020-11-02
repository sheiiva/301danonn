############################################
#                MATHEMATICS               #
############################################
#                                          #
#           COUTRET-ROZET Corentin         #
#                                          #
#           Project : 301dannon            #
#                                          #
############################################

import pytest

from sources.Usage import Usage


def test_show(capsys):

    Usage()

    redir = capsys.readouterr()
    expected = "\
USAGE\n\
\t./301dannon file\n\
DESCRIPTION\n\
\tfile\tfile that contains the numbers to be sorted, separated by spaces.\n"

    assert redir.out == expected
