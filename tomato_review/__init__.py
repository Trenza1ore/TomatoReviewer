from pathlib import Path

from openjiuwen.core.common.logging import logger, llm_logger

for lg in [logger, llm_logger]:
    lg.config["output"] = ["file"]
    lg.reconfigure(logger.config)

__version__ = (Path(__file__).parent / "version.txt").read_text().strip()
