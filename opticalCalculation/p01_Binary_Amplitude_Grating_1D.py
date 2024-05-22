import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as sp

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
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=A[0, :], mode='lines', name='Прямоугольная амплитудная решетка (1D)'))
    fig.update_layout(title='Прямоугольная амплитудная решетка (1D)', xaxis_title='Позиция', yaxis_title='Амплитуда')
    fig.show()

    # Отображение матрицы
    fig = px.imshow(A, color_continuous_scale='gray', title='Прямоугольная амплитудная решетка (2D)')
    fig.update_layout(coloraxis_colorbar={'title': 'Амплитуда'})
    fig.show()

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(A))  # fftshift используется для упорядочивания членов в их естественном порядке
    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    # Отображение реальной части E
    fig = sp.make_subplots(rows=2, cols=1, subplot_titles=('Реальная часть E', 'Реальная часть (1D)'))
    fig.add_trace(go.Heatmap(z=np.real(E), colorscale='gray'), row=1, col=1)
    fig.add_trace(go.Scatter(y=np.real(E[N // 2, :]), mode='lines'), row=2, col=1)
    fig.update_xaxes(title_text='X', row=1, col=1)
    fig.update_yaxes(title_text='Y', row=1, col=1)
    fig.update_xaxes(title_text='Позиция', row=2, col=1)
    fig.update_yaxes(title_text='Реальная часть', row=2, col=1)
    fig.show()

    # Отображение угловой части E
    fig = sp.make_subplots(rows=2, cols=1, subplot_titles=('Угловая часть E', 'Угловая часть (1D)'))
    fig.add_trace(go.Heatmap(z=np.angle(E), colorscale='gray'), row=1, col=1)
    fig.add_trace(go.Scatter(y=np.angle(E[N // 2, :]), mode='lines'), row=2, col=1)
    fig.update_xaxes(title_text='X', row=1, col=1)
    fig.update_yaxes(title_text='Y', row=1, col=1)
    fig.update_xaxes(title_text='Позиция', row=2, col=1)
    fig.update_yaxes(title_text='Угол', row=2, col=1)
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


create_rectangular_amplitude_grating()