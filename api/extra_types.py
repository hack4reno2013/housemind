def make_tuple(s,t=int):
    return tuple(map(t,(s[1:-1].split(','))))

def is_t(s,t):
    try:
        t(s)
        return True
    except ValueError:
        return False

def is_t_pair(s,t):
    try:
        tup = make_tuple(s,t)
        if(len(tup) == 2):
            return True
        else:
            return False
    except:
        return False

#returns either a value 
def either_t_or_pair(value,t):
    if is_t(value,t):
        return t(value)
    elif is_t_pair(value,t):
        return make_tuple(value,t)
    else:
        raise ValueError("is not an int_range")

def int_range(value):
    return either_t_or_pair(value,int)

def float_range(value):
    return either_t_or_pair(value,float)
