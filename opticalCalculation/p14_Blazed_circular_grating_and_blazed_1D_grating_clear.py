import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def axicon_and_1d_grating(N=500, Pr=20, P=10):
    """
    Создает аксикон и 1D амплитудную решетку и отображает выход решетки в дальней зоне.

    Parameters:
    N (int): Размер матрицы.
    Pr (int): Период аксикона.
    P (int): Период решетки.

    Returns:
    None
    """

    # Конструкция блейзового аксикона и решетки
    x = np.arange(1, N + 1)     # Создание массива значений x от 1 до N включительно
    y = np.arange(1, N + 1)     # Создание массива значений y от 1 до N включительно
    X, Y = np.meshgrid(x, y)    # Создание сетки координат X и Y

    r = np.sqrt((X - N / 2) ** 2 + (Y - N / 2) ** 2)    # Вычисление радиальных координат от центра

    fig1 = go.Figure(data=[go.Surface(z=r)])    # Создание 3D поверхности для радиальных координат
    fig1.update_layout(title='', autosize=False, width=600, height=600)
    fig1.show()

    P1 = np.remainder(r, Pr)    # Конструкция блейзового аксикона
    A1 = (P1 / Pr) * 2 * np.pi  # Масштабирование значений для фазы аксикона

    fig2 = go.Figure(data=[go.Surface(z=A1)])   # Создание 3D поверхности для фазы аксикона
    fig2.update_layout(title='', autosize=False, width=600, height=600)
    fig2.show()

    P2 = np.remainder(X, P)     # Конструкция блейзовой 1D решетки по X
    A2 = (P2 / P) * 2 * np.pi   # Масштабирование значений для фазы решетки по X

    fig3 = go.Figure(data=[go.Surface(z=A2)])   # Создание 3D поверхности для фазы решетки по X
    fig3.update_layout(title='', autosize=False, width=600, height=600)
    fig3.show()

    P3 = np.remainder(Y, P)  # Конструкция блейзовой 1D решетки по Y
    A3 = (P3 / P) * 2 * np.pi   # Масштабирование значений для фазы решетки по Y

    A = np.remainder(A2 + A3, 2 * np.pi)   # Сложение двух фазовых профилей по модулю 2π

    fig4 = go.Figure(data=[go.Surface(z=A)])    # Создание 3D поверхности для суммарной фазы
    fig4.update_layout(title='', autosize=False, width=600, height=600)
    fig4.show()

    fig5 = go.Figure()
    fig5.add_trace(go.Heatmap(z=A, colorscale='gray'))  # Добавление тепловой карты для суммарной фазы
    fig5.update_layout(title='', xaxis_title='X', yaxis_title='Y')
    fig5.show()

    B = np.exp(1j * A)  # Вычисление комплексной экспоненты для суммарной фазы

    fig7 = make_subplots(rows=1, cols=2, subplot_titles=('Real part of Blazed axicon', 'Phase part of Blazed axicon'))

    fig7.add_trace(go.Heatmap(z=np.real(B), colorscale='gray'), row=1, col=1)
    fig7.add_trace(go.Heatmap(z=np.angle(B), colorscale='gray'), row=1, col=2)

    fig7.update_layout(title='Blazed Axicon Components')
    fig7.show()

    # Наблюдение выхода решетки в дальней зоне
    E = np.fft.fftshift(np.fft.fft2(B))  # fftshift используется для упорядочивания членов в их естественном порядке

    fig8 = make_subplots(rows=1, cols=2,
                         subplot_titles=('Real part of reconst Blazed axicon', 'Phase part of reconst Blazed axicon'))

    fig8.add_trace(go.Heatmap(z=np.real(E), colorscale='gray'), row=1, col=1)
    fig8.add_trace(go.Heatmap(z=np.angle(E), colorscale='gray'), row=1, col=2)

    fig8.update_layout(title='Reconstructed Blazed Axicon Components')
    fig8.show()

    fig9 = go.Figure()
    fig9.add_trace(go.Scatter(y=np.max(np.real(E), axis=0)))
    fig9.update_layout(title='Max of real part of reconst', xaxis_title='Index', yaxis_title='Value')
    fig9.show()

    IN = (np.abs(E) / (N * N)) ** 2  # Вычисление интенсивности

    fig10 = go.Figure(data=[go.Heatmap(z=IN, colorscale='gray')])
    fig10.update_layout(title='Intensity', coloraxis_showscale=True)
    fig10.show()

    fig11 = go.Figure()
    fig11.add_trace(go.Scatter(y=np.max(IN, axis=0)))
    fig11.update_layout(title='Max of Intensity', xaxis_title='Index', yaxis_title='Intensity')
    fig11.show()


axicon_and_1d_grating()

