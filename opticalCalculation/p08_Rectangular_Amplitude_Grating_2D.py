import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as sp

def create_2d_rectangular_amplitude_grating(N=500, Px=100, Py=100, FFx=0.5, FFy=0.5):
    """
    Рассчитывает 2D прямоугольную амплитудную решетку и отображает выход решетки в дальней зоне.

    Parameters:
    N (int): Размер матрицы
    Px (int): Период решетки по оси x
    Py (int): Период решетки по оси y
    FFx (float): Скважность (Fill factor) по оси x
    FFy (float): Скважность (Fill factor) по оси y

    Returns:
    None
    """
    # Определение параметров решетки
    A1 = np.zeros((N, N))  # Определяем матрицы, присваивая 0 всем пикселям
    A2 = np.zeros((N, N))
    A = np.zeros((N, N))

    # Конструирование решетки
    O1 = np.ones((N, int(FFx * Px)))
    Z1 = np.zeros((N, int(Px - FFy * Px)))
    unit1 = np.hstack((O1, Z1))
    A1 = np.tile(unit1, (1, int(N // Px)))  # Создание 1D решетки

    # Отображение матрицы
    fig = px.imshow(A1, color_continuous_scale='gray', title='')
    fig.update_layout(coloraxis_colorbar={'title': 'Амплитуда'})
    fig.show()

    O2 = np.ones((int(FFy * Py), N))
    Z2 = np.zeros((int(Py - FFy * Py), N))
    unit2 = np.vstack((O2, Z2))
    A2 = np.tile(unit2, (int(N // Py), 1))

    # Отображение матрицы
    fig = px.imshow(A2, color_continuous_scale='gray', title='')
    fig.update_layout(coloraxis_colorbar={'title': 'Амплитуда'})
    fig.show()

    A = A1 * A2

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(A))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    # Построение графика решетки
    fig = px.imshow(A, color_continuous_scale='gray', title='Прямоугольная амплитудная решетка (2D)')
    fig.update_layout(coloraxis_colorbar={'title': 'Амплитуда'})
    fig.show()

    # Отображение интенсивности
    fig = sp.make_subplots(rows=2, cols=1, subplot_titles=('Интенсивность', 'Интенсивность (1D)'))
    fig.add_trace(go.Heatmap(z=IN, colorscale='gray'), row=1, col=1)
    fig.add_trace(go.Scatter(y=IN[N // 2, :], mode='lines'), row=2, col=1)
    fig.update_xaxes(title_text='X', row=1, col=1)
    fig.update_yaxes(title_text='Y', row=1, col=1)
    fig.update_xaxes(title_text='Позиция', row=2, col=1)
    fig.update_yaxes(title_text='Интенсивность', row=2, col=1)
    fig.show()
