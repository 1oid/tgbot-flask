registry = {}


class register(object):

    @staticmethod
    def setcommand(text):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            registry[text] = wrapper
            return wrapper

        return decorator


# @setcommand("/help")
# def _help(message):
#     print(message)


# _help("aa")
# text = "/help"
# print(registry[text]("aaa"))
