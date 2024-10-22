"""
OpenMV Cam Information.

MicroPython module: https://docs.micropython.org/en/preview/library/omv.html

The ``omv`` module is used to get OpenMV Cam information.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/omv.rst
from __future__ import annotations
from typing import Any, Optional
from _typeshed import Incomplete

def version_major() -> int:
    """
    Returns the major version number (int).
    """
    ...

def version_minor() -> int:
    """
    Returns the minor version number (int).
    """
    ...

def version_patch() -> int:
    """
    Returns the patch version number (int).
    """
    ...

def version_string() -> str:
    """
    Returns the version string (e.g. "2.8.0").
    """
    ...

def arch() -> str:
    """
    Returns the board architecture string. This string is really just meant for
    OpenMV IDE but you can get it with this function.
    """
    ...

def board_type() -> str:
    """
    Returns the board type string. This string is really just meant for
    OpenMV IDE but you can get it with this function.
    """
    ...

def board_id() -> str:
    """
    Returns the board id string. This string is really just meant for
    OpenMV IDE but you can get it with this function.
    """
    ...

def disable_fb(disable: Optional[Any] = None) -> bool:
    """
    When ``disable`` is set to ``True`` the OpenMV Cam will no longer jpeg compress images and stream
    them to OpenMV IDE. The IDE may still poll for images unless ``Disable FB`` is checked in OpenMV
    IDE. You may wish to disable the frame buffer when streaming images over to another system while
    debugging you script with OpenMV IDE. If no arguments are passed this function will return
    ``True`` if the frame buffer is disabled and ``False`` if not.

    .. note::

       This is a different flag than the ``Disable FB`` button in OpenMV IDE.
    """
    ...
