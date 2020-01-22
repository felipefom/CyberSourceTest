import unittest
from service.authorize_transaction import authorize_payment
from service.capture_transaction import get_transaction
from service.decision_manager import decision_manager_with_buyer_information

class TestStringMethods(unittest.TestCase):

    def test_authorize_payment(self):
        result = authorize_payment(False)
        self.assertEqual(result, 201)

    def test_get_transaction(self):
        result = get_transaction()
        self.assertEqual(result, 200)

    def test_decision_manager_with_buyer_information(self):
        result = decision_manager_with_buyer_information()
        self.assertEqual(result, 201)


if __name__ == '__main__':
    unittest.main()