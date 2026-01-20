# This file makes the folder a *package* and controls what you export.
# Re-export selected names so users can do: from mypkg import greet, add

from .tools import APP_NAME, greet, add, mood

__all__ = ["APP_NAME", "greet", "add", "mood"]
# __all__ is a list of names (strings) that tells Python, “these are the public things from this module/package.
# when using this: from mypkg import *
