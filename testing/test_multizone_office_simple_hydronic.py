# -*- coding: utf-8 -*-
"""
This module runs tests for multizone_office_simple_hydronic.  To run these tests, testcase
multizone_office_simple_hydronic must already be deployed.

"""

import unittest
import os
import utilities
import requests

class Run(unittest.TestCase, utilities.partialTestTimePeriod):
    '''Tests the example test case.

    '''

    def setUp(self):
        '''Setup for each test.

        '''

        self.name = 'multizone_office_simple_hydronic'
        self.url = 'http://127.0.0.1:80'
        self.points_check = ['heating_cooling_reaPProCoo_y', 'heating_cooling_reaPProHea_y',
                             'structure_reaTZonNz_y', 'structure_reaTZonSz_y',
                             'structure_reaCO2ZonNz_y', 'structure_reaCO2ZonSz_y',
                             'ventilation_reaPAhuSupNz_y', 'ventilation_reaPAhuSupSz_y',
                             'bms_oveTZonSetMinNz_u', 'bms_oveTZonSetMinSz_u',
                             'bms_oveTZonSetMaxNz_u', 'bms_oveTZonSetMaxSz_u',
                             'weaSta_reaWeaTDryBul_y', 'weaSta_reaWeaHGloHor_y']
        self.testid = requests.post("{0}/testcases/{1}/select".format(self.url, self.name)).json()["testid"]

    def tearDown(self):
        requests.put("{0}/stop/{1}".format(self.url, self.testid))

    def test_peak_heat_day(self):
        self.run_time_period('peak_heat_day')

    def test_peak_cool_day(self):
        self.run_time_period('peak_cool_day')

    def test_typical_heat_day(self):
        self.run_time_period('typical_heat_day')

    def test_typical_cool_day(self):
        self.run_time_period('typical_cool_day')

    def test_mix_day(self):
        self.run_time_period('mix_day')

class API(unittest.TestCase, utilities.partialTestAPI):
    '''Tests the api for testcase.

    Actual test methods implemented in utilities.partialTestAPI.  Set self
    attributes defined there for particular testcase in setUp method here.

    '''

    def setUp(self):
        '''Setup for testcase.

        '''

        self.name = 'multizone_office_simple_hydronic'
        self.url = 'http://127.0.0.1:80'
        self.step_ref = 3600
        self.test_time_period = 'peak_heat_day'
        self.input = {'bms_oveByPassNz_activate':0,
                      'bms_oveByPassNz_u':0.5}
        self.measurement = 'heating_cooling_reaPFcuNz_y'
        self.forecast_point = 'EmissionsElectricPower'
        self.testid = requests.post("{0}/testcases/{1}/select".format(self.url, self.name)).json()["testid"]

    def tearDown(self):
        requests.put("{0}/stop/{1}".format(self.url, self.testid))

if __name__ == '__main__':
    utilities.run_tests(os.path.basename(__file__))
