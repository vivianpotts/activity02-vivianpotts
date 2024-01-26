"""Demonstrate strange outcomes when comparing variables."""

# is 1.0 equal to 1.1?
if 1.0 == 1.1:
    print("1.0 is the same as 1.1")
else:
    print("1.0 is not the same as 1.1")


# is 1.0 equal to 1?
if 1.0 == 1:
    print("1.0 is the same as 1.0")
else:
    print("1.0 is not the same as 1.0")


# is .33333 + .33333 + .33333 == 1?
if .33333 + .33333 + .33333 == 1:
    print(".33333 + .33333 + .33333 is equal to 1")
else:
    print(".33333 + .33333 + .33333 is not equal to 1")


# is .33333333333 + .33333333333 + .3333333333 == 1?
if .33333333333 + .33333333333 + .3333333333 == 1:
    print(".33333333333 + .33333333333 + .3333333333 is equal to 1")
else:
    print(".33333333333 + .33333333333 + .3333333333 is not equal to 1")


# what is the value of 1/3 as a decimal number?
print(f"The value of 1/3 is {(1/3)}")


# is 0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 == 1?
if 0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 == 1:
    print("0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is equal to 1")
else:
    print("0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is not equal to 1")


# is 1/3 + 1/3 + 1/3 == 1?
if (1/3) + (1/3) + (1/3) == 1:
    print("1/3 + 1/3 + 1/3 is equal 1")
else:
    print("1/3 + 1/3 + 1/3 is not equal 1")
