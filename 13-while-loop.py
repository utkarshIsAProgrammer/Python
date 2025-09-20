count = 0
while count < 10:
    count += 1

    if count == 3:
        print("Skipping 3")
        continue

    if count == 7:
        print("Breaking at 7")
        break

    print(f"Number: {count}")

else:
    print("Loop completed naturally without break.")
