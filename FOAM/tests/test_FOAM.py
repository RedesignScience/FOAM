"""
Unit and regression test for the FOAM package.
"""

# Import package, test suite, and other packages as needed
import FOAM
import pytest
import sys

def test_FOAM_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "FOAM" in sys.modules
