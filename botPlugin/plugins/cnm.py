from nonebot import *
import nmsl


@on_command('cnmstr')
async def cnm(session: CommandSession):
    mode = session.get('mode', prompt='请输入模式：\n火力全开（慎重选择）\n口吐莲花（过滤大部分脏字）')

    await session.send(await get_cnm(mode))

@on_command('hlqk')
async def cnm(session: CommandSession):
    mode = '火力全开'

    await session.send(await get_cnm(mode))

@on_command('ktlh')
async def cnm(session: CommandSession):
    mode = '口吐莲花'

    await session.send(await get_cnm(mode))


@on_command('randnmsl')
async def randnmsl(session: CommandSession):
    mode = ''
    await session.send(await get_cnm(mode))

async def get_cnm(mode: str) -> str:

    cnm_result = nmsl.nmsl(mode)

    return f'{cnm_result.get_string()}'

@on_natural_language(keywords={'嘴臭模式'}, only_to_me=False)
async def _cnm(session : NLPSession):
    return IntentCommand(90.0, 'cnmstr')

@on_natural_language(keywords={'嘴臭一个', '再来一个', '再来'}, only_to_me=False)
async def _rannmsl(session : NLPSession):
    return IntentCommand(90.0, 'randnmsl')

@on_natural_language(keywords={'火力全开'}, only_to_me=False)
async def _cnm(session : NLPSession):
    return IntentCommand(90.0, 'hlqk')

@on_natural_language(keywords={'口吐莲花'}, only_to_me=False)
async def _cnm(session : NLPSession):
    return IntentCommand(90.0, 'ktlh')