init_atoms = int(input())
final_atoms = int(input())
n = 0
while init_atoms >= final_atoms:
    init_atoms = init_atoms // 2
    n += 1
days = n * 12
print(days)
