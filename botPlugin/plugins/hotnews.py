from nonebot import on_command, CommandSession
import get_hotnews as h


@on_command('hot', aliases=('热点新闻', '新闻', '搜索热点', '查新闻', 'xw'), only_to_me=False)
async def _hotnews(session: CommandSession):
    if session.is_first_run:
        news_list = await get_hot_news_list()
        await session.send(news_list)

    choice = session.get('choice', prompt='查看消息内容请输入编号：')

    if 0 <int(choice) > 10:
        return '不对不对，编号超出范围啦'

    newsarticle = await hot_news(choice)

    await session.send(newsarticle)


async def get_hot_news_list():
    _news_list = h.hotNews()
    _news_list.get_news_list()
    return f'{_news_list.list_toStrng()}'


async def hot_news(choice: str) -> str:
    _news = h.hotNews()
    _news.get_news_list()
    return f'{_news.get_news_detail(choice)}'
