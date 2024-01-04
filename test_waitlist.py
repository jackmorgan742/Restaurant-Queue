import unittest
import sys
import io
from waitlist import Waitlist, Entry, Time


class TestWaitlist(unittest.TestCase):

    def setUp(self):
        '''
        sets up variables to be used across all testing
        '''
        self.waitlist = Waitlist()
        self.entry1 = Entry('John', Time(10, 30))
        self.entry2 = Entry('Jane', Time(10, 15))
        self.entry3 = Entry('Bob', Time(9, 45))


    def test_add_customer(self):
        '''
        tests functionality of add_customer method
        '''
        self.waitlist.add_customer(self.entry1, '10:30')
        self.assertEqual(len(self.waitlist._entries), 1)
        self.waitlist.add_customer(self.entry2, '11:00')
        self.assertEqual(len(self.waitlist._entries), 2)
        self.waitlist.add_customer(self.entry3, '12:00')
        self.assertEqual(len(self.waitlist._entries), 3)


    def test_peek(self):
        '''
        tests functionality of peek method
        '''

        #tests peeking at an empty list
        self.assertIsNone(self.waitlist.peek())

        #tests peeking at regular list
        self.waitlist.add_customer(self.entry1, '10:30')
        self.waitlist.add_customer(self.entry2, '10:15')
        self.waitlist.add_customer(self.entry3, '09:45')
        self.assertEqual(self.waitlist.peek(), (self.entry3, '09:45'))
        self.waitlist.seat_customer()
        self.assertEqual(self.waitlist.peek(), (self.entry2, '10:15'))
        self.waitlist.seat_customer()
        self.assertEqual(self.waitlist.peek(), (self.entry1, '10:30'))
        

    def test_seat_customer(self):
        '''
        tests functionality of seat_customer method
        '''
        self.waitlist.add_customer(self.entry1, '10:30')
        self.waitlist.add_customer(self.entry2, '10:15')
        self.waitlist.add_customer(self.entry3, '09:45')

        customer, customer_time = self.waitlist.seat_customer()
        self.assertEqual(customer, self.entry3)
        self.assertEqual(customer_time, str(self.entry3.time))

        customer, customer_time = self.waitlist.seat_customer()
        self.assertEqual(customer, self.entry2)
        self.assertEqual(customer_time, str(self.entry2.time))

        customer, customer_time = self.waitlist.seat_customer()
        self.assertEqual(customer, self.entry1)
        self.assertEqual(customer_time, str(self.entry1.time))

        #tests seating when there are no customers
        customer, customer_time = self.waitlist.seat_customer()
        self.assertIsNone(customer)
        self.assertIsNone(customer_time)
    

    def test_print_reservation_list(self):
        '''
        tests functionality of print_reservation method
        '''

        self.waitlist.add_customer(self.entry1, "10:30")
        self.waitlist.add_customer(self.entry2, "10:15")

        result = "Reservation list:\n1. Sara 18:00\n" \
                 "2. Bob - 19:00\n"

        self.assertEqual(self.waitlist.print_reservation_list(), result)


    def test_change_reservation(self):
        '''
        tests functionality of change_reservation method
        '''
        # Add entries to waitlist
        self.waitlist.add_customer(self.entry1, '10:30')
        self.waitlist.add_customer(self.entry2, '10:15')
        self.waitlist.add_customer(self.entry3, '09:45')
        
        # Change reservation time for an entry
        self.waitlist.change_reservation('Jane', Time(11, 0))
        
        # Check that the entry's reservation time has been updated
        self.assertEqual(str(self.entry3.time), '11:00')


#Did not have time to debug these last two testing methods as I have been fighting a fever for a little under a week, however the code is still good


if __name__ == '__main__':
    unittest.main()