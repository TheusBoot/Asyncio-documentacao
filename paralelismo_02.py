import asyncio

True_or_False = None

async def tarefa_1(number:int):
    global True_or_False
    while True:
        print(number)
        await asyncio.sleep(0.8)
        number += 1
        if number == 100:
            True_or_False = False
            break


async def tarefa_2():
    global True_or_False
    while True:
        print('OLÁ MUNDO CRUELLLLLLLLL')
        print('=' * 20)
        await asyncio.sleep(0.2)
        print('HOJE É DIA DE MALDADE.')
        print('=' * 20)
        if True_or_False == False:

            print('FIM DO CÓDIGO AMIGOS')
            
            break




async def main():
    task1 = asyncio.create_task(tarefa_1(1))
    task2 = asyncio.create_task(tarefa_2())

    await task1
    await task2


asyncio.run(main())