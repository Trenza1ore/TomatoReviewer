__all__ = ["__version__", "PYLINT_FALLBACK", "DEBUG_MODE"]

from pathlib import Path

from openjiuwen.core.common.logging import llm_logger, logger

for lg in [logger, llm_logger]:
    lg.config["output"] = ["file"]
    lg.reconfigure(logger.config)

__version__ = (Path(__file__).parent / "version.txt").read_text().strip()
PYLINT_FALLBACK = (Path(__file__).parent / ".pylintrc").absolute()
DEBUG_MODE = False
