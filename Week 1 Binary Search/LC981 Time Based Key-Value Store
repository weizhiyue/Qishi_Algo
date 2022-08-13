class TimeMap(object):

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key, timestamp):
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
