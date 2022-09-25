import asyncio


@asyncio.coroutine
def empacotar_bala():
    print('Enpacotando balas')
    yield from asyncio.sleep(0.1)



@asyncio.coroutine
def atender_balcao():
    print('Veificando se há clientes')

    yield from asyncio.sleep(0.1)




loop = asyncio.get_event_loop()
tasks = [loop.create_task(empacotar_bala()),
        loop.create_task(atender_balcao())]

wait_tasks = asyncio.wait(tasks)

loop.run_until_complete(wait_tasks)
loop.close()



#SAIDA     enpacotando balas
#          Verificando se há Clientes