import numpy as np


def prod(items, start=1):
    for item in items:
        start *= item
    return start


def ellipse(box_size, semisizes, position=0.5, n_dim=2, smoothing=1.0):
    shape = (box_size,) * n_dim
    if isinstance(semisizes, (int, float)):
        semisizes = (semisizes,) * n_dim
    position = ((box_size - 1) * position,) * n_dim
    grid = [slice(-x0, dim - x0) for x0, dim in zip(position, shape)]
    position = np.ogrid[grid]
    arr = np.zeros(shape, dtype=float)
    for x_i, semisize in zip(position, semisizes):
        arr += (np.abs(x_i / semisize) ** 2)
    if smoothing:
        k = prod(semisizes) ** (0.5 / n_dim / smoothing)
        return 1.0 - np.clip(arr - 1.0, 0.0, 1.0 / k) * k
    elif isinstance(smoothing, float):
        return (arr <= 1.0).astype(float)
    else:
        return arr <= 1.0


n = 1
print(np.round(ellipse(5 * n, 2 * n, smoothing=0.0), 2))
n = 1
print(np.round(ellipse(5 * n, 2 * n, smoothing=1.0), 2))