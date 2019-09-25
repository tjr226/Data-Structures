import math

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)

        index = len(self.storage) - 1

        if index == 0:
            self._bubble_up(index)
            
        while index is not 0:
            # print(self.storage)
            parent_index = self._parent_index(index)
            # print(f"val index {index}, parent index {parent_index}")
            if self.storage[parent_index] < self.storage[index]:
                self._bubble_up(index)
                index = parent_index
            else:
                break

        return

    def delete(self):
        # self._sift_down(len(self.storage) - 1)
        # print(self.storage)
        if len(self.storage) == 1:
            deleted_value = self.storage[0]
            self.storage.pop()
        else:
            deleted_value = self.storage[0]
            self.storage[0] = self.storage.pop()

        index = 0

        while index is not None:
            # print("index is not none in self.delete, index is ", index)
            index = self._sift_down(index)
            # print("new index is", index)

        # print(self.storage)
        return deleted_value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return

        parent_index = self._parent_index(index)
        self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]

    def _sift_down(self, index):
        # print("sift down is running")
        # returns None if there's no more need to sift down
        # otherwise, returns the position that the old index was swapped to
        left_index = self._left_index(index)
        right_index = self._right_index(index)

        if left_index == None:
            # CASE: no left or right children
            # don't need to check for right index. if no left index, no right index
            return None
        elif right_index == None:
            # CASE: only left child
            if self.storage[left_index] > self.storage[index]:
                self.storage[left_index], self.storage[index] = self.storage[index], self.storage[left_index]
            return None
        else:
            # CASES: two children
            # find greater child
            if self.storage[left_index] > self.storage[right_index]:
                max_child_index = left_index
            else:
                max_child_index = right_index
            # sift down if necessary
            if self.storage[max_child_index] > self.storage[index]:
                # swap values, need to check again
                self.storage[max_child_index], self.storage[index] = self.storage[index], self.storage[max_child_index]
                return max_child_index
            else:
                # return True
                return None


       

        




    def _parent_index(self, index):
        if index == 0:
            return None
        else:
            # print(f"index is {index}, ceiling is {math.ceil(index - 2 / 2)}")
            # print("is this being accessed?")
            # if index % 2 == 0:
            #     return (index - 2 / 2)
            # else:
            #     return math.ceil(index - 2 / 2)
            parent_index = (index - 2 ) / 2
            # print(f"index is {index}, parent is {parent_index}")
            # print(f" parent ceil is {math.ceil(parent_index)}")
            if parent_index % 2 != 0:
                # print("in odd numbers")
                parent_index = math.ceil(parent_index)
            # print("new parent index", parent_index)
            return int(parent_index)

    def _left_index(self, index):
        left_index = (index * 2) + 1
        if left_index > len(self.storage) - 1:
            return None
        else:
            return left_index

    def _right_index(self, index):
        right_index = (index * 2) + 2
        if right_index > len(self.storage) - 1:
            return None
        else:
            return right_index

# test_heap = Heap()

# test_heap.insert(4)

# test_heap = Heap(11)
# test_heap.insert(5)
# test_heap.delete()

# test_heap.insert(1)

# test_heap.insert(10)

# test_heap.insert(7)

# test_heap.insert(3)
# print(test_heap.delete())
# print(test_heap.delete())

# print(test_heap.delete())

# print(test_heap.delete())

# print(test_heap.delete())
# for i in range(20):
    # print("output in for loop", i, test_heap._parent_index(i))
    # test_heap._parent_index(i)
    # print("in the loop")