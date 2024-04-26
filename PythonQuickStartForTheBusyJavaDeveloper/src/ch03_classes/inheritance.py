class BaseClass:
    def method(self):
        print("called method")

    def other_method(self):
        pass


class SubClass(BaseClass):
    def method(self):
        super().method()
        # weitere Aktionen
        print("other actions")

    # Zusätzliche Funktionalität
    def additional_method(self):
        pass