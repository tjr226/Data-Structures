from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.hashmap = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        print(f"incoming key for GET is {key}")
        if key not in self.hashmap:
            return None
        else:
            # move node with key to front of DLL
            # first, need to find that node
            iter_node = self.dll.head
            while key != iter_node.value:
                iter_node = iter_node.next
            # move that node to the front
            self.dll.move_to_front(iter_node)
            # return value from key in hashmap
            return self.hashmap[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.hashmap:
            # when key/value already in hashmap
            # overwrite old key/value pair in hashmap
            self.hashmap[key] = value
            # move key to front of DLL
            # iterate through DLL to find the node matching the key
            iter_node = self.dll.head
            while key != iter_node.value:
                iter_node = iter_node.next
            # move that node to the front
            self.dll.move_to_front(iter_node)
            # explicitly return None to avoid problems
            return None

        # cases when key is not in hashmap (cache)
        if self.dll.length < self.limit:
            # case: key is not in hashmap, room left in cache
            # add key/value to both DLL and hashmap
            self.hashmap[key] = value
            self.dll.add_to_head(key)
            # explicitly return None to avoid problems
            return None
        elif self.dll.length == self.limit:
            # case: key is not in hashmap, also DLL is full
            # delete tail value from DLL and hashmap
            prev_key = self.dll.remove_from_tail()
            del self.hashmap[prev_key]
            # add key/value to both DLL and hashmap
            self.hashmap[key] = value
            self.dll.add_to_head(key)        
