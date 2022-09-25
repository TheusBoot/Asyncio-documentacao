#import asyncio
from asyncio import get_event_loop, coroutine


@coroutine # Funções coroutine são uma promessa, são paralelas...
def print_async(msg:str) -> None:
    print(f'ASYNC:{msg}')

loop = get_event_loop()
loop.run_until_complete(print_async('OI'))
loop.close()

#SAIDA   OI

#---------------------------------------------------------------


async def print_async(msg:str) -> None:
    print(f'ASYNC:{msg}')

loop = get_event_loop()
loop.run_until_complete(print_async('OI'))
loop.close()

# SAIDA    OI

#------------------------------------------------------------------

@asyncio.coroutine
def print_async(path):
    yield from ping_server('127.0.0.1') 
    #YIELD FROM == aguardar até que essa tarefa seja concluída.

loop = get_event_loop()
loop.run_until_complete(print_async('OI'))
loop.close()

#------------------------------------------------------------------


async def print_async(path):
    await ping_server('127.0.0.1') 
    #await == aguardar até que essa tarefa seja concluída.

    #sintaxe base (async só vai ser usado com await)

loop = get_event_loop()
loop.run_until_complete(print_async('OI'))
loop.close()




