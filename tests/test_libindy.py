import unittest
from indy import ledger

from tests import run_async_test


class TestLibIndy(unittest.TestCase):
    @run_async_test
    async def test_noop_calls_to_libindy(self):
        try:
            txn = await ledger.build_get_nym_request("3QDMzWRNmt5f1UJmkDv6tk", "8YkW6J5Rs7YFfJzTFcW9Lt")
        except:
            print("Unable to call libindy through the Python Wrapper")
            print("Check that you have libindy through system packager -- see: https://github.com/hyperledger/indy-sdk")
            self.fail("libindy did not work!")

if __name__ == '__main__':
    unittest.main()
