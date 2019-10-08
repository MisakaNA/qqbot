from nonebot import *
import nmsl, random

@on_command('zz')
async def undiss(session: CommandSession):
    await session.send('你才是智障！')

@on_command('?', aliases={'¿', '?', '？', '喵喵喵'}, only_to_me=False)
async def wut(session: CommandSession):
    await session.send('¿?')

@on_command('undiss')
async def undiss(session: CommandSession):
    c = random.randint(0, 1)
    if c == 0:
        await session.send('你才是垃圾！')
    else:
        await session.send('你有什么不满的吗？')

@on_command('???')
async def fuckme(session: CommandSession):
    c = random.randint(0, 1)

    if c == 0:
        mode = '口吐莲花'
        await session.send(await get_cnm(mode))
    else:
        await session.send('¿ 我觉得这个词用来形容你比较合适')

@on_command('wrnm')
async def undiss(session: CommandSession):
        mode = ''
        await session.send(await get_cnm(mode))

async def get_cnm(mode: str) -> str:

    cnm_result = nmsl.nmsl(mode)

    return f'{cnm_result.get_string()}'

@on_natural_language(keywords={'沙雕bot', '垃圾bot', '垃圾机器人', '辣鸡bot', '屑机器人', '屑bot',
                               '辣鸡机器人', 'lj', '破玩意', '辣鸡', '垃圾', '不是人', '你好无趣'}, only_to_me=False)
async def _undiss(session : NLPSession):
    return IntentCommand(90.0, 'undiss')

@on_natural_language(keywords={'孙雨萌是', '子月是'}, only_to_me=False)
async def _rannmsl(session : NLPSession):
    return IntentCommand(90.0, '???')

@on_natural_language(keywords={'憨批', '傻屌', '废物', '爬', '尼玛', '看看批', 'kkp', '哈批', 'wdnmd', 'cnm', 'nmsl', '傻逼', '破玩意', '撒币'
                               '萨比', '煞笔', '你妈', '操你', '妈的', '玛德'}, only_to_me=False)
async def _undiss(session : NLPSession):
    return IntentCommand(90.0, 'wrnm')

@on_command('more', aliases='会说话就多说点', only_to_me=False)
async def _more(session: CommandSession):
    await session.send('你让我说我就说那我岂不是很没面子？')

@on_natural_language(keywords={'智障'}, only_to_me=False)
async def _rannmsl(session : NLPSession):
    return IntentCommand(90.0, 'zz')