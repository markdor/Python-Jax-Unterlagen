sample_names = ["TIM", "TOM", "MIKE", "JOHN", "MICHAEL", "STEFAN"]
has_odd_length = lambda str: len(str) % 2 != 0  # violates PEP 8

only_odd_length = list(filter(has_odd_length, sample_names))
print(only_odd_length)

only_even_length = list(filter(lambda str: not has_odd_length(str), sample_names))
print(only_even_length)
