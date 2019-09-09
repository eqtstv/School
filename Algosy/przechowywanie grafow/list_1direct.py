#lista jednokierunkowa

class Value:
    def __init__(self, value):
        self.value = value
        self.next = None

    def return_value(self):
        return self.value

    def return_next(self):
        return self.next

    def update_next(self, value):
        self.next = value


class List(Value):
    def __init__(self):
        self.items = []

    def show_list(self):
        for i in self.items:
            print('Value: ' + str(Value.return_value(i)))
            print('Next: ' + str(Value.return_next(i)))
            print('-----------')

        
    def add_value_sorted(self, item):
        self.items.append(item)

        self.item_index = self.items.index(item)
        self.item_value = Value.return_value(item)

        self.prev_block_index = self.item_index - 1
        self.prev_block_value = Value.return_value(self.items[self.prev_block_index])
        self.prev_block_next = Value.return_next(self.items[self.prev_block_index])

        def swap_positions(list, pos1, pos2):
            list[pos1], list[pos2] = list[pos2], list[pos1]


        for i in range(len(self.items), 1, -1):
            if (self.item_value < self.prev_block_value):
                swap_positions(self.items, self.item_index, self.prev_block_index)

                self.item_index -= 1
                self.prev_block_index = self.item_index - 1

                self.items[self.item_index].update_next(self.prev_block_value)

                self.prev_block_value = Value.return_value(self.items[self.prev_block_index])

            else:
                self.items[self.prev_block_index].update_next(self.item_value)




eg_list = List()


for i in range(0, 10, 2):
    i = Value(i)
    eg_list.add_value_sorted(i)

val1 = Value(1)
val2 = Value(12)

eg_list.add_value_sorted(val1)
eg_list.add_value_sorted(val2)

print('List:')
eg_list.show_list()