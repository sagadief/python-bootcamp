def decorated_func(func):
    def wrapper(purse):
        print("SQUEAK")
        return func(purse)
    return wrapper