#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    all_data = dir(hidden_4)

    for n in all_data:
        if n[0] != "_":
            print("{}".format(n))
