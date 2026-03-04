import simpy
import random
import statistics

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

class Process:
    def __init__(self, env, name, ram, cpu, instr_per_cycle):
        self.env = env
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.instr_per_cycle = instr_per_cycle

        self.mem_required = random.randint(1, 10)
        self.instructions = random.randint(1, 10)

        self.start_time = env.now
        self.times = None
        self.action = env.process(self.run())

    def run(self):
        yield self.ram.get(self.mem_required)

        while self.instructions > 0:
            with self.cpu.request() as req:
                yield req
                yield self.env.timeout(1)

                executed = min(self.instr_per_cycle, self.instructions)
                self.instructions -= executed

            if self.instructions > 0:
                if random.randint(1, 21) == 1:
                    yield self.env.timeout(1)

        yield self.ram.put(self.mem_required)
        finish_time = self.env.now
        self.times.append(finish_time - self.start_time)


def process_generator(env, num_processes, ram, cpu, instr_per_cycle, interval, times):
    for i in range(num_processes):
        p = Process(env, f"P{i}", ram, cpu, instr_per_cycle)
        p.times = times
        yield env.timeout(random.expovariate(1.0 / interval))


def simulate(num_processes, ram_capacity=100, cpu_capacity=1,
             instr_per_cycle=3, interval=10):

    times = []
    env = simpy.Environment()
    ram = simpy.Container(env, init=ram_capacity, capacity=ram_capacity)
    cpu = simpy.Resource(env, capacity=cpu_capacity)

    env.process(process_generator(env, num_processes, ram, cpu,
                                  instr_per_cycle, interval, times))
    env.run()

    avg = statistics.mean(times)
    std = statistics.stdev(times) if len(times) > 1 else 0

    return avg, std