import io_csv, csv
from logger import logger

class CEGASCache:
    def __init__(self):
        """Initializes the cache dict and imports `~/db/csv/*.csv`"""
        self.cache = {} # the cache dict itself

        for key, value in self.__fetch_data().items():
            self.set(key, value) 

    def __fetch_data(self):
        """
        Reads entity .csv files and converts each entity 
        into a list of tuples sorted by PK.\n
        Returns: a map of all tuples with keys 
        named after their respective SQL tables.
        """

        # sets row[0], which contains datatype specifications
        # for datatype conversion purposes
        data = {
            "assessment": [(int, str, int, int, int)], 
            "enrollment": [(int, int, int)], 
            "score": [(int, int, int, float)],
            "student": [(int, int, int, str, str, str)], 
            "section": [(int, int)]
        }

        for key in data:
            with open(io_csv.TOP_PATH + f"/db/csv/{key}.csv") as f:
                # opens appropriate csv file and reads line by line
                for row in list(csv.reader(f)):
                    if not row: continue
                    # converting datatypes
                    for i, datatype in enumerate(data[key][0]):
                        if row[i]: 
                            row[i] = datatype(row[i])
                    data[key].append(tuple(row))

        # cleaning: remove index 0 of all values in `data`
        # and sort by primary key
        for key in data:
            data[key].pop(0) # remove datatypes in index 0
            data[key] = set(data[key]) # remove duplicates through sets
            data[key] = sorted(data[key], key=lambda x: x[0]) # sort set
            logger.tee(f"[INFO] Successfully fetched {key}.csv.")

        return data

    def __contains__(self, cache_key):
        return cache_key in self.cache

    def new_sorted(self, cache_key: str, lst, i: int, reverse=False):
        """Adds a list sorted by attribute index into the cache."""

        self.cache[cache_key] = \
            sorted(lst, key=lambda x: x[i], reverse=reverse)
        
    def get(self, cache_key):
        """Quality-of-Life function for neatness.\n
        Equivalent to `self.cache[cache_key]`"""
        return self.cache[cache_key]
    
    def set(self, cache_key, x):
        """Quality-of-Life function for neatness.\n
        Equivalent to `self.cache[cache_key] = x` + logging"""
        self.cache[cache_key] = x

    def run(self, cache_key, method_name: str, *args):
        """Quality-of-Life function for neatness.\n
        Equivalent to `self.cache[cache_key].method_name(args)` + logging"""
        method = getattr(type(self.cache[cache_key]), method_name)
        method(self.cache[cache_key], args)


    def size_changed(self, cache_key: str, len: int):
        """Check if current size matches cached size. Helps with checking if 
        something changed."""
        return False if len(self.get(cache_key)) == len else True

cache_instance = CEGASCache()