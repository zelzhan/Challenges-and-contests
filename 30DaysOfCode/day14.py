class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):			#easy computations of max and min
        self.maximumDifference = max(a) - min(a)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
