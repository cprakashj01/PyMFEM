# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_vector')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_vector')
    _vector = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vector', [dirname(__file__)])
        except ImportError:
            import _vector
            return _vector
        try:
            _mod = imp.load_module('_vector', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _vector = swig_import_helper()
    del swig_import_helper
else:
    import _vector
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import array
import ostream_typemap

def add_vector(*args):
    return _vector.add_vector(*args)
add_vector = _vector.add_vector

def subtract_vector(*args):
    return _vector.subtract_vector(*args)
subtract_vector = _vector.subtract_vector

def CheckFinite(v, n):
    return _vector.CheckFinite(v, n)
CheckFinite = _vector.CheckFinite
class Vector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr

    def Load(self, *args):
        return _vector.Vector_Load(self, *args)

    def SetSize(self, s):
        return _vector.Vector_SetSize(self, s)

    def SetData(self, d):
        return _vector.Vector_SetData(self, d)

    def SetDataAndSize(self, d, s):
        return _vector.Vector_SetDataAndSize(self, d, s)

    def NewDataAndSize(self, d, s):
        return _vector.Vector_NewDataAndSize(self, d, s)

    def MakeDataOwner(self):
        return _vector.Vector_MakeDataOwner(self)

    def Destroy(self):
        return _vector.Vector_Destroy(self)

    def Size(self):
        return _vector.Vector_Size(self)

    def Capacity(self):
        return _vector.Vector_Capacity(self)

    def GetData(self):
        return _vector.Vector_GetData(self)

    def OwnsData(self):
        return _vector.Vector_OwnsData(self)

    def StealData(self, *args):
        return _vector.Vector_StealData(self, *args)

    def Elem(self, *args):
        return _vector.Vector_Elem(self, *args)

    def __call__(self, *args):
        return _vector.Vector___call__(self, *args)

    def __mul__(self, *args):
        return _vector.Vector___mul__(self, *args)

    def __imul__(self, v):
        ret = _vector.Vector___imul__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0            
        return self



    def __itruediv__(self, v):
        ret = _vector.Vector___itruediv__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0      
        return self



    def __isub__(self, v):
        ret = _vector.Vector___isub__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0            
        return self



    def __iadd__(self, v):
        ret = _vector.Vector___iadd__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0                  
        return self



    def Add(self, a, Va):
        return _vector.Vector_Add(self, a, Va)

    def Set(self, a, x):
        return _vector.Vector_Set(self, a, x)

    def SetVector(self, v, offset):
        return _vector.Vector_SetVector(self, v, offset)

    def Neg(self):
        return _vector.Vector_Neg(self)

    def Swap(self, other):
        return _vector.Vector_Swap(self, other)

    def median(self, lo, hi):
        return _vector.Vector_median(self, lo, hi)

    def GetSubVector(self, *args):
        return _vector.Vector_GetSubVector(self, *args)

    def SetSubVector(self, *args):
        return _vector.Vector_SetSubVector(self, *args)

    def AddElementVector(self, *args):
        return _vector.Vector_AddElementVector(self, *args)

    def SetSubVectorComplement(self, dofs, val):
        return _vector.Vector_SetSubVectorComplement(self, dofs, val)

    def Print(self, *args):
        return _vector.Vector_Print(self, *args)

    def Print_HYPRE(self, out):
        return _vector.Vector_Print_HYPRE(self, out)

    def Randomize(self, seed=0):
        return _vector.Vector_Randomize(self, seed)

    def Norml2(self):
        return _vector.Vector_Norml2(self)

    def Normlinf(self):
        return _vector.Vector_Normlinf(self)

    def Norml1(self):
        return _vector.Vector_Norml1(self)

    def Normlp(self, p):
        return _vector.Vector_Normlp(self, p)

    def Max(self):
        return _vector.Vector_Max(self)

    def Min(self):
        return _vector.Vector_Min(self)

    def Sum(self):
        return _vector.Vector_Sum(self)

    def DistanceSquaredTo(self, p):
        return _vector.Vector_DistanceSquaredTo(self, p)

    def DistanceTo(self, p):
        return _vector.Vector_DistanceTo(self, p)

    def CheckFinite(self):
        return _vector.Vector_CheckFinite(self)
    __swig_destroy__ = _vector.delete_Vector
    __del__ = lambda self: None

    def __init__(self, *args):

        from numpy import ndarray, ascontiguousarray
        keep_link = False
        own_data = False  
        if len(args) == 1:
            if isinstance(args[0], list): 
                args = (args[0], len(args[0]))
                own_data = True	  
            elif isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                    raise ValueError('Must be float64 array')
                else:
          	    args = (ascontiguousarray(args[0]), args[0].shape[0])
        # in this case, args[0] need to be maintained
        # in this object.
        	    keep_link = True


        this = _vector.new_Vector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        if keep_link:
           self._link_to_data = args[0]
        if own_data:
           self.MakeDataOwner()




    def Assign(self, *args):

        from numpy import ndarray, ascontiguousarray
        if len(args) == 1 and isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                    raise ValueError('Must be float64 array')
                elif args[0].ndim != 1:
                    raise ValueError('Ndim must be one') 
                elif args[0].shape[0] != _vector.Vector_Size(self):
                    raise ValueError('Length does not match')
                else:
          	    args = (ascontiguousarray(args[0]),)


        val = _vector.Vector_Assign(self, *args)

        return self


        return val


    def __setitem__(self, i, v):
        return _vector.Vector___setitem__(self, i, v)

    def __getitem__(self, param):
        return _vector.Vector___getitem__(self, param)

    def GetDataArray(self):
        return _vector.Vector_GetDataArray(self)
Vector_swigregister = _vector.Vector_swigregister
Vector_swigregister(Vector)


def IsFinite(val):
    return _vector.IsFinite(val)
IsFinite = _vector.IsFinite

def DistanceSquared(x, y, n):
    return _vector.DistanceSquared(x, y, n)
DistanceSquared = _vector.DistanceSquared

def Distance(x, y, n):
    return _vector.Distance(x, y, n)
Distance = _vector.Distance

Vector.__idiv__ = Vector.__itruediv__

# This file is compatible with both classic and new-style classes.


