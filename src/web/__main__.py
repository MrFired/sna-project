import uvicorn

from src.web.app import app, config

config = uvicorn.Config(
    app,
    host="0.0.0.0",  # noqa: S104
    port=config.PORT,
    log_level=config.LOG_LEVEL,
)
server = uvicorn.Server(config)
server.run()
