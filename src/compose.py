def compose(*funcs):
    def wrapper(*args):
        for func in funcs:
            print(args)
            if hasattr(args, '__iter__'):
                args = func(*args)
            else:
                args = func(args)
        return args
    return wrapper
