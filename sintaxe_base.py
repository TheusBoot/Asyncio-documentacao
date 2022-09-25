#import asyncio
from asyncio import get_event_loop, coroutine


@coroutine
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



