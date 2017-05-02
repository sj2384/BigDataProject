import datetime
from matplotlib import path


def get_type(s):
    try:        
        int(s)
        return 'int'
    except ValueError:
        try:
            float(s)
            return 'float'
        except ValueError:
            try:
                datetime.datetime.strptime(s, '%m/%d/%Y')
                return 'datetime'
            except ValueError:
                try:
                    datetime.datetime.strptime(s, '%H:%M:%S')
                    return 'timestamp'
                except ValueError:
                    return 'string'
    
def get_NTA(dic, point):
    d = {}
    for k in dic.keys():
        p = path.Path(dic[k])
        if p.contains_points(point):
            d[k] = 1
    return d