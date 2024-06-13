def calculate_structure_sum(*args):
    a = 0
    for i in args:
        if isinstance(i, int):
            a += i
        elif isinstance(i, str):
            a += len(i)
        elif isinstance(i, dict):
            a += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, set, tuple)):
            a += calculate_structure_sum(*i)
    return a


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'dram': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

result = calculate_structure_sum(data_structure)
print(result)
