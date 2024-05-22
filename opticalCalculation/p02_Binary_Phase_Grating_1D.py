import numpy as np
import matplotlib.pyplot as plt

def create_rectangular_phase_grating(N=500, P=50, FF=0.75):
    """
    Рассчитывает 1D прямоугольную фазовую решетку и отображает выход решетки в дальней зоне.

    Parameters:
    N (int): Размер матрицы
    P (int): Период решетки
    FF (float): Скважность (Fill factor)

    Returns:
    None
    """
    # Определение параметров решетки
    A = np.zeros(N)  # Определяем строковую матрицу, присваивая 0 всем пикселям

    # Конструирование решетки
    O = np.ones((N, int(round(FF * P))))
    Z = np.zeros((N, P - int(round(FF * P))))
    unit = np.hstack((O, Z))
    A = np.tile(unit, (1, N // P))

    # Построение графика
    plt.figure()
    plt.plot(A[0, :])
    plt.show()

    # Создание фазовой решетки
    B = np.exp(1j * A.T)

    # Построение угловой части B
    plt.figure()
    plt.plot(np.angle(B[0, :]))
    plt.show()

    # Отображение матрицы
    plt.figure()
    plt.imshow(np.angle(B), cmap='gray')
    plt.show()

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft(B))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / N) ** 2  # Вычисление интенсивности

    # Отображение изображения с высоким контрастом
    plt.figure()
    plt.imshow(A, cmap='gray')
    plt.show()

    # Отображение интенсивности
    plt.figure()
    plt.imshow(IN, cmap='gray')
    plt.show()

    # Построение интенсивности по центру
    plt.figure()
    plt.plot(IN[:, N // 2])
    plt.show()
