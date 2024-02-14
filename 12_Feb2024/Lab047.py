# Continue
for num in range(1, 10):
    # if num > 1:
    #   print(num)

    if num % 2 == 0:
        print(f"Found even number {num}")
        # else:
        #   print(f"Found Odd number  {num}")
        continue
    print(f"Odd number{num}")
