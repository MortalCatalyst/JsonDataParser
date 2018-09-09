import collections
import pprint
import operator
from functools import reduce

with open(r"C:\Users\Sayth\OneDrive\Projects\Folder\Results\Randwick_2018-09-05.json", 'rb') as f:
    # pp = pprint.PrettyPrinter(indent=4)
    data = f.read()
    
    def get_paths(source):
        paths = []
        # found a dict-like structure...
        if isinstance(source, collections.MutableMapping):
            for k, v in source.items():  # iterate over it; Python 2.x: source.iteritems()
                paths.append([k])  # add the current child path
                # get sub-paths, extend with the current
                paths += [[k] + x for x in get_paths(v)]
        # else, check if a list-like structure, remove if you don't want list paths included
        elif isinstance(source, collections.Sequence) and not isinstance(source, str):
            #                          Python 2.x: use basestring instead of str ^
            for i, v in enumerate(source):
                paths.append([i])
                # get sub-paths, extend with the current
                paths += [[i] + x for x in get_paths(v)]
        return paths


    def getFromDict(dataDict, mapList):
        return reduce(operator.getitem, mapList, dataDict)


    def setInDict(dataDict, mapList, value):
        getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

    paths = get_paths(data)
    indexes = range(len(paths))

    for index in indexes:
        print(paths[index], getFromDict(data, paths[index]))
