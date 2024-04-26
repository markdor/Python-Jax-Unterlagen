class MyClass:
    def __init__(self):
        self.attr = 7271
        self.info = "This is PUBLIC"
        self.__private_info = "My birthday"

    def get_private_info(self):
        return self.__private_info


obj = MyClass()
print("hasattr()")
print(hasattr(obj, "__init__"))
print(hasattr(obj, "info"))
print(hasattr(obj, "__private_info"))
print(hasattr(obj, "_MyClass__private_info"))
print(hasattr(obj, "unknown"))

print("getattr()")
print(getattr(obj, "__init__"))
print(getattr(obj, "attr"))
print(getattr(obj, "info"))
print(getattr(obj, "unknown", "FALLBACK"))

print("callable()")
print(callable(getattr(obj, "__init__")))
print(callable(getattr(obj, "get_private_info")))
print(callable(getattr(obj, "attr")))

print("setattr()")
setattr(obj, "attr", 1234)
setattr(obj, "info", "PIN-CODE")
setattr(obj, "_MyClass__private_info", "!!UNEXPECTED!!")
print(obj.attr)
print(obj.info)
print(obj._MyClass__private_info)