class CustomerNotFoundException(Exception):
    pass


class CustomerNotFoundException(Exception):
    def __init__(self, customer_id, customer_name):
         self.id = customer_id
         self.name = customer_name

    def __str__(self):
        return "customer {} with id {} not found".format(self.name, self.id)


class ValueOutOfBoundsError(ValueError):
    def __init__(self, value, lower, upper):
         self.value = value
         self.lower = lower
         self.upper = upper

    def __str__(self):
        return "{} not in {} - {}".format(self.value, self.lower, self.upper)



