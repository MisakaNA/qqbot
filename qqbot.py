import nonebot
from os import path
import config



@nonebot.on_request('group')
async def handle_request(session : nonebot.RequestSession):
    await session.approve()



if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'botPlugin', 'plugins'),
        'botPlugin.plugins'
    )
    nonebot.run(host='127.0.0.1', port=8080)