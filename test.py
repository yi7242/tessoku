
def pred(plants, query):
    for t, x, y in query:
        if t == 0:
            plants = np.where(plants <= x, plants + y, plants)
        else:
            plants = np.where(plants >= x, plants - y, plants)

    return plants