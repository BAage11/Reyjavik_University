# Implement the class Sales which has a private member variable which contains sales data. Implement the member functions needed for the following program to run:
# In addition to the member functions in the Sales class, you need to implement the function read_data_from_file () which reads data from the file sales.txt into a list and returns that list.
# No text file is given but you should create one yourself and test your code using it.

class Sales():
  def __init__(self, sales_data):
    self.__sales_data = sales_data

  def get_average(self):
    total_sum = 0
    for i in self.__sales_data:
      total_sum += i
    return total_sum / (len(self.__sales_data))

  def add_sale(self, add_sale):
    return self.__sales_data.append(add_sale)


def read_data_from_file(file):
    word_list = []
    file = open(file, "r")
    for word in file:
      word_list.append(float(word.strip()))
    file.close()
    return word_list

def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()