
def formatArgs(args: tuple):
    res = f'{args}'[2:-3]
    if res[-1] == ',':
        res = res[:-1]
    return res
