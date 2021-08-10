"""Config for gunicorn."""
from typing import Any

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider, export

host = "0.0.0.0"
port = "8000"
bind = f"{host}:{port}"

workers = 1

timeout = 60

worker_class = "uvicorn.workers.UvicornWorker"

keepalive = 120

worker_tmp_dir = "/dev/shm"


def post_fork(server: Any, worker: Any) -> None:
    span_processor = export.BatchSpanProcessor(OTLPSpanExporter())
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(span_processor)
