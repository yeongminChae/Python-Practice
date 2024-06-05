from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution1(head: ListNode) -> bool:
    # 연결리스트를 일반 배열로 변경 후 풀이하는 방법
    q: list = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


def solution2(head: ListNode) -> bool:
    # 연결리스트를 데크를 이용한 최적화
    q: deque = deque()

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(2)
node_4 = ListNode(1)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

head = node_1
print(solution1(head))


def selfPrac(head: ListNode):
    q: list = []
    deq: deque = deque()
    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        deq.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
        if deq.popleft() != deq.pop():
            return False

    return True
