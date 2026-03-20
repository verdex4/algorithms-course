from linked_list import LinkedList

def contains_target(ll: LinkedList, target: int):
    for x in ll.items():
        if x.value == target:
            return True
    return False

ll = LinkedList([3, 6, 9, 12])
print(contains_target(ll, 9)) # True

ll = LinkedList([1, 3, 2, 8, 11, 15, 33, 22])
print(contains_target(ll, 4)) # False
