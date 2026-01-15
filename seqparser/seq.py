# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # Initially started by looping over the sequence and replacing each character. 
    # Then looked up more efficient ways to replace characters in a string according to a mapping, and came across
    # the translate method for strings.
    transcription_table = str.maketrans(TRANSCRIPTION_MAPPING)
    return seq.translate(transcription_table)

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    transcription_table = str.maketrans(TRANSCRIPTION_MAPPING)
    return seq.translate(transcription_table)[::-1] # string slicing to iterate over a sequence in reverse steps of 1.