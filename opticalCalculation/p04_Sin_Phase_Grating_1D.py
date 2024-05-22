import numpy as np
import plotly.graph_objects as go

def create_sin_phase_grating(N=500, P=500):
    """
    Рассчитывает 1D синусоидальную фазовую решетку и отображает выход решетки в дальней зоне.

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
        A[q] = (1 + np.sin(np.remainder(q, P) * (2 * np.pi) / P)) / 2 - 0.5

    # Построение графика фазовой решетки (1D)
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=A, mode='lines', name='Фазовая решетка (1D)'))
    fig.update_layout(title='Фазовая решетка (1D)', xaxis_title='Позиция', yaxis_title='Амплитуда', legend_title='Легенда')
    fig.show()

    # Создание фазовой решетки
    A = np.exp(1j * np.pi * A)

    # Построение графика угловой части A
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=np.angle(A), mode='lines', name='Угловая часть B'))
    fig.update_layout(title='Угловая часть B', xaxis_title='Позиция', yaxis_title='Угол', legend_title='Легенда')
    fig.show()

    # Создание 2D решетки путем дублирования строки
    B = np.tile(A, (N, 1))

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(B))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    # Отображение интенсивности
    fig = go.Figure()
    fig.add_trace(go.Heatmap(z=IN, colorscale='gray'))
    fig.update_layout(title='Интенсивность', xaxis_title='X', yaxis_title='Y')
    fig.show()

    # Отображение интенсивности по центру (1D)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(0, N), y=IN[N//2, :], mode='lines'))
    fig.update_layout(title='Интенсивность по центру (1D)', xaxis_title='X', yaxis_title='Y')
    fig.show()

create_sin_phase_grating()
