from unittest import TestCase
import pytest
from src.jdmortgagecalculator import MortgageCalculator

class TestRepayment(TestCase):
    
    def test_repayment(self):
        term  = 25 * 12
        interest_rate = 0.05
        assert True
