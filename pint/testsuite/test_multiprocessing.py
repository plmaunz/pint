from multiprocessing import Process, Queue
from pint import UnitRegistry, set_application_registry
from pint.testsuite import QuantityTestCase

ureg = UnitRegistry()
set_application_registry(ureg)
Q = ureg.Quantity


def f(to_child, to_parent):
    one, two = to_child.get()
    to_parent.put(one / two)


class TestIssues(QuantityTestCase):

    def test_multiprocessing(self):
        to_child = Queue()
        to_parent = Queue()
        p = Process(target=f, args=(to_child, to_parent))
        p.start()
        t1 = Q(50, 'ms')
        t2 = Q(50, ' ns')
        to_child.put((t1, t2))
        result = to_parent.get()
        self.assertEqual(result, t1 / t2)
        self.assertEqual(int(round(float(result))), 1000000)
        p.join()