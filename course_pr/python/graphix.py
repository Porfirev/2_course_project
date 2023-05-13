import matplotlib.pyplot as plt


def draw_points(points):
    vertex_factor = [[] for i in range(4)]
    for point in points:
        vertex_factor[point.num - 1].append(point.A)
    for factor in vertex_factor:
        X = list(map(lambda x: x.x, factor))
        Y = list(map(lambda x: x.y, factor))
        plt.scatter(X, Y)
    plt.show()


def draw_geodesic(geodesics):
    X = []
    Y = []
    for key, value in geodesics.items():
        X.append(key)
        Y.append(value)
    plt.plot(X, Y)
    plt.show()


def draw_geodesic_counts_func(counts, title, y_label, func=lambda x: x, draw=True, save_name=None):
    X = []
    Y = []
    for key, value in counts.items():
        X.append(key)
        Y.append(func(value))
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.75, 0.75])
    ax.scatter(X, Y)
    ax.set_title(title)
    ax.set_xlabel("radius")
    ax.set_ylabel(y_label)
    if draw:
        plt.show()
    else:
        fig.savefig(f"{save_name}.png")
