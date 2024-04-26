class StaticExample:
    static_info = "Class wide info"

    @staticmethod
    def generate_info():
        print("static methods can be called without creating objects")
        return "Special Information"

    def object_method(self):
        print("object methods must be called on objects")
        print("static methods/variables are accessible")
        return StaticExample.static_info
