from nonebot import on_command, CommandSession
import get_weather as g


__plugin_usage__ = r""
@on_command('chinaweather', aliases={'中国天气'}, only_to_me=False)
async def weather(session: CommandSession):

    city = session.get('city', prompt='你想查询哪个城市的天气呢？')

    weather_report = await get_weather_of_city(city)

    await session.send(weather_report)


@weather.args_parser
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
    _weather = g.GetWeather(city)
    get_city = _weather.get_city()

    if get_city == -1:
        return f'{"啊哦，没有这个城市哦。。"}'
    else:
        return f'{_weather.get_weather()}'

