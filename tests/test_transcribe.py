# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    transcribed_seq = transcribe("ACTNG")
    assert transcribed_seq == "UGANC"

def test_transcribe_unallowed_chars():
    """
    Write your unit test for the transcribe function here.
    """
    transcribed_seq = transcribe("A.CNNGT")
    assert transcribed_seq == "U.GNNCA"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    rev_transcribed_seq = reverse_transcribe("ACTNG")
    assert rev_transcribed_seq == "CNAGU"

def test_reverse_transcribe_unallowed_chars():
    """
    Write your unit test for the reverse transcribe function here.
    """
    rev_transcribed_seq = reverse_transcribe("NGC.NA")
    assert rev_transcribed_seq == "UN.GCN"

