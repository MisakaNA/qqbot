from nonebot import *
import moneycode as c


@on_command('helping')
async def helping(session: CommandSession):

    countryname = session.get('countrycode', prompt='请输入所要查询货币代码的国家或地区：（如：中国，美国）')
    get_countrycode = await country_code(countryname)

    await session.send(get_countrycode + '\n如需继续查询汇率请输入“查汇率”或“汇率查询”\n如需继续查询货币代码请输入“货币帮助”')

async def country_code(countryname: str) -> str:

    codes = c.exchangehelp(countryname)

    return f'{codes.get_code()}'

@on_natural_language(keywords={'货币帮助'}, only_to_me=False)
async def _helping(session : NLPSession):
    return IntentCommand(90.0, 'helping')
