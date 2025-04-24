from dataclasses import dataclass
from timeit import default_timer as time
import asyncio

@dataclass
class Producer:
    seconds_between_items: float
    num_items: int
    value_yielded: str

    async def start_generating(self):
        for i in range(1, self.num_items + 1):
            await asyncio.sleep(self.seconds_between_items)
            yield f"{self.value_yielded}-{i}"

class MultiProducer:
    def __init__(self, seconds_between_producers: float, producers: list[Producer]):
        self.seconds_between_producers = seconds_between_producers
        self.producers = producers

    async def start_generating(self):
        queue = asyncio.Queue()

        async def produce(producer: Producer, delay: float):
            await asyncio.sleep(delay)
            async for item in producer.start_generating():
                await queue.put(item)

        tasks = []
        for i, producer in enumerate(self.producers):
            delay = i * self.seconds_between_producers
            tasks.append(asyncio.create_task(produce(producer, delay)))

        async def wait_for_completion():
            await asyncio.gather(*tasks)
            await queue.put(None)

        waiter = asyncio.create_task(wait_for_completion())

        while True:
            item = await queue.get()
            if item is None:
                break
            yield item

        await waiter

# =========================
# Funciones de prueba
# =========================

async def single_producer_tester(tr: Producer):
    times = []
    i = 0

    async for item in tr.start_generating():
        times.append(time())
        i += 1
        assert item == f"{tr.value_yielded}-{i}"

    assert len(times) == tr.num_items

    assert all(
        abs((current_time - previous_time) - tr.seconds_between_items) < 0.05
        for previous_time, current_time in zip(times[:-1], times[1:])
    )

async def multi_producer_tester(producers: list[Producer], delay_between_task_starts: float):
    timers = {producer.value_yielded: [] for producer in producers}

    async for item in MultiProducer(delay_between_task_starts, producers).start_generating():
        current_time = time()
        producer_name, _ = item.split("-")
        timers[producer_name].append(current_time)

    for producer in producers:
        times = timers[producer.value_yielded]
        print(f"\n🔍 Checking producer: {producer.value_yielded}")
        print("Tiempos generados:")
        for previous_time, current_time in zip(times[:-1], times[1:]):
            delta = current_time - previous_time
            print(f"  Δt = {delta:.3f} (esperado: {producer.seconds_between_items})")

        assert len(times) == producer.num_items
        assert all(
            abs((current_time - previous_time) - producer.seconds_between_items) < 0.05
            for previous_time, current_time in zip(times[:-1], times[1:])
        )

    starting_times = [timers[producer.value_yielded][0] for producer in producers]
    print("\n⏱ Verificando retrasos entre productores:")
    for i in range(1, len(starting_times)):
        delay = starting_times[i] - starting_times[i - 1]
        print(f"  Delay entre {producers[i-1].value_yielded} y {producers[i].value_yielded}: {delay:.3f} (esperado: {delay_between_task_starts})")

    assert all(
        abs((starting_times[i] - starting_times[i - 1]) - delay_between_task_starts) < 0.25
        for i in range(1, len(starting_times))
    )

def test_single_task():
    tr = Producer(1, 5, "test")
    asyncio.run(single_producer_tester(tr))

def test_multi_task():
    producers = [
        Producer(0.1, 5, "test1"),
        Producer(0.3, 5, "test2"),
        Producer(0.5, 5, "test3"),
    ]
    asyncio.run(multi_producer_tester(producers, 0.1))

# =========================
# Versión con prints para debug
# =========================

async def debug_single_producer():
    tr = Producer(1, 5, "A")
    async for item in tr.start_generating():
        print(f"[{time():.2f}] Received from single: {item}")

async def debug_multi_producer():
    producers = [
        Producer(0.5, 4, "A"),
        Producer(1, 6, "B"),
        Producer(0.3, 12, "C"),
    ]
    mp = MultiProducer(0.5, producers)
    async for item in mp.start_generating():
        print(f"[{time():.2f}] Received from multi: {item}")

# =========================
# Descomenta para probar
# =========================

test_single_task()
test_multi_task()

asyncio.run(debug_single_producer())
asyncio.run(debug_multi_producer())