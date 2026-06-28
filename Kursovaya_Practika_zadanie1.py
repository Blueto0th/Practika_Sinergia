# Кейс-задача № 1
# Дан одномерный массив А размерности N.
# Найти сумму отрицательных элементов,
# расположенных между максимальным и минимальным элементами.

def find_sum_between_max_min(arr):
    """
    Функция находит сумму отрицательных элементов,
    расположенных между максимальным и минимальным элементами массива.
    """
    # Если в массиве меньше 3 элементов, между ними ничего нет
    if len(arr) < 3:
        return 0

    # Находим индексы максимального и минимального элементов
    max_index = 0
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
        if arr[i] < arr[min_index]:
            min_index = i

    # Определяем левую и правую границы (между max и min)
    left = min(max_index, min_index)
    right = max(max_index, min_index)

    # Если между ними нет элементов
    if right - left <= 1:
        return 0

    # Суммируем отрицательные элементы между ними
    total = 0
    for i in range(left + 1, right):
        if arr[i] < 0:
            total += arr[i]

    return total


# ---------- Основная программа ----------
if __name__ == "__main__":
    # Ввод размера массива
    N = int(input("Введите размер массива N: "))

    # Ввод элементов массива
    arr = []
    for i in range(N):
        arr.append(int(input(f"Введите A[{i}]: ")))

    # Вывод массива
    print("\nМассив:", arr)

    # Вычисление результата
    result = find_sum_between_max_min(arr)
    print("Сумма отрицательных элементов между max и min:", result)
