5.1.1

a=[1,2,3,4,5,66667,098]
print(a)

5.1.2

def search_element(array, target):
    try:
        return array.index(target)
    except ValueError:
        return -1

def main():
    array = []
    n = int(input("Enter the number of elements: "))

    for i in range(n):
        array.append(input(f"Enter element {i + 1}: "))

    target = input("Enter the element to search for: ")
    position = search_element(array, target)

    if position != -1:
        print(f"The element '{target}' is found at position {position + 1}.")
    else:
        print(f"The element '{target}' is not found.")

if __name__ == "__main__":
    main()



5.1.3

def find_largest_smallest(numbers):
   
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

def main():
    
    numbers = []

   
    n = int(input("Enter the number of elements: "))

    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    largest, smallest = find_largest_smallest(numbers)

    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")

if __name__ == "__main__":
    main()

5.1.4



def display_list(elements):
    print("The elements in the list are:", elements)

def insert_at_position(elements, number, position):
    """Function to insert a number at a specified position in the list"""
    elements.insert(position, number)
    return elements

def delete_from_position(elements, position):

    if 0 <= position < len(elements):
        elements.pop(position)
    else:
        print("Invalid position")
    return elements

def main():
    elements = []

    n = int(input("Enter the number of elements: "))

    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        elements.append(number)

  
    display_list(elements)

    insert_number = float(input("Enter the number to insert: "))
    insert_position = int(input("Enter the position to insert the number (0-indexed): "))
    elements = insert_at_position(elements, insert_number, insert_position)

    print("After insertion:")
    display_list(elements)

    # Delete number from specified position
    delete_position = int(input("Enter the position to delete the number from (0-indexed): "))
    elements = delete_from_position(elements, delete_position)

    print("After deletion:")
    display_list(elements)

if __name__ == "__main__":
    main()


5.1.5

import math

def calculate_mean(numbers):

    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    
    return math.sqrt(variance)

def main()
    numbers = []

   
    n = int(input("Enter the number of elements: "))

    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)


    mean = calculate_mean(numbers)
    print(f"The mean is: {mean}")


    variance = calculate_variance(numbers, mean)
    print(f"The variance is: {variance}")

    
    standard_deviation = calculate_standard_deviation(variance)
    print(f"The standard deviation is: {standard_deviation}")

if __name__ == "__main__":
    main()

5.2.1

def remove_duplicates(array):
    unique_elements = []
    seen = set()
    for element in array:
        if element not in seen:
            unique_elements.append(element)
            seen.add(element)
    return unique_elements

def main():
    size = int(input("Enter the array size: "))

    array = []
    print(f"Input {size} elements in an array: ")
    for i in range(size):
        element = int(input())
        array.append(element)
    unique_elements = remove_duplicates(array)
    print("The unique elements found in the array are: ")
    for element in unique_elements:
        print(element, end=" ")
    print()

if __name__ == "__main__":
    main()

5.2.2

def main():
    n = int(input("Enter how many values you want to read: "))
    array = []
    for i in range(n):
        value = int(input(f"Enter the value of a[{i}]: "))
        array.append(value)
    array.sort()
    print("Array sorted in ascending order =", ' '.join(map(str, array)))

if __name__ == "__main__":
    main()

5.2.3

def main():

    n = int(input("Enter how many values you want to read: "))

    array = []
    for i in range(n):
        value = int(input(f"Enter the value of a[{i}]: "))
        array.append(value)
    total_sum = sum(array)

    print(f"The sum of array elements = {total_sum}")

if __name__ == "__main__":
    main()

5.2.4

def check_arrays_equal(array1, array2):
    if len(array1) != len(array2):
        return False
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True

def main():
    
    # Input the number of values
    n = int(input("Enter how many values you want to read: "))


    array1 = []
    array2 = []

    print("Enter elements for array1:")
    for i in range(n):
        value = int(input(f"Enter the value of a[{i}]: "))
        array1.append(value)
    print("Enter elements for array2:")
    for i in range(n):
        value = int(input(f"Enter the value of b[{i}]: "))
        array2.append(value)
    if check_arrays_equal(array1, array2):
        print("Both arrays are equal")
    else:
        print("Both arrays are not equal")

if __name__ == "__main__":
    main()

5.2.5

def find_repetitive_element(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)

def main():
    arrays = [[1, 3, 2, 3, 4], [1, 5, 1, 2, 3, 4]]

    for array in arrays:
        print("Array:", array)
        result = find_repetitive_element(array)
        print("Repetitive element:", result)
        print()

if __name__ == "__main__":
    main()


5.3.1

import math

def is_perfect_square(num):

    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def largest_not_perfect_square(array):
    max_not_square = -1
    for num in array:
        if not is_perfect_square(num):
            max_not_square = max(max_not_square, num)
    return max_not_square

def main():
  
    arrays = [[16, 20, 25, 2, 3, 10], [36, 64, 10, 16, 29, 25]]

    for array in arrays:
        print("Array:", array)
        result = largest_not_perfect_square(array)
        print("Output:", result)
        print()

if __name__ == "__main__":
    main()

5.3.2

def count_subsets(array):
  
    n = len(array)
    total_subsets = 2 ** n
    return total_subsets

def main():
   
    size = int(input("Enter array size: "))

    if size < 0:
        print("Invalid input")
        return

    if size == 0:
        print("Number of subsets: 1")
        return
    print(f"Enter {size} elements separated by space:")
    array = list(map(int, input().split()))
    subsets_count = count_subsets(array)
    print("Number of subsets:", subsets_count)

if __name__ == "__main__":
    main()

5.3.3

def count_subsets(n):
    return 2 ** n

def main():
  
    # Input array size
    size = int(input("Enter array size: "))

    if size <= 0:
        print("Invalid input")
        return
    subsets_count = count_subsets(size)
    print(subsets_count)

if __name__ == "__main__":
    main()


5.3.4


def max_min_product(arr1, arr2):
    """Function to calculate the product of max element of first array and min element of second array"""
    max_element_arr1 = max(arr1)
    min_element_arr2 = min(arr2)
    return max_element_arr1 * min_element_arr2

def main():
  
    size1, size2 = map(int, input("Enter size of first and second arrays: ").split())


    print("Enter first array elements:")
    arr1 = list(map(int, input().split()))
    print("Enter second array elements:")
    arr2 = list(map(int, input().split()))
    product = max_min_product(arr1, arr2)

    max_element_arr1 = max(arr1)
    # Find min element in second array
    min_element_arr2 = min(arr2)

    # Print results
    print("max element in first array is", max_element_arr1, "and min element in second array is", min_element_arr2)
    print("The product of these two is", product)

if __name__ == "__main__":
    main()

5.3.5

def move_zeros_to_end(array):
    """Function to move all the 0's to the end of the array"""
    n = len(array)
    non_zero_index = 0
    
    # Move non-zero elements to the beginning
    for current_index in range(n):
        if array[current_index] != 0:
            array[non_zero_index] = array[current_index]
            non_zero_index += 1
    
    # Fill remaining positions with zeros
    for i in range(non_zero_index, n):
        array[i] = 0

def main():
    """Main function to input array elements and move zeros to the end"""
    # Input array size
    size = int(input("Enter array size: "))

    if size <= 0:
        print("Invalid input")
        return

    # Input elements
    print("Enter array elements separated by space:")
    array = list(map(int, input().split()))

    # Move zeros to the end
    move_zeros_to_end(array)

    # Print modified array
    print("Modified array:", ' '.join(map(str, array)))

if __name__ == "__main__":
    main()
