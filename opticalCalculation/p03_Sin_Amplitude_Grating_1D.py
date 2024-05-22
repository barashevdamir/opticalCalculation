import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as sp


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

    # Построение графика решетки
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=A[N // 2, :], mode='lines', name='Прямоугольная амплитудная решетка (1D)'))
    fig.update_layout(title='Прямоугольная амплитудная решетка (1D)', xaxis_title='Позиция', yaxis_title='Амплитуда')
    fig.show()


    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(A))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    # Отображение интенсивности
    fig = go.Figure()
    fig.add_trace(go.Heatmap(z=IN, colorscale='gray'))
    fig.update_layout(title='Интенсивность', xaxis_title='X', yaxis_title='Y')
    fig.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(1, 501), y=IN[:, 251], mode='lines'))
    fig.update_layout(title='Интенсивность по центру (1D)', xaxis_title='X', yaxis_title='Y')
    fig.show()


create_sin_amplitude_grating()