from passwordcheck import strength_check

tests = ["password","pass94_pass","Pa$$word","Pa$word9b"]
for password in tests:
    print(password + ": " + str(strength_check(password)))
