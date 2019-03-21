"""The Console Environment."""

from typing import Type, TypeVar

from j5.backends import Environment

ConsoleEnvironment = Environment("ConsoleEnvironment")

T = TypeVar("T")


class Console:
    """A helper class for the comsole environment."""

    def __init__(self, descriptor: str) -> None:
        self. _descriptor = descriptor

    def info(self, message: str) -> None:
        """Print information to the user."""
        print(f"{self._descriptor}: {message}")

    def read(self, prompt: str, return_type: Type[T] = str) -> T:  # type: ignore
        """
        Get a value of type 'return_type'.

        We have to ignore the types on this function unfortunately, as static type
        checking is not powerful enough to confirm that it is correct at runtime.
        """
        while True:
            response = input(f"{self._descriptor}: {prompt}: ")
            try:
                return return_type(response)  # type: ignore
            except ValueError:
                self.info(f"Unable to construct a {return_type.__name__}"
                          f" from '{response}'")
