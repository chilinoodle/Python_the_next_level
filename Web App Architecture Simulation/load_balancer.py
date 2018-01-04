import computer1
import computer2
import computer3

SERVERS = [computer1, computer2, computer3]

last_server = -1


"""
# My Solution
def get_server1():
    global last_server
    if last_server != len(SERVERS)-1:
        last_server += 1
    else:
        last_server = 0
    return SERVERS[last_server]
"""

# solution 1
n = -1
def get_server():
    global n
    n+=1
    return SERVERS[n % len(SERVERS)]

"""
# solution 2
import itertools
cycle = itertools.cycle(SERVERS)
def get_server2():
    global cycle
    return cycle.next()

# Solution 3
def get_server3():
    def f():
        while True:
            i = SERVERS.pop(0)
            SERVERS.append(i)
            yield i
    return next(f())

# Solution 4
def get_server4():
    try:
        return next(get_server4.s)
    except StopIteration:
        get_server4.s = iter(SERVERS)
        return next(get_server4.s)

setattr(get_server4, "s", iter(SERVERS))
"""
# testing load with generating 9 random requests with
if __name__ == "__main__":
    from random import randint
    for i in range(10):
        z = randint(1,21)
        a = [44,85,123,55,32,34,87][z%7]
        b = [54,15,32,98,311,28,54][z%7]
        # Choosing a server
        server = get_server()
        # Printing the results
        print server.printname()
        print "{} X {} = ".format(a,b)
        print server.multiplyHandler(a,b)
        print server.lastMultipliedHandler()
        print " "