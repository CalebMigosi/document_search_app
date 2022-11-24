import sys
import logging
import logging.config
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers.store import store
from api.routers.check import check
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client


def create_app():
    '''
        Factory method for creating app to deal with potential proxy redirects
        and to define bespoke features elsewhere other than on main.

        Unnecessary but I also wanted to have a clean log when the app loads.
    '''
    try:
        # Load logger
        logging.config.fileConfig("./config/logging.conf")
        logger = logging.getLogger("root")

        # Create elastic APM client
        apm = make_apm_client(
            {"SERVICE_NAME": "fastapi-app", "SERVER_URL": "http://apm-server:8200"} # noqa
        )

        app = FastAPI()

        # Add routers
        app.include_router(store)
        app.include_router(check)

        # Add middleware
        origins = ["*"]
        app.add_middleware(ElasticAPM, client=apm)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=False,
            allow_headers=["*"],
            allow_methods=["POST", "GET"],
            expose_headers=["Access-Control-Allow-Origin"]
        )

        # Should log successfully
        logger.info("Application successfully loaded")
        return app

    except Exception as e:
        # Lots of next lines because I fail to see the errors sometimes
        logging.error(f"""\n\nApp failed to load.\n\n{e}\n\n""", exc_info=True)

        # Exit
        sys.exit()


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)