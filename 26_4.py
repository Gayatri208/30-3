for i in range(2,21):
    with open(f"table of multiple_03{i}",'w') as  f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")
            break 