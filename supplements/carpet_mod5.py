def print_tile(name, label, nb, eb, sb, wb, nl, el, sl, wl, color):
    print("TILENAME", name)
    print("LABEL", label)
    print("NORTHBIND", nb)
    print("EASTBIND", eb)
    print("SOUTHBIND", sb)
    print("WESTBIND", wb)
    print("NORTHLABEL", nl)
    print("EASTLABEL", el)
    print("SOUTHLABEL", sl)
    print("WESTLABEL", wl)
    print("TILECOLOR", color)
    print("CREATE", "\n")

def print_seeds():
    print_tile("SEED", "1", 2, 2, 0, 0, "(1,1)", "1", "", "", "red")
    print_tile("BOTTOM", "1", 1, 2, 0, 2, "(1,1)", "1", "", "1", "red")
    print_tile("LEFT", "1", 2, 1, 2, 0, "(1,1)", "1", "(1,1)", "", "red")

def print_mod5_tile(x, y, z):
    name = str(x) + str(y) + str(z)
    left = str(x)
    bot = "(" + str(y) + "," + str(z) + ")"
    w = (x + y + z) % 5
    right = str(w)
    top = "(" + str(x) + "," + str(w) + ")"
    color = "white" if w == 0 else "red"
    label = str(w)
    print_tile(name, label, 1, 1, 1, 1, top, right, bot, left, color)

print_seeds()

for x in range(5):
    for y in range(5):
        for z in range(5):
            print_mod5_tile(x, y, z);