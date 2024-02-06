class Stack:
    def __init__(self, some_list = None):
        if some_list is None:
            some_list = list()
        self.stack = some_list

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Стек пуст"

    def size(self):
        return len(self.stack)


def bracket_balance(bracket_string):
    brackets_pair = {
        "]": "[",
        ")": "(",
        "}": "{",
    }
    brackets = Stack(list(bracket_string))
    sort_brackets = Stack()
    sort_brackets.push(brackets.pop())
    for i in range(brackets.size()):
        if not sort_brackets.is_empty():
            if sort_brackets.peek() not in brackets_pair.keys():
                break
            if brackets.peek() == brackets_pair[sort_brackets.peek()]:
                brackets.pop()
                sort_brackets.pop()
            else:
                sort_brackets.push(brackets.pop())
        else:
            sort_brackets.push(brackets.pop())
    if brackets.is_empty():
        print("Сбалансированно")
    else:
        print("Несбалансированно")


if __name__ == '__main__':
    while True:
        bracket_balance(input())

