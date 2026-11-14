from abc import ABC, abstractmethod

from pytimewarp.event import Event
from pytimewarp.logical_process import LogicalProcess
from pytimewarp.state import State


class Model(ABC):
    """Model base class (abstract)

    Defines the methods required for all models to implement.
    """

    def __init__(self, s: State, lp: LogicalProcess) -> None:
        self.state = s
        self.lp = lp
        lp.model = self

    @abstractmethod
    def event_handler(self, e: Event, s: State, lp: LogicalProcess):
        """Forward event handler.

        Args:
            e (Event): The event to process.
        """
        pass

    @abstractmethod
    def reverse_event_handler(self, e: Event, s: State, lp: LogicalProcess):
        """Reverse event handler

        Required only for Optimistic engine.

        Args:
            e (Event): The event to reverse.
        """
        pass
