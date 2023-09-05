from collections import Counter, namedtuple, deque

"""
Counter
a = 'aaabbbbccccc'

myc = Counter(a)

print(myc)

print(myc.most_common(1)[0][1])"""

"""#namedtuple

Point = namedtuple('Point','x,y')
pt = Point(1, -22)
print(pt.x, pt.y) """

#deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)