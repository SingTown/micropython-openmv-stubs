"""
Example voice recognition module.

MicroPython module: https://docs.micropython.org/en/preview/library/micro_speech.html

The `micro_speech` module runs Google's TensorFlow Lite for Microcontrollers Micro Speech framework
for voice recognition.

Please see this `guide <https://www.digikey.com/en/maker/projects/how-to-train-new-tensorflow-lite-micro-speech-models/e9480d4a38264604a2bf0336ce11aa9e>`__ for training a new model.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/micro_speech.rst
from __future__ import annotations
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union, NamedTuple, TypeVar
from _typeshed import Incomplete
class MicroSpeech():
    """
       Creates a MicroSpeech voice recognition class.
    """
    def __init__(self) -> None:
        ...
    def audio_callback(self, buf_in) -> Incomplete:
        """
              Pass this method to `audio.start_streaming()` to fill the `MicroSpeech` class with audio samples.
        
              `MicroSpeech` will compute the FFT of the audio samples and keep a sliding window internally
              of the FFT the last 100ms or so of audio samples received as features for voice recognition.
        """
        ...
    def listen(self, tf_model, threshold=0.9, timeout=1000, filter=None: Optional[Any]=None) -> int:
        """
              Executes the tensor flow lite model ``tf_model``, which should be a path to a tensor flow lite
              model on disk, on the audio stream.
        
              This method will continue to execute the model until it classifies a result that has a
              confidence ratio above ``threshold`` and that's within the range specified by ``filter``.
        
              For example, if the model is designed to classify sounds into the four labels ['Silence',
              'Unknown', 'Yes', 'No'], then a ``threshold`` of 0.7 mean that listen() only returns when
              the confidence score for one of those classes goes above 0.7. ``filter`` can then be ``[2, 3]``
              to specify that we only care about 'Yes' or 'No' going above 0.7.
        
              ``timeout`` is the amount of time to run the model on audio data. If zero then listen will
              run forever until a result passes the threshold and filter criteria.
        
              Returns the index of the the label with the highest confidence score. E.g. for the example
              above 0, 1, 2, or 3 for ['Silence', 'Unknown', 'Yes', 'No'] respectively.
        """
        ...
