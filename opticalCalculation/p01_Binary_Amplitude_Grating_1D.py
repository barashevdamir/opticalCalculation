import numpy as np
import matplotlib.pyplot as plt

def create_rectangular_amplitude_grating(N=500, P=100, FF=0.5):
    """
    Рассчитывает 1D прямоугольную амплитудную решетку и отображает выход решетки в дальней зоне.

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
    for q in range(N):
        if q % P < P * FF:
            A[q] = 1
    A = np.tile(A, (N, 1))  # Создание 2D решетки путем дублирования строки

    # Альтернативный код для конструирования решетки
    # O = np.ones((N, int(FF * P)))
    # Z = np.zeros((N, P - int(FF * P)))
    # unit = np.hstack((O, Z))
    # A = np.tile(unit, (1, N // P))

    # Построение графика решетки
    plt.figure()
    plt.plot(A[0, :])
    plt.show()

    # Отображение матрицы
    plt.figure()
    plt.imshow(A, cmap='gray')
    plt.show()

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(A))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    # Отображение реальной части E
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.imshow(np.real(E), cmap='gray')
    plt.subplot(2, 1, 2)
    plt.plot(np.real(E[N // 2, :]))
    plt.show()

    # Отображение угловой части E
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.imshow(np.angle(E), cmap='gray')
    plt.subplot(2, 1, 2)
    plt.plot(np.angle(E[N // 2, :]))
    plt.show()

    # Отображение интенсивности
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.imshow(IN, cmap='gray')
    plt.subplot(2, 1, 2)
    plt.plot(IN[N // 2, :])
    plt.show()

create_rectangular_amplitude_grating()