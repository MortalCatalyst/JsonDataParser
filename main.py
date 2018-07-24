import collections
import pprint
from functools import reduce  # forward compatibility for Python 3
import operator


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


data = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages...",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
# pp = pprint.PrettyPrinter(indent=4)
paths = get_paths(data)

indexes = range(len(paths))

for index in indexes:
    print(paths[index], getFromDict(data, paths[index]))
