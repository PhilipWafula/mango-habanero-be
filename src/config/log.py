import logging
import sys

import structlog
from structlog.types import Processor


def _shared_processors() -> list[Processor]:
    timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False)
    return [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.stdlib.ExtraAdder(),
        timestamper,
        structlog.processors.StackInfoRenderer(),
    ]


def _default_formatter(processors: list[Processor], renderer: Processor):
    return structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer,
        ],
    )


def _logs_renderer(enable_json_logging: bool) -> Processor:
    return (
        structlog.processors.JSONRenderer()
        if enable_json_logging
        else structlog.dev.ConsoleRenderer(colors=True)
    )


def configure_logging(enable_json_logging: bool = False, log_level: str = "INFO"):
    shared_processors = _shared_processors()

    structlog.configure(
        processors=shared_processors
        + [structlog.stdlib.ProcessorFormatter.wrap_for_formatter],
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    renderer = _logs_renderer(enable_json_logging)
    formatter = _default_formatter(shared_processors, renderer)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(log_level.upper())

    for _log in ["_granian"]:
        logging.getLogger(_log).handlers.clear()
        logging.getLogger(_log).propagate = True

    def handle_exception(exc_type, exc_value, exc_traceback):
        """
        Log any uncaught exception instead of letting it be printed by Python
        (but leave KeyboardInterrupt untouched to allow users to Ctrl+C to stop)
        See https://stackoverflow.com/a/16993115/3641865
        """
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        root_logger.error(
            "Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback)
        )

    sys.excepthook = handle_exception


logger = structlog.get_logger("system")
