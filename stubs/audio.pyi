"""
Get audio samples..

MicroPython module: https://docs.micropython.org/en/preview/library/audio.html

The ``audio`` module is used to record audio samples from a microphone on the Arduino Portenta.

Please read about `PDM Microphones <https://www.st.com/resource/en/application_note/dm00380469-interfacing-pdm-digital-microphones-using-stm32-mcus-and-mpus-stmicroelectronics.pdf>`__.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/audio.rst
from __future__ import annotations
from _typeshed import Incomplete

def init(channels=2, frequency=16000, gain_db=24, highpass=0.9883) -> Incomplete:
    """
    Initializes the audio module. Must be called first before using the audio module.

    ``channels`` specifies the number of audio channels. May be 1 or 2. Audio samples are
    interleaved for two audio channels.

    ``frequency`` is the sample frequency to run at. Running at a higher sample frequency results
    in a higher noise flow which means less effective bits per sample. By default audio samples are
    8-bits with 7-bits of effective dynamic range for voice recording.

    ``gain_db`` is the microphone gain to apply.

    ``highpass`` is the high pass filter cut off given the target sample frequency.
    """
    ...

def deint() -> Incomplete:
    """
    Deinitializes the audio module.
    """
    ...

def start_streaming(callback) -> Incomplete:
    """
    Calls the ``callback`` that takes one argument ``pcmbuf`` automatically forever when enough
    PCM samples have accumulated based on the audio module settings.

    ``pcmbuf`` is a 16-bit array of audio samples sized based on the decimation factor and number
    of channels.

    In single channel mode audio samples will be 8-bits each filling up the 16-bit array.

    In dual channel mode audio samples will be 8-bits each in pairs filling up the 16-bit array.
    """
    ...

def stop_streaming() -> None:
    """
    Stops audio streaming and the callback from being called.
    """
    ...
