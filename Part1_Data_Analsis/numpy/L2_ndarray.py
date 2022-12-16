import numpy as np

# ndarray 的基本形式
t_list = [1, 2, 3, 4, 5]
t_array = np.array(t_list)
print(t_array)
print(type(t_array))
print(t_array.dtype)
# t_array.fill(1)
print(t_array[1:4])

# ndarray 多维数组
t_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(t_array.size)
print(t_array.shape)
print(t_array.ndim)
print(t_array[1, 1])
print(t_array[1])
print(t_array[:, 1])

# ndarray.arange() 等差数组生成函数
t_array = np.arange(0, 100, 10)
print(t_array)

mask = np.array([0, 0, 0, 1, 1, 1, 0, 0, 1, 1], dtype=bool)
print(t_array[mask])
print(t_array)
random_array = np.random.rand(10)
mask = random_array > 0.5
print(mask)
print(t_array[mask])
print(np.where(random_array > 0.5))
print(t_array[np.where(random_array > 0.5)])

# dnarray 的数据类型
t_array = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(t_array.dtype)
print(t_array.nbytes)
