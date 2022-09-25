from asyncio import get_event_loop,coroutine
import asyncio


#@asyncio.coroutine
async def primeiro():
	while True:

		print('Primeiro 1')
		await asyncio.sleep(0.2)

#@asyncio.coroutine
async def segundo():
	while True:
		
		print('Segundo 2')
		await asyncio.sleep(0.2)



async def main():

	task1 = asyncio.create_task(primeiro())
	task2 = asyncio.create_task(segundo())
	await task1
	await task2


asyncio.run(main())



# SAIDA primeiro 1
#       segundo 2