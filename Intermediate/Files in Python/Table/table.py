# Multiplication table from 2 to 20
for i in range(2,21):
    with open(f"MultiplicationTableOf {i}",'w') as f:
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
    break
