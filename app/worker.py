import asyncio
from collections import namedtuple
from datetime import datetime

Task = namedtuple('Task', ['creation_time', 'num', 'timeout'])


class Worker:
    run = False
    tasks = []
    results = []

    async def add_task(self, num: int, timeout: int):
        new_task = Task(datetime.now(), num, timeout)
        self.tasks.append(new_task)

    async def get_tasks(self):
        return [{'number': i, 'creation_time': str(task.creation_time), 'num': task.num, 'timeout': task.timeout
                 } for i, task in enumerate(self.tasks)]

    async def start_worker(self):
        while True:
            if self.tasks:
                task = self.tasks[0]
                await asyncio.sleep(task.timeout)
                self.results.append(task.num)
                self.tasks = self.tasks[1:]
            await asyncio.sleep(1)
