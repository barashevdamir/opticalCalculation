import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as sp

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
    A = np.zeros((1, N))  # Определяем строковую матрицу, присваивая 0 всем пикселям

    # Конструирование решетки
    O = np.ones((N, round(FF * P)))
    Z = np.zeros((N, P - round(FF * P)))
    unit = np.hstack((O, Z))
    A = np.tile(unit, (1, N // P))

    # Построение графика
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=A[0, :], mode='lines', name='Фазовая решетка (1D)'))
    fig.update_layout(title='Фазовая решетка (1D)', xaxis_title='Позиция', yaxis_title='Амплитуда', legend_title='Легенда')
    fig.show()

    # Создание фазовой решетки
    B = np.exp(1j * A.T)

    # Построение угловой части B
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=np.angle(B[0, :]), mode='lines', name='Угловая часть B'))
    fig.update_layout(title='Угловая часть B', xaxis_title='Позиция', yaxis_title='Угол', legend_title='Легенда')
    fig.show()

    # Отображение матрицы
    fig = px.imshow(np.angle(B), color_continuous_scale='gray', title='Угловая часть B (2D)')
    fig.update_layout(coloraxis_colorbar={'title': 'Угол'})
    fig.show()

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft(B))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / N) ** 2  # Вычисление интенсивности

    # Отображение изображения фазовой решетки (2D)
    fig = px.imshow(A, color_continuous_scale='gray', title='Фазовая решетка (2D)')
    fig.update_layout(coloraxis_colorbar={'title': 'Амплитуда'})
    fig.show()

    # Отображение интенсивности
    fig = sp.make_subplots(rows=2, cols=1, subplot_titles=('Интенсивность', 'Интенсивность (1D)'))
    fig.add_trace(go.Heatmap(z=IN, colorscale='gray'), row=1, col=1)
    fig.add_trace(go.Scatter(y=IN[N//2 + 1, :], mode='lines'), row=2, col=1)
    fig.update_xaxes(title_text='X', row=1, col=1)
    fig.update_yaxes(title_text='Y', row=1, col=1)
    fig.update_xaxes(title_text='Позиция', row=2, col=1)
    fig.update_yaxes(title_text='Интенсивность', row=2, col=1, type='log')
    fig.show()


create_rectangular_phase_grating()
