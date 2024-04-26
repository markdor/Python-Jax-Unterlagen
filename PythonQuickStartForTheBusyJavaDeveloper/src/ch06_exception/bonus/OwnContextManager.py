# https://towardsdatascience.com/how-to-build-custom-context-managers-in-python-31727ffe96e1

def myfunction():
    print("MY FUNC")


class OwnContextManager:
    def __enter__(self):
        print("ENTERING")

    def __exit__(self, type, value, traceback):
        print("EXITiNG")


with OwnContextManager() as owm:
    myfunction()

# with VAR = EXPR:
#    BLOCK

# VAR = EXPR
# VAR.__enter__()
# try:
#     BLOCK
# finally:
#     VAR.__exit__()
