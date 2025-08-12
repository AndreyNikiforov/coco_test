#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x718cd0e

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

# def factorial(0) = 1

# addpattern def factorial(int() as n if n > 0) = # type: ignore
#     """Compute n! where n is an integer >= 0."""
#     range(1, n+1) |> reduce$(*)

# "hello, world!" |> print

# 1234 |> factorial |> print

# data vector(*pts):
#     """Immutable n-vector."""
#     def __new__(cls, *pts):
#         """Create a new vector from the given pts."""
#         match [v `isinstance` vector] in pts:
#             return v  # vector(v) where v is a vector should return v
#         else:
#             return pts |*> makedata$(cls)  # accesses base constructor
#     def __abs__(self) =
#         """Return the magnitude of the vector."""
#         self.pts |> map$(.**2) |> sum |> (.**0.5)
#     def __add__(self, vector(*other_pts)
#                 if len(other_pts) == len(self.pts)) =
#         """Add two vectors together."""
#         map((+), self.pts, other_pts) |*> vector
#     def __sub__(self, vector(*other_pts)
#                 if len(other_pts) == len(self.pts)) =
#         """Subtract one vector from another."""
#         map((-), self.pts, other_pts) |*> vector
#     def __neg__(self) =
#         """Retrieve the negative of the vector."""
#         self.pts |> map$(-) |*> vector
#     def __mul__(self, other):
#         """Scalar multiplication and dot product."""
#         match vector(*other_pts) in other:
#             assert len(other_pts) == len(self.pts)
#             return map((*), self.pts, other_pts) |> sum  # dot product
#         else:
#             return self.pts |> map$(.*other) |*> vector  # scalar multiplication
#     def __rmul__(self, other) =
#         """Necessary to make scalar multiplication commutative."""
#         self * other
#     def __truediv__(self, other) = self.pts |> map$(./other) |*> vector  # scalar multiplication
#     def unit(self) = self / abs(self)
#     def angle(self, other `isinstance` vector) = math.acos(self.unit() * other.unit())

# # Test cases:
# vector(1, 2, 3) |> print  # vector(*pts=(1, 2, 3))
# vector(4, 5) |> vector |> print  # vector(*pts=(4, 5))
# vector(3, 4) |> abs |> print  # 5
# vector(1, 2) + vector(2, 3) |> print  # vector(*pts=(3, 5))
# vector(2, 2) - vector(0, 1) |> print  # vector(*pts=(2, 1))
# -vector(1, 3) |> print  # vector(*pts=(-1, -3))
# (vector(1, 2) == "string") |> print  # False
# (vector(1, 2) == vector(3, 4)) |> print  # False
# (vector(2, 4) == vector(2, 4)) |> print  # True
# 2*vector(1, 2) |> print  # vector(*pts=(2, 4))
# vector(1, 2) * vector(1, 3) |> print  # 7

# def diagonal_line(n if n >= 0) = range(n+1) |> map$(x => (n - x, x))

# diagonal_line(0) `isinstance` (list, tuple) |> print  # False (should be an iterator)
# diagonal_line(0) |> list |> print  # [(0, 0)]
# diagonal_line(1) |> list |> print  # [(0, 1), (1, 0)]

# def linearized_plane(n=0 if n >= 0) = diagonal_line(n) :: linearized_plane(n+1)

# linearized_plane()$[0] |> print  # (0, 0)
# linearized_plane()$[:3] |> list |> print  # [(0, 0), (0, 1), (1, 0)]
# linearized_plane()$[:5] |> list |> print  # [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1)]

# def vector_field() = linearized_plane() |> starmap$( vector )
# vector_field()$[0] |> print  # vector(*pts=(0, 0))
# vector_field()$[2:3] |> list |> print  # [vector(*pts=(1, 0))]


# vector(3, 4) / 1 |> print  # vector(*pts=(3.0, 4.0))
# vector(2, 4) / 2 |> print  # vector(*pts=(1.0, 2.0))

# vector(0, 1).unit() |> print  # vector(*pts=(0.0, 1.0))
# vector(5, 0).unit() |> print  # vector(*pts=(1.0, 0.0))

# vector(2, 0).angle(vector(3, 0)) |> print  # 0.0
# print(vector(1, 0).angle(vector(0, 2)), math.pi/2)  # should be the same
# vector(1, 2).angle(5)  # MatchError
