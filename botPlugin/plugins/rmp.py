from nonebot import *
import getrating as r


@on_command('rating')
async def rating(session: CommandSession):
    school = session.get('school', prompt='请输入所查询学校的英文全称：')
    professor = session.get('professor', prompt='请输入所查询教授的英文全名：')

    get_rating = await get_rmp_rating(school, professor)
    await session.send(get_rating)

'''
@rating.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['professor'] = stripped_arg

        return

    if not stripped_arg:
        session.pause('要查询的教授名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg
'''

async def get_rmp_rating(school: str, professor: str) -> str:

    ratings = r.rmp(school, professor)

    return f'{ratings.get_rating()}'

@on_natural_language(keywords={'教授评分', '查评分'}, only_to_me=False)
async def _rating(session : NLPSession):
    return IntentCommand(90.0, 'rating')
