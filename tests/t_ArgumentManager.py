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

from sources.ArgumentManager import ArgumentManager


def test_isFloat_normal_case():

    argman = ArgumentManager()

    assert argman.isFloat(3.2) is True


def test_isFloat_int_case():

    argman = ArgumentManager()

    assert argman.isFloat(3) is True


def test_isFloat_wrong_case():

    argman = ArgumentManager()

    assert argman.isFloat('a') is False


def test_isFloat_negative_case():

    argman = ArgumentManager()

    assert argman.isFloat(-2) is True


def test_needHelp_h_case():

    argman = ArgumentManager()

    argv = ['binary', '-h']

    assert argman.needHelp(argv) is True


def test_needHelp_help_case():

    argman = ArgumentManager()

    argv = ['binary', '--help']

    assert argman.needHelp(argv) is True


def test_needHelp_wrong_case():

    argman = ArgumentManager()

    argv = ['binary', 'path']

    assert argman.needHelp(argv) is False


def test_checkArgs_normal_case():

    argman = ArgumentManager()

    argv = ['binary', 'tests/deps/normal_file']

    assert argman.checkArgs(argv) == 0


def test_checkArgs_wrong_path(capsys):

    argman = ArgumentManager()

    argv = ['binary', 'wrong path']

    assert argman.checkArgs(argv) == 84
    redir = capsys.readouterr()

    excepted = "wrong path is not a valid file\n"
    assert redir.out == excepted


def test_checkArgs_wrong_argv(capsys):

    argman = ArgumentManager()

    argv = ['binary', 'tests/deps/normal_file', 'third']

    assert argman.checkArgs(argv) == 84
    redir = capsys.readouterr()

    excepted = "Wrong number of arguments.\n"
    assert redir.out == excepted
