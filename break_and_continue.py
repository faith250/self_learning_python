for n in range(2,9):
    for x in range(2,n):
        if n%x==0:
            print(f"{n}equals{x}*{n//x}")
            break


for num in range(2,9):
    if num%2==0:
        print(f"even num found to be{num}")
        print('before continue')
        continue
    print(f"odd numner found{num}")


for n in range(2,9):
    for x in range(2,n):
        if n%x==0:
            print(f"{n}equals{x}*{n//x}")
            break
    else:
        print(n,'is a prime number')