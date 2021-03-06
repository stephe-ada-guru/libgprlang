import os

from testsuite_support.polyfill import BaseTestsuite

import testsuite_support.parser_driver

class Testsuite(BaseTestsuite):
    TEST_SUBDIR = 'tests'
    DRIVERS = {
        'parser': testsuite_support.parser_driver.ParserDriver,
    }

    def add_options(self):
        self.main.add_option(
            '--valgrind', action='store_true',
            help='Run tests within Valgrind to check memory issues.')

        self.main.add_option(
            '--debug', '-g', action='store_true',
            help='Run a test under a debugger'
        )
        self.main.add_option(
            '--debugger', '-G', default='gdb',
            help='Program to use as a debugger (default: gdb)'
        )

        # Tests update
        self.main.add_option(
            '--rewrite', '-r', action='store_true',
            help='Rewrite test baselines according to current output.'
        )

# end of file
