# If a chessboard were to have wheat placed upon each square such that one grain were placed on the first square, two on the second, four on the third, and so on (doubling the number of grains on each subsequent square), how many grains of wheat would be on the chessboard at the finish?
# Write a Python program using a for loop that calculates and prints out this number of grains.

grains = 1

for i in range(1, 64):
# Endar í 64, þar sem búið er að telja fyrsta reitin (grains=1).
# Þar af leiðandi á kóðinn að stoppa í tölu 64 og telja því 63 reiti samtals plús grains=1
    grains += 2**i

print("Number of grains:", grains)
    