import numpy as np
import matplotlib.pyplot as plt

# Matrix multiplication
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[10, 11], [12, 13], [14, 15]])

result_matrix = np.dot(matrix_a, matrix_b)

print("Matrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)
print("\nResultant Matrix (A · B):\n", result_matrix)
print("\nShape of Resultant Matrix:", result_matrix.shape)

# Statistical calculations
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)

print("\nData:\n", data)
print(f"\nMean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")

# Histogram plot
random_data = np.random.rand(1000)
plt.hist(random_data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Reshaping array
data = np.arange(12)
try:
    reshaped_data = data.reshape(3, 4)
    print("\nOriginal Array:\n", data)
    print("\nReshaped Array (3x4):\n", reshaped_data)
except ValueError as e:
    print("Reshaping not possible:", e)

# Filtering elements > 5
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
filtered_data = data[data > 5]
print("\nOriginal Array:\n", data)
print("\nFiltered Array (elements > 5):\n", filtered_data)

data = np.array([1,2,3,4,5])
modified_data=data+10
print("Original Array:\n",data)
print("\nModified Array (after broadcasting):\n",modified_data)

data=np.array([[1,2,3],[4,5,6]])
np.savetxt("my array.txt",data)

loaded_data=np.loadtxt("my_array.txt")
print("Original Array:\n",data)
print("\nLoaded Array:",loaded_data)
print("\nArrays are equal:",np.array_equal(data,loaded_data))