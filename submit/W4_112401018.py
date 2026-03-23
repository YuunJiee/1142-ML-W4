import numpy as np

# 1. 建立陣列
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(10, 15)  # 從 10 到 14

print("arr1:", arr1)
print("arr2:", arr2)

# 2. 基本運算
sum_arr = arr1 + arr2
diff_arr = arr2 - arr1
prod_arr = arr1 * 2

print("arr1 + arr2:", sum_arr)
print("arr2 - arr1:", diff_arr)
print("arr1 * 2:", prod_arr)

# 3. 二維陣列與索引
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("matrix:\n", matrix)
print("第一列:", matrix[0])
print("第二行第三列元素:", matrix[1, 2])

# 4. 統計操作
print("matrix sum:", np.sum(matrix))
print("matrix 平均值:", np.mean(matrix))
print("matrix 最大值:", np.max(matrix))
print("matrix 最小值:", np.min(matrix))

# 5. 隨機陣列
rand_arr = np.random.rand(3, 3)
print("3x3 隨機陣列:\n", rand_arr)


