def str_sub(s):
    return str(max(int(s[0]) - int(s[1]), 0))


def pix_sub(p1, p2):
    return "".join(map(str_sub, zip(p1, p2)))


def str_add(s):
    return str(min(int(s[0]) + int(s[1]), 1))


def pix_add(p1, p2):
    return "".join(map(str_add, zip(p1, p2)))


p1 = "00111100"
p2 = "00110000"

print(pix_add(p1, p2))
print(pix_sub(p1, p2))
