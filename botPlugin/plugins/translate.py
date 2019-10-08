from nonebot import *
import google_translate as g

@on_command('translate')
async def translate(session: CommandSession):

    language = session.get('language', prompt='请输入目标语种')
    transstr = session.get('professor', prompt='请输入所需要翻译的内容：')

    trans_result = await get_translate(language, transstr)
    await session.send(trans_result)


async def get_translate(language: str, transstr: str) -> str:

    trans = g.translateapi(language, transstr)

    return f'{trans.get_translate_result()}'

@on_natural_language(keywords={'翻译', 'fy', 'fanyi'}, only_to_me=False)
async def _translate(session : NLPSession):
    return IntentCommand(90.0, 'translate')