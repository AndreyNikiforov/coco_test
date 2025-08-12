#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x25ea2ac

# Compiled with Coconut version 3.1.2

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.2', '313', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == '__coconut__':  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

#!/usr/bin/env coconut-run

if _coconut.typing.TYPE_CHECKING:  #3 (line in Coconut source)
    from typing import Mapping  #3 (line in Coconut source)
else:  #3 (line in Coconut source)
    try:  #3 (line in Coconut source)
        Mapping = _coconut.typing.Mapping  #3 (line in Coconut source)
    except _coconut.AttributeError as _coconut_imp_err:  #3 (line in Coconut source)
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3 (line in Coconut source)
if _coconut.typing.TYPE_CHECKING:  #3 (line in Coconut source)
    from typing import Sequence  #3 (line in Coconut source)
else:  #3 (line in Coconut source)
    try:  #3 (line in Coconut source)
        Sequence = _coconut.typing.Sequence  #3 (line in Coconut source)
    except _coconut.AttributeError as _coconut_imp_err:  #3 (line in Coconut source)
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3 (line in Coconut source)
if _coconut.typing.TYPE_CHECKING:  #3 (line in Coconut source)
    from typing import Literal  #3 (line in Coconut source)
else:  #3 (line in Coconut source)
    try:  #3 (line in Coconut source)
        Literal = _coconut.typing.Literal  #3 (line in Coconut source)
    except _coconut.AttributeError as _coconut_imp_err:  #3 (line in Coconut source)
        raise _coconut.ImportError(_coconut.str(_coconut_imp_err))  #3 (line in Coconut source)


# rfc8259
type JSON_Null = None  #7 (line in Coconut source)
type JSON_True = Literal[True]  #8 (line in Coconut source)
type JSON_False = Literal[False]  #9 (line in Coconut source)
type JSON_Number = int | float  #10 (line in Coconut source)
type JSON_String = str  #11 (line in Coconut source)
type JSON_Object[T: JSON_Value] = Mapping[str, T]  #12 (line in Coconut source)
type JSON_Array[T: JSON_Value] = Sequence[T]  #13 (line in Coconut source)
type JSON_Value[T: JSON_Value] = JSON_Null | JSON_True | JSON_False | JSON_Number | JSON_String | JSON_Object[T] | JSON_Array[T]  #14 (line in Coconut source)

# How to do "parser combinators" for json mapping?
# def safe_get_item[T <: JSON_Value](field: str) -> (JSON_Object[T] -> Expected[T]) =
#     (.[field]) |> safe_call$

# {"fields": "abc"} |> safe_get_item("fields") |>  print
# ex: JSON_Object[JSON_Object[str]] = {"fields": {"res": "def"}}
# {"fields": {"res": "def"}} |> (safe_get_item("fields") ..> fmap$(safe_get_item("res")) ..> .join()) |> print

# # stricter typed defs
# type J_value[T : (str, int, float)] = JSON_Object[T]
# type J_fields[T <: J_value] = JSON_Object[T]

# # reading value into typed value
# safe_cast_int: Any -> Expected[int] = int$ ..> safe_call$
# safe_cast_float: Any -> Expected[int] = float$ ..> safe_call$

# safe_value = safe_get_item("value")
# p_value_int[T]: J_value[T] -> Expected[int] = safe_value ..> fmap$(safe_cast_int) ..> .join()
# p_fields[T]: J_fields[T] -> Expected[int] = safe_get_item("fields") ..> fmap$(p_value_int[T]) ..> .join()

# def error_to_none[T](r: Expected[T]) -> Optional[T] = r |> .result_or_else(_ => None)

# p_f = p_fields ..> error_to_none

# {"fields": {"value": 10}} |> p_fields |> print      # 10
# {"fields": {"value": {}}} |> p_fields |> print      # Expected(TypeError)
# {"fields": {"value": "abc"}} |> p_fields |> print   # Expected(ValueError)
# {"fields": {"value": None}} |> p_fields |> print    # Expected(TypeError)
# {"fields": {"value": 11.2}} |> p_fields |> print    # 11
# {"fieldsX": {"value": 11.2}} |> p_fields |> print   # Expected(KeyError)

# {"fields": {"value": 11.2}} |> p_f |> print   # None

# add_two: int -> int = x => x + 2
# p_valid = p_f ..> fmap$(add_two) ..> .join()
# {"fields": {"value": 11.2}} |> p_valid |> print

# # should catch incorrect types at compile time
# app_abc: str -> str = x => x + "aaa"
# p_invalid = p_f ..> fmap$(app_abc) ..> .join()
# {"fields": {"value": 11.2}} |> p_invalid |> print
