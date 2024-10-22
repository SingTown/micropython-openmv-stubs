"""
Tensor Flow.

MicroPython module: https://docs.micropython.org/en/preview/library/tf.html

The ``tf`` module is capable of executing Quantized TensorFlow Lite Models
on the OpenMV Cam (not supported on the OpenMV Cam M4).

You can read more about how to create your own models that can run on the
OpenMV Cam `here <https://www.tensorflow.org/lite/microcontrollers>`__. In
particular:

   * Supported operations are listed `here <https://github.com/openmv/tensorflow-lib/blob/master/libtf.cc#L71>`__.

     * Note that tensorflow lite operations are versioned. If no version numbers
       are listed after the operation then the min and max version supported are
       1. If there are numbers after an operation those numbers represent the
       minimum and maximum operation version supported.
     * If you are using Keras to generate your model be careful about only using
       operators that are supported by tensorflow lite for microcontrollers. Otherwise,
       your model will not be runnable by your OpenMV Cam.

   * Convert your model to a FlatBuffer by following the instructions `here <https://www.tensorflow.org/lite/microcontrollers/build_convert#model_conversion>`__.
   * Finally, quantize your model by following the instructions `here <https://www.tensorflow.org/lite/microcontrollers/build_convert#quantization>`__.

Alternatively, just follow Google's in-depth guide `here <https://github.com/openmv/tensorflow/blob/master/tensorflow/lite/micro/examples/person_detection/training_a_model.md>`__.
If you have problems with Google's in-depth guide please contact Google for help.

The final output ``.tflite`` model can be directly loaded and run by your
OpenMV Cam. That said, the model and the model's required sratch RAM must
fit within the available frame buffer stack RAM on your OpenMV Cam.

   * The OpenMV Cam M7 has about 384KB of frame buffer RAM. Please try
     to keep your model and it's required scratch buffer under 320 KB.
   * The OpenMV Cam H7 has about 496KB of frame buffer RAM. Please try
     to keep your model and it's required scratch buffer under 400 KB.
   * The OpenMV Cam H7 Plus has about 31MB of frame buffer RAM. That
     said, running a model anywhere near the that size will be extremely slow.

Alternatively, you can also load a model onto the MicroPython Heap or the OpenMV Cam frame buffer.
However, this significantly limits the model size on all OpenMV Cams.
"""

# source version: preview
# origin module:: repos/micropython/docs/library/tf.rst
from __future__ import annotations
from typing import IO, Any, Callable, Coroutine, Dict, Generator, Iterator, List, NoReturn, Optional, Tuple, Union, NamedTuple, TypeVar
from _typeshed import Incomplete
class tf_classification():
    """
       Please call `tf.classify()` or `tf_model.classify()` to create this object.
    
       Methods
       ~~~~~~~
    """
    def __init__(self) -> None:
        ...
    def rect(self) -> Tuple:
        """
              Returns a rectangle tuple (x, y, w, h) for use with `image` methods
              like `Image.draw_rectangle()` of the tf_classification's bounding box.
        """
        ...
    def x(self) -> the:
        """
              Returns the tf_classification's bounding box x coordinate (int).
        
              You may also get this value doing ``[0]`` on the object.
        """
        ...
    def y(self) -> the:
        """
              Returns the tf_classification's bounding box y coordinate (int).
        
              You may also get this value doing ``[1]`` on the object.
        """
        ...
    def w(self) -> the:
        """
              Returns the tf_classification's bounding box w coordinate (int).
        
              You may also get this value doing ``[2]`` on the object.
        """
        ...
    def h(self) -> the:
        """
              Returns the tf_classification's bounding box h coordinate (int).
        
              You may also get this value doing ``[3]`` on the object.
        """
        ...
    def classification_output(self) -> List:
        """
              Returns a list of the classification label scores. The size of this
              list is determined by your model output channel size. For example,
              mobilenet outputs a list of 1000 classification scores for all 1000
              classes understood by mobilenet. Use ``zip`` in python to combine
              the classification score results with classification labels.
        
              You may also get this value doing ``[4]`` on the object.
        """
        ...
class tf_model():
    """
       Please call `tf.load()` to create the TensorFlow Model object. TensorFlow Model objects allow
       you to execute a model from RAM versus having to load it from disk repeatedly.
    
       Methods
       ~~~~~~~
    """
    def __init__(self) -> None:
        ...
    def len(self) -> bytes:
        """
              Returns the size in bytes of the model.
        """
        ...
    def ram(self) -> bytes:
        """
              Returns the model's required free RAM in bytes.
        """
        ...
    def input_height(self) -> Incomplete:
        """
              Returns the input height of the model. You can use this to size your input
              image height appropriately.
        """
        ...
    def input_width(self) -> Incomplete:
        """
              Returns the input width of the model. You can use this to size your input
              image width appropriately.
        """
        ...
    def input_channels(self) -> int:
        """
              Returns the number of input color channels in the model.
        """
        ...
    def input_datatype(self) -> str:
        """
              Returns the model's input datatype (this is a string of "uint8", "int8", or "float").
        """
        ...
    def input_scale(self) -> Incomplete:
        """
              Returns the input scale for the model.
        """
        ...
    def input_zero_point(self) -> Incomplete:
        """
              Returns the output zero point for the model.
        """
        ...
    def output_height(self) -> Incomplete:
        """
              Returns the output height of the model. You can use this to size your output
              image height appropriately.
        """
        ...
    def output_width(self) -> Incomplete:
        """
              Returns the output width of the model. You can use this to size your output
              image width appropriately.
        """
        ...
    def output_channels(self) -> int:
        """
              Returns the number of output color channels in the model.
        """
        ...
    def output_datatype(self) -> str:
        """
              Returns the model's output datatype (this is a string of "uint8", "int8", or "float").
        """
        ...
    def output_scale(self) -> Incomplete:
        """
              Returns the output scale for the model.
        """
        ...
    def output_zero_point(self) -> Incomplete:
        """
              Returns the output zero point for the model.
        """
        ...
    def classify(self, img, roi, min_scale=1.0, scale_mul=0.5, x_overlap=0, y_overlap=0: Optional[Any]=None) -> List:
        """
              Executes the TensorFlow Lite image classification model on the ``img``
              object and returns a list of `tf_classification` objects. This method
              executes the network multiple times on the image in a controllable sliding
              window type manner (by default the algorithm only executes the network once
              on the whole image frame).
        
              ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
              specified, it is equal to the image rectangle. Only pixels within the
              ``roi`` are operated on.
        
              ``min_scale`` controls how much scaling is applied to the network. At the
              default value the network is not scaled. However, a value of 0.5 would allow
              for detecting objects 50% in size of the image roi size...
        
              ``scale_mul`` controls how many different scales are tested out. The sliding
              window method works by multiplying a default scale of 1 by ``scale_mul``
              while the result is over ``min_scale``. The default value of ``scale_mul``,
              0.5, tests out a 50% size reduction per scale change. However, a value of
              0.95 would only be a 5% size reductioin.
        
              ``x_overlap`` controls the percentage of overlap with the next detector
              area of the sliding window. A value of zero means no overlap. A value of
              0.95 would mean 95% overlap.
        
              ``y_overlap`` controls the percentage of overlap with the next detector
              area of the sliding window. A value of zero means no overlap. A value of
              0.95 would mean 95% overlap.
        """
        ...
    def segment(self, img, roi: Optional[Any]=None) -> List:
        """
              Executes the TensorFlow Lite image segmentation model on the ``img``
              object and returns a list of grayscale `image` objects for each
              segmentation class output channel.
        
              ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
              specified, it is equal to the image rectangle. Only pixels within the
              ``roi`` are operated on.
        """
        ...
    def detect(self, img, roi, thresholds, invert: Optional[Any]=None) -> List:
        """
              Executes the TensorFlow Lite image segmentation model on the ``img``
              object and returns a list of `image.blob` objects for each segmentation
              class output. E.g. if you have an image that's segmented into two classes
              this method will return a list of two lists of blobs that match the requested
              thresholds.
        
              ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
              specified, it is equal to the image rectangle. Only pixels within the
              ``roi`` are operated on.
        
              ``thresholds`` must be a list of tuples
              ``[(lo, hi), (lo, hi), ..., (lo, hi)]`` defining the ranges of color you
              want to track. You may pass up to 32 threshold tuples in one call. Each tuple
              needs to contain two values - a min grayscale value and a max grayscale value.
              Only pixel regions that fall between these thresholds will be considered.
              For easy usage this function will automatically fix swapped min and max values.
              If the tuple is too short the rest of the thresholds are assumed to be at maximum
              range. If no thresholds are specified they are assumed to be (128, 255) which
              will detect "active" pixel regions in the segmented images.
        
              ``invert`` inverts the thresholding operation such that instead of matching
              pixels inside of some known color bounds pixels are matched that are outside
              of the known color bounds.
        """
        ...
    def regression(self, array) -> Incomplete:
        """
              Executes the TensorFlow Lite regression model on the passed array of floats and returns
              a new array of floats as the result. This method accepts 1D/2D/3D arrays which must match
              the input shape of the network. Arrays should be organized in [height][width][channel] order.
        """
        ...
def classify(path, img, roi, min_scale=1.0, scale_mul=0.5, x_overlap=0, y_overlap=0: Optional[Any]=None) -> List:
    """
       Executes the TensorFlow Lite image classification model on the ``img``
       object and returns a list of `tf_classification` objects. This method
       executes the network multiple times on the image in a controllable sliding
       window type manner (by default the algorithm only executes the network once
       on the whole image frame).
    
       ``path`` a path to a ``.tflite`` model to execute on your OpenMV Cam's
       disk. The model is loaded into memory, executed, and released all in
       one function call to save from having to load the model in the
       MicroPython heap. Pass ``"person_detection"`` to load the built-in
       person detection model from your OpenMV Cam's internal flash.
    
       ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
       specified, it is equal to the image rectangle. Only pixels within the
       ``roi`` are operated on.
    
       ``min_scale`` controls how much scaling is applied to the network. At the
       default value the network is not scaled. However, a value of 0.5 would allow
       for detecting objects 50% in size of the image roi size...
    
       ``scale_mul`` controls how many different scales are tested out. The sliding
       window method works by multiplying a default scale of 1 by ``scale_mul``
       while the result is over ``min_scale``. The default value of ``scale_mul``,
       0.5, tests out a 50% size reduction per scale change. However, a value of
       0.95 would only be a 5% size reductioin.
    
       ``x_overlap`` controls the percentage of overlap with the next detector
       area of the sliding window. A value of zero means no overlap. A value of
       0.95 would mean 95% overlap.
    
       ``y_overlap`` controls the percentage of overlap with the next detector
       area of the sliding window. A value of zero means no overlap. A value of
       0.95 would mean 95% overlap.
    """
    ...
def segment(path, img, roi: Optional[Any]=None) -> List:
    """
       Executes the TensorFlow Lite image segmentation model on the ``img``
       object and returns a list of grayscale `image` objects for each
       segmentation class output channel.
    
       ``path`` a path to a ``.tflite`` model to execute on your OpenMV Cam's
       disk. The model is loaded into memory, executed, and released all in
       one function call to save from having to load the model in the
       MicroPython heap.
    
       ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
       specified, it is equal to the image rectangle. Only pixels within the
       ``roi`` are operated on.
    """
    ...
def detect(path, img, roi, thresholds, invert: Optional[Any]=None) -> List:
    """
       Executes the TensorFlow Lite image segmentation model on the ``img``
       object and returns a list of `image.blob` objects for each segmentation
       class output. E.g. if you have an image that's segmented into two classes
       this method will return a list of two lists of blobs that match the requested
       thresholds.
    
       ``path`` a path to a ``.tflite`` model to execute on your OpenMV Cam's
       disk. The model is loaded into memory, executed, and released all in
       one function call to save from having to load the model in the
       MicroPython heap.
    
       ``roi`` is the region-of-interest rectangle tuple (x, y, w, h). If not
       specified, it is equal to the image rectangle. Only pixels within the
       ``roi`` are operated on.
    
       ``thresholds`` must be a list of tuples
       ``[(lo, hi), (lo, hi), ..., (lo, hi)]`` defining the ranges of color you
       want to track. You may pass up to 32 threshold tuples in one call. Each tuple
       needs to contain two values - a min grayscale value and a max grayscale value.
       Only pixel regions that fall between these thresholds will be considered.
       For easy usage this function will automatically fix swapped min and max values.
       If the tuple is too short the rest of the thresholds are assumed to be at maximum
       range. If no thresholds are specified they are assumed to be (128, 255) which
       will detect "active" pixel regions in the segmented images.
    
       ``invert`` inverts the thresholding operation such that instead of matching
       pixels inside of some known color bounds pixels are matched that are outside
       of the known color bounds.
    """
    ...
def regression(path, array) -> Incomplete:
    """
       Executes the TensorFlow Lite regression model on the passed array of floats and returns
       a new array of floats as the result. This method accepts 1D/2D/3D arrays which must match
       the input shape of the network. Arrays should be organized in [height][width][channel] order.
    
       ``path`` a path to a ``.tflite`` model to execute on your OpenMV Cam's
       disk. The model is loaded into memory, executed, and released all in
       one function call to save from having to load the model in the
       MicroPython heap.
    """
    ...
def load(path, load_to_fb=False: Optional[Any]=None) -> tfmodel:
    """
       ``path`` a path to a ``.tflite`` model to load into memory on the MicroPython heap by default.
    
       NOTE! The MicroPython heap is only ~50 KB on the OpenMV Cam M7 and ~256 KB on the OpenMV Cam H7.
    
       Pass ``"person_detection"`` to load the built-in person detection model from your
       OpenMV Cam's internal flash. This built-in model does not use any Micropython Heap
       as all the weights are stored in flash which is accessible in the same way as RAM.
    
       ``load_to_fb`` if passed as True will instead reserve part of the OpenMV Cam frame buffer
       stack for storing the TensorFlow Lite model. You will get the most efficent execution
       performance for large models that do not fit on the heap by loading them into frame buffer
       memory once from disk and then repeatedly executing the model. That said, the frame buffer
       space used will not be available anymore for other algorithms.
    
       Returns a `tf_model` object which can operate on an image.
    """
    ...
def free_from_fb() -> Incomplete:
    """
       Deallocates a previously allocated `tf_model` object created with ``load_to_fb`` set to True.
    
       Note that deallocations happen in the reverse order of allocation.
    """
    ...
