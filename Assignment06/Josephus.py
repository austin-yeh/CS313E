import sys


class Link(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList(object):
    # Constructor
    def __init__(self):
        self.head = None

    # Insert an element (value) in the list
    def insert(self, data):
        if self.head is None:
            self.head = Link(data)
            self.head.next = self.head
        else:
            curr_link = self.head
            while curr_link.next != self.head:
                curr_link = curr_link.next
            curr_link.next = Link(data)
            curr_link.next.next = self.head

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            return self.head
        curr_link = self.head
        while curr_link.next != self.head:
            if curr_link.data == data:
                return curr_link
            curr_link = curr_link.next
        if curr_link.data == data:
            return curr_link
        return None

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        if self.find(data) is None:
            return Link(data)
        if self.head.data == data:
            tmp = self.head
            if self.head.next == self.head:
                self.head = None
                return tmp
            self.head = self.head.next
            curr_link = self.head
            while curr_link.next != tmp:
                curr_link = curr_link.next
            curr_link.next = self.head
            return tmp
        curr_link = self.head
        while curr_link.next != self.head:
            if curr_link.next.data == data:
                tmp = curr_link.next
                curr_link.next = curr_link.next.next
                return tmp
            curr_link = curr_link.next
        return None

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        curr_link = start
        for i in range(n-1):
            curr_link = curr_link.next
        deleted = self.delete(curr_link.data)
        return [deleted, deleted.next]

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if not self.head:
            return '[]'
        else:
            strng = '['
            curr_link = self.head
            while curr_link.next != self.head:
                strng += str(curr_link.data) + ', '
                curr_link = curr_link.next
            strng += str(curr_link.data) + ']'
            return strng


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    clst = CircularList()
    for i in range(1, num_soldiers+1):
        clst.insert(i)
    tmp = [None, clst.find(start_count)]
    for i in range(num_soldiers):
        tmp = clst.delete_after(tmp[1], elim_num)
        print(tmp[0].data)


if __name__ == "__main__":
    main()
