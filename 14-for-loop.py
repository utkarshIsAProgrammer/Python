for i in range(1, 10):
    if i == 3:
        print("Skipping 3")
        continue
    elif i == 5:
        print("Passing at 5, do nothing")
        pass
    elif i == 7:
        print("Breaking at 7")
        break
    print(f"Current number: {i}")
else:
    print("Loop completed without break.")
