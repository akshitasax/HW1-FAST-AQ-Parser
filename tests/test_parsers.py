# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa

    Adding a comment to trigger a build
    """
    fasta_object = FastaParser("data/test.fa") #create instance of FastaParser
    first_record = next(iter(fasta_object)) #iterating over the FastaParser object to get the first record
    assert first_record == ("seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA")


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. If a fastq file is
    read, the first item is None
    """
    fasta_object = FastaParser("data/test.fq") #create instance of FastaParser
    first_record = next(iter(fasta_object)) #iterating over the FastaParser object to get the first record
    assert first_record[0] is None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq_object = FastqParser("data/test.fq") #create instance of FastaParser
    first_record = next(iter(fastq_object)) #iterating over the FastaParser object to get the first record
    assert first_record == ("seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG", "\*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32=")

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_object = FastqParser("data/test.fa") #create instance of FastaParser
    first_record = next(iter(fastq_object)) #iterating over the FastaParser object to get the first record
    assert first_record[0] is None