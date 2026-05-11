import numpy as np

# 1. Створіть одновимірний масив з 200 випадкових чисел від -100 до 100.
arr = np.random.randint(-100, 101, size=200)
print("Масив:\n", arr)

# 2. Використовуючи маску, відфільтруйте всі додатні числа в масиві.
mask = arr > 0
print("\nУсі додатні числа в масиві:\n", arr[mask])

# 3. Замініть всі від’ємні значення на нулі.
arr_with0 = arr.copy()
arr_with0[arr_with0 < 0] = 0
print("\nОновлений масив:\n", arr_with0)

# 4. Обчисліть середнє значення отриманого масиву.
mean_value = np.mean(arr_with0)
print("\nCереднє значення:\n", mean_value)