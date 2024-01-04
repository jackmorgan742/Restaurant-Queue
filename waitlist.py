import random

class Time:

    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)


    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    

    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False


    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"



class Entry:

    """A class that represents a customer in the _entries"""
    def __init__(self, name, time):
        self.name = name
        self.time = time


    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

    
class Waitlist:

    def __init__(self):
        '''
        Initializes instance variable so entries can be added to a list
        '''
        self._entries = []


    def add_customer(self, item, priority):
        '''
        Add customers to the waiting list
        item: customer name
        priority: reservation time in the format HH:MM
        '''
        time = Time(*priority.split(':'))
        entry = Entry(item, time)
        self._entries.append(entry)
        self._percolate_up(len(self._entries) - 1)


    def peek(self):
        '''
        Peek and see the first customer in the _entries (i.e., the customer with the highest priority)
        Return a tuple of the extracted item (customer, time). Return None if the heap is empty
        '''
        if len(self._entries) == 0:
            return None
        return (self._entries[0].name, str(self._entries[0].time))


    def seat_customer(self):
        '''
        Extracts the customer with the highest priority (i.e., the earliest reservation time) from the priority queue.
        Return a tuple of the extracted item (customer, time)
        '''

        if len(self._entries) == 0:
            return (None, None)
        entry = self._entries[0]
        self._entries[0] = self._entries[-1]
        self._entries.pop()
        self._percolate_down(0)
        return (entry.name, str(entry.time))


    def print_reservation_list(self):
        '''
        Prints all customers in order of their priority (reservation time)
        '''
        if not self._entries:
            print("No customers in waitlist.")
        else:
            print("Reservation list:")
            for reservation_time, _, name in self._entries:
                print(f"{name}, {reservation_time}")
    

    def change_reservation(self, name, new_priority):
        '''
        Change the reservation time (priority) for the customer with the given name
        name: the name of the customer
        new_priority: the new reservation time in the format HH:MM
        '''
        customer = None
        for i in range(len(self._entries)):
            if self._entries[i].name == name:
                customer = self._entries[i]
                break

        if not customer:
            return f"Customer {name} not found in the waitlist."

        customer.reservation_time = new_priority
        self._percolate_down(i)


    def _percolate_up(self, i):
        '''
        Move the entry at index i up the heap until the heap order property is restored
        '''
        while i > 0:
            parent = (i - 1) // 2
            if self._entries[i] < self._entries[parent]:
                self._entries[i], self._entries[parent] = self._entries[parent], self._entries[i]
                i = parent
            else:
                break


    def _percolate_down(self, i):
        '''
        Move the entry at index i down the heap until the heap order property is restored
        '''
        while 2 * i + 1 < len(self._entries):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            min_child = left_child
            if right_child < len(self._entries) and self._entries[right_child] < self._entries[left_child]:
                min_child = right_child
            if self._entries[i] > self._entries[min_child]:
                self._entries[i], self._entries[min_child] = self._entries[min_child], self._entries[i]
                i = min_child
            else:
                break