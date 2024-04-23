
import unittest


class TestSysPer(unittest.TestCase):
    def test_cpu_count(self):
        count = cpu_count()
        self.assertIsInstance(count, int)
        self.assertGreater(count, 0)

    def test_cpu_times(self):
        times = cpu_times()
        self.assertIsInstance(times, tuple)
        self.assertEqual(len(times), 2)
        self.assertIsInstance(times[0], float)
        self.assertIsInstance(times[1], float)

    def test_disk_per(self):
        per = disk_per()
        self.assertIsInstance(per, float)
        self.assertGreaterEqual(per, 0)
        self.assertLessEqual(per, 100)

    def test_disk_usage(self):
        usage = disk_usage()
        self.assertIsInstance(usage, tuple)
        self.assertEqual(len(usage), 2)
        self.assertIsInstance(usage[0], int)
        self.assertIsInstance(usage[1], int)
        self.assertGreaterEqual(usage[0], 0)
        self.assertGreaterEqual(usage[1], 0)

    def test_mem_per(self):
        per = mem_per()
        self.assertIsInstance(per, float)
        self.assertGreaterEqual(per, 0)
        self.assertLessEqual(per, 100)

if __name__ == '__main__':
    from ..engine.sys_per import *
    unittest.main()


