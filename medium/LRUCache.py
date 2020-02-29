# Minci
# time elapsed: 54 min
# submitted 5 times


class LRUCache:

    def __init__(self, capacity: int):
        self.queue = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not self.queue:
            return -1

        for i in range(len(self.queue)):
            if key in self.queue[i]:
                result_pair = self.queue[i]
                self.queue.pop(i)
                self.queue.append(result_pair)
                # self.queue[-1], self.queue[i] = self.queue[i], self.queue[-1]
                # print("refreshing LRU: " + str(self.queue))
                return result_pair[key]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.queue)):
            if key in self.queue[i]:
                self.queue[i][key] = value
                result_pair = self.queue[i]
                self.queue.pop(i)
                self.queue.append(result_pair)
                # print(self.queue)
                return

        if len(self.queue) == self.capacity:
            self.queue.pop(0)
            self.queue.append({key: value})
            # print(self.queue)
        else:
            self.queue.append({key: value})
            # print(self.queue)


# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)