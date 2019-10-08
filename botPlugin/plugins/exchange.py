from nonebot import *
import exchangerate as e
import moneycode as c


@on_command('exchange')
async def exchange(session: CommandSession):
    if session.is_first_run:
        await session.send('请输入所持币种的货币代码：（如：USD）')
    duiqian = session.get('duiqian', prompt='若不知道代码请输入“货币帮助”')
    if duiqian == '货币帮助':
        countryname = session.get('countrycode', prompt='请输入所要查询货币代码的国家或地区：（如：中国，美国）')
        get_countrycode = await country_code(countryname)
        await session.send(get_countrycode + '\n如需继续查询汇率请输入“查汇率”或“汇率查询”\n如需继续查询货币代码请输入“货币帮助”')
        return


    duihou = session.get('professor', prompt='请输入兑换币种的货币代码：')
    if duihou == '货币帮助':
        countryname = session.get('countrycode', prompt='请输入所要查询货币代码的国家：（如：中国，美国）')
        get_countrycode = await country_code(countryname)
        await session.send(get_countrycode + '\n如需继续查询汇率请输入“查汇率”或“汇率查询”\n如需继续查询货币代码请输入“货币帮助”')
        return

    get_exchange = await get_exchanges(duiqian, duihou)
    await session.send(get_exchange)


async def get_exchanges(duiqian: str, duihou: str) -> str:

    _exchanges = e.exchange_rates(duiqian, duihou)

    return f'{_exchanges.exchange()}'


async def country_code(countryname: str) -> str:

    codes = c.exchangehelp(countryname)

    return f'{codes.get_code()}'

@on_natural_language(keywords={'货币帮助', 'hbbz'})
async def _helping(session : NLPSession):
    return IntentCommand(90.0, 'helping')

@on_natural_language(keywords={'汇率查询', '查汇率', '汇率', 'hl', 'huilv'}, only_to_me=False)
async def _exchange(session : NLPSession):
    return IntentCommand(90.0, 'exchange')
