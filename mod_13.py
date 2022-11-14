import unittest
import datetime

"""

TO RUN, IN TERMINAL python -m unittest mod_13.py
(or whatever the file name is and youre in the right directory)

"""

def getSymbol():
    symbol = input("Enter symbol, capitalized, 1-7 alpha characters: ")
    return symbol
def getChartType():
    chart_type = input("Enter either a 1 or a 2: ")
    return chart_type
def getTimeSeries():
    time_series = input("Enter a number 1 - 4: ")
    return time_series
def getStartDate():
    start_date = input("Enter a date formatted YYYY-MM-DD: ")
    return start_date
def geetEndDate():
    end_date = input("Enter a date formatted YYYY-MM-DD: ")
    return end_date

def getInput():
#    symbol = input("Enter symbol, capitalized, 1-7 alpha characters: ")
#    chart_type = input("Enter either a 1 or a 2: ")
#    time_series = input("Enter a number 1 - 4: ")
#    start_date = input("Enter a date formatted YYYY-MM-DD: ")
#    end_date = input("Enter a date formatted YYYY-MM-DD: ")
    return [symbol, chart_type, time_series, start_date, end_date]

class Tests(unittest.TestCase):
    def test_symbolIsValid(self):
        symbol = getSymbol()
        self.assertEqual(symbol.isupper(),True)
    def test_chartTypeIsValid(self):
        chart_type = getChartType()
        self.assertTrue(int(chart_type) == 1 or int(chart_type) == 2)
    def test_timeSeriesIsValid(self):
        time_series = getTimeSeries()
        self.assertIn(int(time_series), range(1, 5))
    def test_startDateIsValid(self):
        start_date = getStartDate()
        year, month, day = start_date.split('-')[0], start_date.split('-')[1], start_date.split('-')[2]
        self.assertTrue(len(year) == 4)
        self.assertTrue(len(month) == 2)
        self.assertTrue(int(month) <= 12 and int(month) > 0)
        self.assertTrue(len(day) == 2)
        self.assertTrue(int(day) <= 31 and int(day) > 0)
    def test_endDateIsValid(self):
        end_date = getStartDate()
        year, month, day = end_date.split('-')[0], end_date.split('-')[1], end_date.split('-')[2]
        self.assertTrue(len(year) == 4)
        self.assertTrue(len(month) == 2)
        self.assertTrue(int(month) <= 12 and int(month) > 0)
        self.assertTrue(len(day) == 2)
        self.assertTrue(int(day) <= 31 and int(day) > 0)
        
    
