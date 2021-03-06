# Copyright 2012 TellApart, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Defines a test suite encompassing all test cases in this and child packages.
"""

from tellapart.testutil import test_suite_manager

from tellapart.storage.engine import redis_engine_test

_ALL_TEST_CASES = {
  'small' : [
    redis_engine_test.RedisTestCase,
  ],
}

_CHILD_TEST_SUITES = [
]

TEST_SUITE_MANAGER = test_suite_manager.TestSuiteManager(_ALL_TEST_CASES,
    _CHILD_TEST_SUITES)

if __name__ == '__main__':
  TEST_SUITE_MANAGER.RunTests()
