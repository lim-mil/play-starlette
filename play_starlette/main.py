import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route

from play_starlette import config

routes = [

]


middleware = [

]


on_startup = [

]


on_shutdown = [

]


app = Starlette(debug=True, routes=routes, middleware=middleware, on_startup=on_startup, on_shutdown=on_shutdown, )


if __name__ == '__main__':
    uvicorn.run(app, reload=True, host=config.HOST, port=config.PORT)
