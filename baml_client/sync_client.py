###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Any, Dict, List, Optional, TypeVar, Union, TypedDict, Type, Literal, cast
from typing_extensions import NotRequired
import pprint

import baml_py
from pydantic import BaseModel, ValidationError, create_model

from . import partial_types, types
from .types import Checked, Check
from .type_builder import TypeBuilder
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME

OutputType = TypeVar('OutputType')

# Define the TypedDict with optional parameters having default values
class BamlCallOptions(TypedDict, total=False):
    tb: NotRequired[TypeBuilder]
    client_registry: NotRequired[baml_py.baml_py.ClientRegistry]

class BamlSyncClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __stream_client: "BamlStreamClient"

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__stream_client = BamlStreamClient(self.__runtime, self.__ctx_manager)

    @property
    def stream(self):
      return self.__stream_client

    
    def ChooseATool(
        self,
        user_image: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> Union[types.Appointment, types.NutritionLabel, types.DropOffPackageReceipt]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ChooseATool",
        {
          "user_image": user_image,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(Union[types.Appointment, types.NutritionLabel, types.DropOffPackageReceipt], raw.cast_to(types, types, partial_types, False))
    
    def ExtractAppointmentFromImage(
        self,
        appointment_card: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> types.Appointment:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractAppointmentFromImage",
        {
          "appointment_card": appointment_card,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.Appointment, raw.cast_to(types, types, partial_types, False))
    
    def ExtractDropOffPackageReceiptFromImage(
        self,
        package_label: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> types.DropOffPackageReceipt:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractDropOffPackageReceiptFromImage",
        {
          "package_label": package_label,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.DropOffPackageReceipt, raw.cast_to(types, types, partial_types, False))
    
    def ExtractNutritionLabelFromImage(
        self,
        nutrition_label: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> types.NutritionLabel:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractNutritionLabelFromImage",
        {
          "nutrition_label": nutrition_label,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      return cast(types.NutritionLabel, raw.cast_to(types, types, partial_types, False))
    



class BamlStreamClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager

    
    def ChooseATool(
        self,
        user_image: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[Union[partial_types.Appointment, partial_types.NutritionLabel, partial_types.DropOffPackageReceipt]], Union[types.Appointment, types.NutritionLabel, types.DropOffPackageReceipt]]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ChooseATool",
        {
          "user_image": user_image,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[Optional[Union[partial_types.Appointment, partial_types.NutritionLabel, partial_types.DropOffPackageReceipt]], Union[types.Appointment, types.NutritionLabel, types.DropOffPackageReceipt]](
        raw,
        lambda x: cast(Optional[Union[partial_types.Appointment, partial_types.NutritionLabel, partial_types.DropOffPackageReceipt]], x.cast_to(types, types, partial_types, True)),
        lambda x: cast(Union[types.Appointment, types.NutritionLabel, types.DropOffPackageReceipt], x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def ExtractAppointmentFromImage(
        self,
        appointment_card: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Appointment, types.Appointment]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractAppointmentFromImage",
        {
          "appointment_card": appointment_card,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.Appointment, types.Appointment](
        raw,
        lambda x: cast(partial_types.Appointment, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.Appointment, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def ExtractDropOffPackageReceiptFromImage(
        self,
        package_label: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.DropOffPackageReceipt, types.DropOffPackageReceipt]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractDropOffPackageReceiptFromImage",
        {
          "package_label": package_label,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.DropOffPackageReceipt, types.DropOffPackageReceipt](
        raw,
        lambda x: cast(partial_types.DropOffPackageReceipt, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.DropOffPackageReceipt, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    
    def ExtractNutritionLabelFromImage(
        self,
        nutrition_label: baml_py.Image,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.NutritionLabel, types.NutritionLabel]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb # type: ignore (we know how to use this private attribute)
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractNutritionLabelFromImage",
        {
          "nutrition_label": nutrition_label,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      return baml_py.BamlSyncStream[partial_types.NutritionLabel, types.NutritionLabel](
        raw,
        lambda x: cast(partial_types.NutritionLabel, x.cast_to(types, types, partial_types, True)),
        lambda x: cast(types.NutritionLabel, x.cast_to(types, types, partial_types, False)),
        self.__ctx_manager.get(),
      )
    

b = BamlSyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)

__all__ = ["b"]