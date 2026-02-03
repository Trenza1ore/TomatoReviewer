"""
Compatibility layer for AgentSession.

This module provides a compatibility wrapper for AgentSession that adds
the get_session_id() method for backward compatibility.
"""

from typing import Optional

from openjiuwen.core.session.checkpointer.base import Checkpointer
from openjiuwen.core.session.config.base import Config
from openjiuwen.core.session.internal.agent import AgentSession as BaseAgentSession


class AgentSession(BaseAgentSession):
    """Compatibility wrapper for AgentSession that adds get_session_id() method.

    This class extends the upstream AgentSession to provide a get_session_id()
    method for backward compatibility with code that expects this method.
    """

    def __init__(
        self,
        session_id: str,
        config: Optional[Config] = None,
        checkpointer: Optional[Checkpointer] = None,
        card=None,
    ):
        """Initialize AgentSession with compatibility layer.

        Args:
            session_id: Unique session identifier
            config: Optional session configuration
            checkpointer: Optional checkpointer for session state
            card: Optional agent card
        """
        super().__init__(session_id, config, checkpointer, card)

    def get_session_id(self) -> str:
        """Get the session ID.

        This method provides compatibility with code that expects get_session_id()
        instead of the session_id() property method.

        Returns:
            The session ID string
        """
        return self.session_id()


__all__ = ["AgentSession"]
