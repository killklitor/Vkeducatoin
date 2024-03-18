def average_value(input_string):
    numbers = [int(n) for n in input_string.split() if n.isdigit()]
    return sum(numbers) / len(numbers) if numbers else None

while True:
    line = input()
    if not line.strip():
        break
    print(average_value(line))