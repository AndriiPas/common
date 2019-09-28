def alphabet() -> dict:

    alph = {}
    for i in range(1, 27):
        alph[chr(i+96)] = i
    return alph

print(alphabet())



