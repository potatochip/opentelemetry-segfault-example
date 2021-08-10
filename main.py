from opentelemetry.instrumentation.starlette import StarletteInstrumentor
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def route(request) -> dict:
    await request.json()
    return PlainTextResponse("OK", status_code=200)


app = Starlette(
    routes=[
        Route("/", route, methods=["POST"]),
    ],
)
StarletteInstrumentor.instrument_app(app)
