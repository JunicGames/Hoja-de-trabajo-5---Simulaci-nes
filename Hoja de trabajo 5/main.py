from simulation import simulate
from graphs import plot_results

process_counts = [25, 50, 100, 150, 200]

def run_experiment(interval, ram=100, cpu=1, instr=3):
    averages = []

    print(f"\nIntervalo = {interval}, RAM = {ram}, CPU = {cpu}, Instr = {instr}")

    for n in process_counts:
        avg, std = simulate(n,
                            ram_capacity=ram,
                            cpu_capacity=cpu,
                            instr_per_cycle=instr,
                            interval=interval)

        averages.append(avg)
        print(f"Procesos: {n} | Promedio: {avg:.2f} | Std: {std:.2f}")

    plot_results(process_counts, averages,
                 f"Intervalo {interval} | RAM {ram} | CPU {cpu}")

if __name__ == "__main__":

    run_experiment(interval=10)

    run_experiment(interval=5)
    run_experiment(interval=1)

    run_experiment(interval=10, ram=200)
    run_experiment(interval=10, instr=6)

    run_experiment(interval=10, cpu=2)
