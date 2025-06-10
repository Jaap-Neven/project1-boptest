# -*- coding: utf-8 -*-
"""
This module runs tests for multizone_office_complex_air.  To run these tests, testcase
multizone_office_complex_air must already be deployed.

"""

import unittest
import os
import utilities

class Run(unittest.TestCase, utilities.partialTestTimePeriod):
    '''Tests the example test case.

    '''

    def setUp(self):
        '''Setup for each test.

        '''

        self.name = 'multizone_office_complex_air'
        self.url = 'http://127.0.0.1:5000'
        self.points_check = ['hva_reaChiWatSys_reaPChi_y', 'hva_reaHotWatSys_reaPBoi_y',
                            'hva_reaChiWatSys_reaPPum_y','hva_reaChiWatSys_reaPCooTow_y',
                            'hva_reaHotWatSys_reaPPum_y',
                             'hva_floor1_reaZonCor_TZon_y', 'hva_floor1_reaZonNor_TZon_y',
                             'hva_floor2_reaZonEas_TZon_y','hva_floor3_reaZonWes_TZon_y',
                             'hva_floor1_reaAhu_TMix_y','hva_floor2_reaAhu_TMix_y','hva_floor3_reaAhu_TMix_y',
                             'loaEnePlu_weaSta_reaWeaTDryBul_y', 'loaEnePlu_weaSta_reaWeaHGloHor_y']

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

        self.name = 'multizone_office_complex_air'
        self.url = 'http://127.0.0.1:5000'
        self.step_ref = 3600
        self.test_time_period = 'peak_heat_day'
        #<u_variable>_activate is meant to be 0 for the test_advance_false_overwrite API test
        self.input = {'hva_floor1_TSupAirSet_activate': 0,
                      'hva_floor1_TSupAirSet_u': 273.15 + 22}
        self.measurement = 'hva_reaHotWatSys_reaPBoi_y'
        self.forecast_point = 'EmissionsElectricPower'

if __name__ == '__main__':
    utilities.run_tests(os.path.basename(__file__))
