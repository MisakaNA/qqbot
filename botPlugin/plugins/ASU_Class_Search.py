from nonebot import *
import ASUCourseFinder as f


@on_command('findclass')
async def searching(session: CommandSession):

    classcode = session.get('code', prompt='请输入所查询课程的类型：（如 CSE，MAT）')
    classnum = session.get('num', prompt='请输入所查询课程的三位数编号：（如 101，230）')

    get_class = await get_asu_class(classcode, classnum)
    await session.send(get_class)

async def get_asu_class(classcode: str, classnum: str) -> str:

    classes = f.ASUCourses(classcode, classnum)

    return f'{classes.find_class()}'

@on_natural_language(keywords={'查课', '课程查询', 'kechengchaxun', 'kccx'})
async def _helping(session : NLPSession):
    return IntentCommand(90.0, 'findclass')
