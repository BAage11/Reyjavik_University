import sys
from dll import DLL

from random import Random

rand = Random()
rand.seed(742983798423)

def test_print(dll):
    print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))

def test_insert(dll):
    num = rand.randint(10, 29)
    print("insert " + str(num))
    dll.insert(num)
    test_print(dll)

def test_remove(dll):
    print("remove")
    dll.remove()
    test_print(dll)

def test_move_to_next(dll):
    print("move_to_next")
    dll.move_to_next()
    test_print(dll)

def test_move_to_prev(dll):
    print("move_to_prev")
    dll.move_to_prev()
    test_print(dll)

def test_move_to_pos(dll):
    pos = rand.randint(-2, len(dll) + 5)
    print("move_to_pos " + str(pos))
    dll.move_to_pos(pos)
    test_print(dll)

def test_remove_all(dll):
    num = rand.randint(8, 31)
    print("remove_all " + str(num))
    dll.remove_all(num)
    test_print(dll)

def test_sort(dll):
    print("sort")
    dll.sort()
    test_print(dll)

def test_reverse(dll):
    print("reverse")
    dll.reverse()
    test_print(dll)

def test_dll(complex = False):
    dll = DLL()
    test_print(dll)
    for _ in range(100):
        if complex:
            choice = rand.randint(1, 8)
        else:
            choice = rand.randint(1, 5)
        if choice == 1:
            for _ in range(rand.randint(1, 10)):
                test_insert(dll)
        elif choice == 2:
            for _ in range(rand.randint(1, 11)):
                test_remove(dll)
        elif choice == 3:
            for _ in range(rand.randint(1, max(1, len(dll) // 3))):
                test_move_to_next(dll)
        elif choice == 4:
            for _ in range(rand.randint(1, max(1, len(dll) // 3))):
                test_move_to_prev(dll)
        elif choice == 5:
            test_move_to_pos(dll)
        elif choice == 6:
            test_remove_all(dll)
        elif choice == 7:
            test_sort(dll)
        elif choice == 8:
            test_reverse(dll)

def main():

    orig_stdout = sys.stdout
    fout = open('out.txt', 'w+')
    sys.stdout = fout


    print("\n\nTESTING THE BASIC STUFF\n")

    for _ in range(30):
        test_dll()

    print("\n\nTESTING MORE COMPLEX STUFF\n")

    for _ in range(30):
        test_dll(True)

    sys.stdout = orig_stdout
    fout.close()


if __name__ == "__main__":
    main()


