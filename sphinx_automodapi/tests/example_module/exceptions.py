__all__ = ["SomeError", "ClassMethodError"]


class SomeError(Exception):
    """For some kind of error."""

    def normalMethod(self):
        """A normal method on an exception."""
        return


class ClassMethodError(Exception):
    """Getting text for classmethods on Exceptions."""

    @classmethod
    def classMethod():
        """A class method on an exception."""
        return
