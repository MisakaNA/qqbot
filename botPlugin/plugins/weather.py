from nonebot import *
import world_weather as w



@on_command('weather')
async def _weather(session: CommandSession):

    city = session.get('city', prompt='你想查询哪个城市的天气呢？')

    weather_report = await get_weather_of_city(city)

    await session.send(weather_report)


@_weather.args_parser
async def _(session: CommandSession):

    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:

        if stripped_arg:

            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


async def get_weather_of_city(city: str) -> str:
    _weather = w.GetWeather(city)

    return f'{_weather.get_weather()}'

@on_natural_language(keywords={'天气', '天气查询', '查天气', '天气预报'}, only_to_me=False)
async def _translate(session : NLPSession):
    return IntentCommand(90.0, 'weather')

