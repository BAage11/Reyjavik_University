
import random
from random import Random

# This function generates a test file
# with random prefix notation statements
def generate_prefix_notation_statement(f, rand, possible_operators, depth_factor):
    
    oper = rand.randint(1, possible_operators)
    if oper == 1:
        f.write("+ ")
    if oper == 2:
        f.write("- ")
    if oper == 3:
        f.write("* ")
    if oper == 4:
        f.write("/ ")
    inception = rand.randint(0, depth_factor)
    if inception == 0:
        f.write(str(rand.randint(0, 9)) + " ")
    else:
        generate_prefix_notation_statement(f, rand, possible_operators, depth_factor - 1)
    inception = rand.randint(0, depth_factor)
    if inception == 0:
        f.write(str(rand.randint(0, 9)) + " ")
    else:
        generate_prefix_notation_statement(f, rand, possible_operators, depth_factor - 1)
    

f = open("prefix_test.txt", "w+")
rand = Random()
generate_prefix_notation_statement(f, rand, 1, 0)

for _ in range(2):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 1, 0)

for _ in range(12):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 2, 0)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 2, 1)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 3, 1)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 3, 2)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 4, 1)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 4, 2)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 4, 3)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 4, 4)

for _ in range(5):
    f.write("\n")
    generate_prefix_notation_statement(f, rand, 4, 5)

f.close()