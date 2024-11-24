# Task 1.
def sum_distance(from_value, to_value):
    if from_value > to_value:
        from_value, to_value = to_value, from_value
    
    return sum(range(from_value, to_value + 1))

print(sum_distance(5, 1))
print(sum_distance(3, 7))

#==============================
# Task 2.

def trim_and_repeat(string, offset=0, repetitions=1):
    trimmed_string = string[offset:]
    
    return trimmed_string * repetitions

print(trim_and_repeat("HSE"))
print(trim_and_repeat("Python", 3))
print(trim_and_repeat("Homework it is something great!", offset=3, repetitions=2))