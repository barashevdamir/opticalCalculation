import numpy as np
import matplotlib.pyplot as plt

def create_sin_amplitude_grating(N=500, P=500):
    """
    Рассчитывает 1D синусоидальную амплитудную решетку и отображает выход решетки в дальней зоне.

    Parameters:
    N (int): Размер матрицы
    P (int): Период решетки

    Returns:
    None
    """
    # Определение параметров решетки
    A = np.ones(N)  # Определяем матрицу, присваивая 1 всем пикселям

    # Конструирование решетки
    for q in range(N):
        A[q] = (1 + np.sin((q % P) * (2 * np.pi) / P)) / 2
    A = np.tile(A, (N, 1))  # Создание 2D решетки путем дублирования строки

    # Наблюдение выхода решетки в дальней зоне
    plt.figure()
    plt.plot(A[N // 2, :])
    plt.show()

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(A))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    # Отображение интенсивности
    plt.figure()
    plt.imshow(IN, cmap='gray')
    plt.show()

    # Построение интенсивности по центру
    plt.figure()
    plt.plot(np.arange(1, 501), IN[251, :])
    plt.show()
