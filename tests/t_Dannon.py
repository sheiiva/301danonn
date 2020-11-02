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

from sources.Dannon import Dannon


def test_countElemnts_normalcase(capsys):

    dannon = Dannon("tests/deps/normal_file")

    dannon._elem = [1, 2, 3]
    dannon.countElements()

    redir = capsys.readouterr()
    expected = "3 elements\n"

    assert redir.out == expected


def test_countElemnts_one_element(capsys):

    dannon = Dannon("tests/deps/normal_file")

    dannon._elem = [3]
    dannon.countElements()

    redir = capsys.readouterr()
    expected = "1 element\n"

    assert redir.out == expected


def test_countElemnts_no_element(capsys):

    dannon = Dannon("tests/deps/normal_file")

    dannon._elem = []
    dannon.countElements()

    redir = capsys.readouterr()
    expected = "0 element\n"

    assert redir.out == expected


def test_checkElems_normal_case():

    dannon = Dannon("tests/deps/normal_file")

    dannon._elem = [1, 2, 3]
    ret = dannon.checkElems()

    assert ret is True


def test_checkElems_wrong_case():

    dannon = Dannon("tests/deps/normal_file")

    dannon._elem = [1, 'a', 3]
    ret = dannon.checkElems()

    assert ret is False


def test_checkElems_empty_case():

    dannon = Dannon("tests/deps/normal_file")

    dannon._elem = []
    ret = dannon.checkElems()

    assert ret is True


def test_isValidFile_normal_case():

    dannon = Dannon("tests/deps/normal_file")

    expected_elem = ['0', '-1', '9.2', '-28383', '222']
    ret = dannon.isValidFile()

    assert ret is True
    for i in range(len(dannon._elem)):
        assert dannon._elem[i] == expected_elem[i]


def test_isValidFile_empty_case():

    dannon = Dannon("tests/deps/empty_file")

    ret = dannon.isValidFile()

    assert ret is False


def test_isValidFile_tricky_case():

    dannon = Dannon("tests/deps/tricky_file")

    expected_elem = ['0', '-1', '9.2', '-28383', '222']
    ret = dannon.isValidFile()

    assert ret is True
    for i in range(len(dannon._elem)):
        assert dannon._elem[i] == expected_elem[i]
