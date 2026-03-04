import matplotlib.pyplot as plt

def plot_results(process_counts, averages, title):
    plt.figure()
    plt.plot(process_counts, averages)
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo promedio")
    plt.title(title)
    plt.show()