from nonebot import *


@on_command('hello', aliases={'hi', '哈喽', '你好', '你好呀', '在', '在不在', '在吗', '在嘛', '你说话啊', '说话'}, only_to_me=False)
async def hello(session: CommandSession):

    await session.send('你好~~发送“功能”查看菜单哦~^O^')



@on_command('morning', aliases={'早呀', '早上好', '早啊', '早安'}, only_to_me=False)
async def hello(session: CommandSession):

    await session.send('早上好~')

@on_command('morning', aliases={'午安', '中午好'}, only_to_me=False)
async def hello(session: CommandSession):

    await session.send('中午好~')

@on_command('morning', aliases={'晚上好'}, only_to_me=False)
async def hello(session: CommandSession):

    await session.send('晚上好~')

@on_command('haha')
async def hello(session: CommandSession):

    await session.send('哈哈哈哈哈嗝')

@on_command('happy')
async def hello(session: CommandSession):

    await session.send('同乐同乐')

@on_command('pic')
async def hello(session: CommandSession):

    await session.send('暂时不支持发图片呢~')

@on_command('robot')
async def hello(session: CommandSession):

    await session.send('对哦，kono机器人哒~')

@on_natural_language(keywords={'哈哈', 'w', '233'}, only_to_me=False)
async def _haha(session : NLPSession):
    return IntentCommand(90.0, 'haha')

@on_natural_language(keywords={'图'}, only_to_me=False)
async def _haha(session : NLPSession):
    return IntentCommand(90.0, 'pic')

@on_natural_language(keywords={'是机器人'}, only_to_me=False)
async def _haha(session : NLPSession):
    return IntentCommand(90.0, 'robot')

@on_natural_language(keywords={'快乐'}, only_to_me=False)
async def _haha(session : NLPSession):
    return IntentCommand(90.0, 'happy')