import unittest
from tool import find_duplicates, fingerprint

class DuplicateTests(unittest.TestCase):
    def test_canonical_order_and_groups(self):
        self.assertEqual(fingerprint({"a":1,"b":2}), fingerprint({"b":2,"a":1}))
        groups = find_duplicates([{"a":1}, {"a":2}, {"a":1}])
        self.assertEqual(list(groups.values()), [[0, 2]])

if __name__ == "__main__": unittest.main()
