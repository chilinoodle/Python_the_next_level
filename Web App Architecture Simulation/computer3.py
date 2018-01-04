import fake_database

from memcache import Memcache

CACHE = Memcache()


def printname():
    return str(__name__)


def updateLastMultiplied(a,b,result):
    key = "lastFive"
    lastFiveList = CACHE.get(key)
    if lastFiveList:
        if len(lastFiveList) >= 5:
            newList = lastFiveList[1:]
            newList.append("{} X {} = {}".format(a,b,result))
            done = CACHE.set(key, newList)
        else:
            lastFiveList.append("{} X {} = {}".format(a,b,result))
            done = CACHE.set(key, lastFiveList)
    else:
        done = CACHE.set(key, ["{} X {} = {}".format(a,b,result)])


def lastMultipliedHandler():
    """
    Inputs : none
    Outputs : The last 5 multiplied result
    """
    key = "lastFive"
    last = CACHE.get(key)
    if key:
        return "Last 5 = {}".format(last)
    else:
        return "Russian Not Used Before"


def multiplyHandler(a,b):
    """
    Inputs: a,b numbers as arguments from the request
    Outputs: The result of those numbers being sent through the Russian algorithm
    """
    key = (a,b)
    cachedAnswer = CACHE.get(key)
    if cachedAnswer:
        return cachedAnswer
    else:
        result = fake_database.russian(a,b)
        updateLastMultiplied(a,b,result)
        done = CACHE.set(key,result)
        return "Last Result: {}".format(result)
        lastMultipliedHandler()

if __name__ == "__main__":
    multiplyHandler(2, 6)
    multiplyHandler(5, 6)
    multiplyHandler(10, 6)
    multiplyHandler(23, 6)
    multiplyHandler(4, 6)
    multiplyHandler(11, 6)
    multiplyHandler(200, 6)
