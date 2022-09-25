
from asyncio import get_event_loop,coroutine
import asyncio




@asyncio.coroutine
def primeiro():
	while True:

		print('Primeiro 1')
		yield from asyncio.sleep(0.9)

@asyncio.coroutine
def segundo():
	while True:
		
		print('Segundo 2')
		yield from asyncio.sleep(0.1)




loop = asyncio.get_event_loop()
tasks = [loop.create_task(primeiro()),
		loop.create_task(segundo())]
wait_tasks = asyncio.wait(tasks)

loop.run_until_complete(wait_tasks)
loop.close()
