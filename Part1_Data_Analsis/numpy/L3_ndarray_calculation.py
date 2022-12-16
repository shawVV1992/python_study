import numpy as np

# ndarray 的数组内元素的计算
t_array=np.array([[1.1,2.8,3.4],[2.1,2.9,3.2],[1.2,1.3,2.4]])
# 1 sum 求和函数
print(t_array.sum())
print(t_array.sum(axis=0))
print(t_array.sum(axis=1))
print(t_array.sum(axis=-1))

# 2 prod 乘积函数
print(t_array.prod())
print(t_array.prod(axis=0))
print(t_array.prod(axis=-1))

# 3 max/min 最值函数
print(t_array.max())
print(t_array.max(axis=1))
print(t_array.min(axis=-1))

# 4 argmax/argmin 最值索引函数
print(t_array.argmax())
print(t_array.argmax(axis=0))
print(t_array.argmin(axis=-1))

# 5 mean/std/var 平均值、标准差、方差函数
print(t_array.mean(axis=1))
print(t_array.std(axis=1))
print(t_array.var(axis=1))

# 6 clip 范围函数
print(t_array.clip(1.2,2.5))

# 7 round 近似值函数
print(t_array.round(decimals=0))