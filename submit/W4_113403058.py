import numpy as np

# 1. 建立陣列
numbers_a = np.array([1, 2, 3, 4, 5])
numbers_b = np.arange(10, 15)  # 從 10 到 14

print("numbers_a:", numbers_a)
print("numbers_b:", numbers_b)

# 2. 基本運算（Element-wise operations）
sum_array = numbers_a + numbers_b
diff_array = numbers_b - numbers_a
scalar_product = numbers_a * 2
elementwise_product = numbers_a * numbers_b

print("\n--- 基本運算 ---")
print("加法:", sum_array)
print("減法:", diff_array)
print("純量乘法:", scalar_product)
print("元素乘法:", elementwise_product)

# 3. 二維陣列與索引
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("\n--- 二維陣列 ---")
print("matrix:\n", matrix)
print("第一列:", matrix[0])
print("第二列第三個元素:", matrix[1, 2])

# 4. 統計操作（含 axis）
print("\n--- 統計操作 ---")
print("總和:", np.sum(matrix))
print("平均值:", np.mean(matrix))
print("最大值:", np.max(matrix))
print("最小值:", np.min(matrix))

# axis 操作（重點）
print("各欄總和 (axis=0):", np.sum(matrix, axis=0))
print("各列平均 (axis=1):", np.mean(matrix, axis=1))

# 5. 隨機陣列
random_matrix = np.random.rand(3, 3)

print("\n--- 隨機陣列 ---")
print("3x3 隨機矩陣:\n", random_matrix)
