def f21(x):
    if x[0] == 1972:
        if x[3] == 2015:
            if x[2] == 'rebol':
                return 0
            if x[2] == 'ampl':
                return 1
        if x[3] == 1992:
            if x[4] == 'r':
                if x[1] == 1984:
                    return 2
                if x[1] == 2017:
                    return 3
                if x[1] == 2004:
                    return 4
            if x[4] == 'ston':
                if x[2] == 'rebol':
                    return 5
                if x[2] == 'ampl':
                    return 6
            if x[4] == 'http':
                return 7
    if x[0] == 1969:
        if x[1] == 1984:
            return 8
        if x[1] == 2004:
            return 11
        if x[1] == 2017:
            if x[3] == 2015:
                return 9
            if x[3] == 1992:
                return 10
    if x[0] == 1985:
        return 12

f21()