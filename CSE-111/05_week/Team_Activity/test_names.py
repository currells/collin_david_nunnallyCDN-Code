"""
Name: Maydens of Mayham (BC, CN, PT, JH, ZM)
Class: CSE-111
Comments:
Test file for names.py
"""

from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("Collin", "Nunnally") == "Nunnally; Collin"
    assert make_full_name("", "") == "; "
    assert make_full_name("Brenden", "Clark-Sir") == "Clark-Sir; Brenden"

def test_extract_name():
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Nunnally; Collin") == "Nunnally"
    assert extract_family_name("; ") == ""
    assert extract_family_name("Clark-Sir; Brenden") == "Clark-Sir"

def test_extract_given_name():
    assert extract_given_name("Washington ; George") == "George"
    assert extract_given_name("Nunnally; Collin") == "Collin"
    assert extract_given_name("; ") == ""
    assert extract_given_name("Clark-Sir; Brenden") == "Brenden"

# Call the main function that is part of pytest so that the computer will execute the test functions in this file. Imported from Team Activity page.
pytest.main(["-v", "--tb=line", "-rN", __file__])