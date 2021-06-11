# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _operators
else:
    import _operators

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _operators.SWIG_PyInstanceMethod_New
_swig_new_static_method = _operators.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
class Operator(object):
    r"""Proxy of C++ mfem::Operator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    DIAG_ZERO = _operators.Operator_DIAG_ZERO
    
    DIAG_ONE = _operators.Operator_DIAG_ONE
    
    DIAG_KEEP = _operators.Operator_DIAG_KEEP
    

    def InitTVectors(self, Po, Ri, Pi, x, b, X, B):
        r"""InitTVectors(Operator self, Operator Po, Operator Ri, Operator Pi, Vector x, Vector b, Vector X, Vector B)"""
        return _operators.Operator_InitTVectors(self, Po, Ri, Pi, x, b, X, B)
    InitTVectors = _swig_new_instance_method(_operators.Operator_InitTVectors)

    def __init__(self, *args):
        r"""
        __init__(Operator self, int s=0) -> Operator
        __init__(Operator self, int h, int w) -> Operator
        """
        if self.__class__ == Operator:
            _self = None
        else:
            _self = self
        _operators.Operator_swiginit(self, _operators.new_Operator(_self, *args))

    def Height(self):
        r"""Height(Operator self) -> int"""
        return _operators.Operator_Height(self)
    Height = _swig_new_instance_method(_operators.Operator_Height)

    def NumRows(self):
        r"""NumRows(Operator self) -> int"""
        return _operators.Operator_NumRows(self)
    NumRows = _swig_new_instance_method(_operators.Operator_NumRows)

    def Width(self):
        r"""Width(Operator self) -> int"""
        return _operators.Operator_Width(self)
    Width = _swig_new_instance_method(_operators.Operator_Width)

    def NumCols(self):
        r"""NumCols(Operator self) -> int"""
        return _operators.Operator_NumCols(self)
    NumCols = _swig_new_instance_method(_operators.Operator_NumCols)

    def GetMemoryClass(self):
        r"""GetMemoryClass(Operator self) -> mfem::MemoryClass"""
        return _operators.Operator_GetMemoryClass(self)
    GetMemoryClass = _swig_new_instance_method(_operators.Operator_GetMemoryClass)

    def Mult(self, x, y):
        r"""Mult(Operator self, Vector x, Vector y)"""
        return _operators.Operator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.Operator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(Operator self, Vector x, Vector y)"""
        return _operators.Operator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.Operator_MultTranspose)

    def GetGradient(self, x):
        r"""GetGradient(Operator self, Vector x) -> Operator"""
        return _operators.Operator_GetGradient(self, x)
    GetGradient = _swig_new_instance_method(_operators.Operator_GetGradient)

    def AssembleDiagonal(self, diag):
        r"""AssembleDiagonal(Operator self, Vector diag)"""
        return _operators.Operator_AssembleDiagonal(self, diag)
    AssembleDiagonal = _swig_new_instance_method(_operators.Operator_AssembleDiagonal)

    def GetProlongation(self):
        r"""GetProlongation(Operator self) -> Operator"""
        return _operators.Operator_GetProlongation(self)
    GetProlongation = _swig_new_instance_method(_operators.Operator_GetProlongation)

    def GetRestriction(self):
        r"""GetRestriction(Operator self) -> Operator"""
        return _operators.Operator_GetRestriction(self)
    GetRestriction = _swig_new_instance_method(_operators.Operator_GetRestriction)

    def GetOutputProlongation(self):
        r"""GetOutputProlongation(Operator self) -> Operator"""
        return _operators.Operator_GetOutputProlongation(self)
    GetOutputProlongation = _swig_new_instance_method(_operators.Operator_GetOutputProlongation)

    def GetOutputRestrictionTranspose(self):
        r"""GetOutputRestrictionTranspose(Operator self) -> Operator"""
        return _operators.Operator_GetOutputRestrictionTranspose(self)
    GetOutputRestrictionTranspose = _swig_new_instance_method(_operators.Operator_GetOutputRestrictionTranspose)

    def GetOutputRestriction(self):
        r"""GetOutputRestriction(Operator self) -> Operator"""
        return _operators.Operator_GetOutputRestriction(self)
    GetOutputRestriction = _swig_new_instance_method(_operators.Operator_GetOutputRestriction)

    def FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior=0):
        r"""FormLinearSystem(Operator self, intArray ess_tdof_list, Vector x, Vector b, mfem::Operator *& A, Vector X, Vector B, int copy_interior=0)"""
        return _operators.Operator_FormLinearSystem(self, ess_tdof_list, x, b, A, X, B, copy_interior)
    FormLinearSystem = _swig_new_instance_method(_operators.Operator_FormLinearSystem)

    def FormRectangularLinearSystem(self, trial_tdof_list, test_tdof_list, x, b, A, X, B):
        r"""FormRectangularLinearSystem(Operator self, intArray trial_tdof_list, intArray test_tdof_list, Vector x, Vector b, mfem::Operator *& A, Vector X, Vector B)"""
        return _operators.Operator_FormRectangularLinearSystem(self, trial_tdof_list, test_tdof_list, x, b, A, X, B)
    FormRectangularLinearSystem = _swig_new_instance_method(_operators.Operator_FormRectangularLinearSystem)

    def RecoverFEMSolution(self, X, b, x):
        r"""RecoverFEMSolution(Operator self, Vector X, Vector b, Vector x)"""
        return _operators.Operator_RecoverFEMSolution(self, X, b, x)
    RecoverFEMSolution = _swig_new_instance_method(_operators.Operator_RecoverFEMSolution)

    def FormSystemOperator(self, ess_tdof_list, A):
        r"""FormSystemOperator(Operator self, intArray ess_tdof_list, mfem::Operator *& A)"""
        return _operators.Operator_FormSystemOperator(self, ess_tdof_list, A)
    FormSystemOperator = _swig_new_instance_method(_operators.Operator_FormSystemOperator)

    def FormRectangularSystemOperator(self, trial_tdof_list, test_tdof_list, A):
        r"""FormRectangularSystemOperator(Operator self, intArray trial_tdof_list, intArray test_tdof_list, mfem::Operator *& A)"""
        return _operators.Operator_FormRectangularSystemOperator(self, trial_tdof_list, test_tdof_list, A)
    FormRectangularSystemOperator = _swig_new_instance_method(_operators.Operator_FormRectangularSystemOperator)

    def FormDiscreteOperator(self, A):
        r"""FormDiscreteOperator(Operator self, mfem::Operator *& A)"""
        return _operators.Operator_FormDiscreteOperator(self, A)
    FormDiscreteOperator = _swig_new_instance_method(_operators.Operator_FormDiscreteOperator)
    __swig_destroy__ = _operators.delete_Operator
    ANY_TYPE = _operators.Operator_ANY_TYPE
    
    MFEM_SPARSEMAT = _operators.Operator_MFEM_SPARSEMAT
    
    Hypre_ParCSR = _operators.Operator_Hypre_ParCSR
    
    PETSC_MATAIJ = _operators.Operator_PETSC_MATAIJ
    
    PETSC_MATIS = _operators.Operator_PETSC_MATIS
    
    PETSC_MATSHELL = _operators.Operator_PETSC_MATSHELL
    
    PETSC_MATNEST = _operators.Operator_PETSC_MATNEST
    
    PETSC_MATHYPRE = _operators.Operator_PETSC_MATHYPRE
    
    PETSC_MATGENERIC = _operators.Operator_PETSC_MATGENERIC
    
    Complex_Operator = _operators.Operator_Complex_Operator
    
    MFEM_ComplexSparseMat = _operators.Operator_MFEM_ComplexSparseMat
    
    Complex_Hypre_ParCSR = _operators.Operator_Complex_Hypre_ParCSR
    

    def GetType(self):
        r"""GetType(Operator self) -> mfem::Operator::Type"""
        return _operators.Operator_GetType(self)
    GetType = _swig_new_instance_method(_operators.Operator_GetType)

    def PrintMatlab(self, *args):
        r"""
        PrintMatlab(Operator self, std::ostream & out, int n=0, int m=0)
        PrintMatlab(Operator self, char const * file, int precision=8)
        """
        return _operators.Operator_PrintMatlab(self, *args)
    PrintMatlab = _swig_new_instance_method(_operators.Operator_PrintMatlab)

    def PrintMatlabGZ(self, file, precision=8):
        r"""PrintMatlabGZ(Operator self, char const * file, int precision=8)"""
        return _operators.Operator_PrintMatlabGZ(self, file, precision)
    PrintMatlabGZ = _swig_new_instance_method(_operators.Operator_PrintMatlabGZ)
    def __disown__(self):
        self.this.disown()
        _operators.disown_Operator(self)
        return weakref.proxy(self)

# Register Operator in _operators:
_operators.Operator_swigregister(Operator)

class TimeDependentOperator(Operator):
    r"""Proxy of C++ mfem::TimeDependentOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    EXPLICIT = _operators.TimeDependentOperator_EXPLICIT
    
    IMPLICIT = _operators.TimeDependentOperator_IMPLICIT
    
    HOMOGENEOUS = _operators.TimeDependentOperator_HOMOGENEOUS
    
    NORMAL = _operators.TimeDependentOperator_NORMAL
    
    ADDITIVE_TERM_1 = _operators.TimeDependentOperator_ADDITIVE_TERM_1
    
    ADDITIVE_TERM_2 = _operators.TimeDependentOperator_ADDITIVE_TERM_2
    

    def __init__(self, *args):
        r"""
        __init__(TimeDependentOperator self, int n=0, double t_=0.0, mfem::TimeDependentOperator::Type type_=EXPLICIT) -> TimeDependentOperator
        __init__(TimeDependentOperator self, int h, int w, double t_=0.0, mfem::TimeDependentOperator::Type type_=EXPLICIT) -> TimeDependentOperator
        """
        if self.__class__ == TimeDependentOperator:
            _self = None
        else:
            _self = self
        _operators.TimeDependentOperator_swiginit(self, _operators.new_TimeDependentOperator(_self, *args))

    def GetTime(self):
        r"""GetTime(TimeDependentOperator self) -> double"""
        return _operators.TimeDependentOperator_GetTime(self)
    GetTime = _swig_new_instance_method(_operators.TimeDependentOperator_GetTime)

    def SetTime(self, t_):
        r"""SetTime(TimeDependentOperator self, double const t_)"""
        return _operators.TimeDependentOperator_SetTime(self, t_)
    SetTime = _swig_new_instance_method(_operators.TimeDependentOperator_SetTime)

    def isExplicit(self):
        r"""isExplicit(TimeDependentOperator self) -> bool"""
        return _operators.TimeDependentOperator_isExplicit(self)
    isExplicit = _swig_new_instance_method(_operators.TimeDependentOperator_isExplicit)

    def isImplicit(self):
        r"""isImplicit(TimeDependentOperator self) -> bool"""
        return _operators.TimeDependentOperator_isImplicit(self)
    isImplicit = _swig_new_instance_method(_operators.TimeDependentOperator_isImplicit)

    def isHomogeneous(self):
        r"""isHomogeneous(TimeDependentOperator self) -> bool"""
        return _operators.TimeDependentOperator_isHomogeneous(self)
    isHomogeneous = _swig_new_instance_method(_operators.TimeDependentOperator_isHomogeneous)

    def GetEvalMode(self):
        r"""GetEvalMode(TimeDependentOperator self) -> mfem::TimeDependentOperator::EvalMode"""
        return _operators.TimeDependentOperator_GetEvalMode(self)
    GetEvalMode = _swig_new_instance_method(_operators.TimeDependentOperator_GetEvalMode)

    def SetEvalMode(self, new_eval_mode):
        r"""SetEvalMode(TimeDependentOperator self, mfem::TimeDependentOperator::EvalMode const new_eval_mode)"""
        return _operators.TimeDependentOperator_SetEvalMode(self, new_eval_mode)
    SetEvalMode = _swig_new_instance_method(_operators.TimeDependentOperator_SetEvalMode)

    def ExplicitMult(self, x, y):
        r"""ExplicitMult(TimeDependentOperator self, Vector x, Vector y)"""
        return _operators.TimeDependentOperator_ExplicitMult(self, x, y)
    ExplicitMult = _swig_new_instance_method(_operators.TimeDependentOperator_ExplicitMult)

    def ImplicitMult(self, x, k, y):
        r"""ImplicitMult(TimeDependentOperator self, Vector x, Vector k, Vector y)"""
        return _operators.TimeDependentOperator_ImplicitMult(self, x, k, y)
    ImplicitMult = _swig_new_instance_method(_operators.TimeDependentOperator_ImplicitMult)

    def Mult(self, x, y):
        r"""Mult(TimeDependentOperator self, Vector x, Vector y)"""
        return _operators.TimeDependentOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.TimeDependentOperator_Mult)

    def ImplicitSolve(self, dt, x, k):
        r"""ImplicitSolve(TimeDependentOperator self, double const dt, Vector x, Vector k)"""
        return _operators.TimeDependentOperator_ImplicitSolve(self, dt, x, k)
    ImplicitSolve = _swig_new_instance_method(_operators.TimeDependentOperator_ImplicitSolve)

    def GetImplicitGradient(self, x, k, shift):
        r"""GetImplicitGradient(TimeDependentOperator self, Vector x, Vector k, double shift) -> Operator"""
        return _operators.TimeDependentOperator_GetImplicitGradient(self, x, k, shift)
    GetImplicitGradient = _swig_new_instance_method(_operators.TimeDependentOperator_GetImplicitGradient)

    def GetExplicitGradient(self, x):
        r"""GetExplicitGradient(TimeDependentOperator self, Vector x) -> Operator"""
        return _operators.TimeDependentOperator_GetExplicitGradient(self, x)
    GetExplicitGradient = _swig_new_instance_method(_operators.TimeDependentOperator_GetExplicitGradient)

    def SUNImplicitSetup(self, x, fx, jok, jcur, gamma):
        r"""SUNImplicitSetup(TimeDependentOperator self, Vector x, Vector fx, int jok, int * jcur, double gamma) -> int"""
        return _operators.TimeDependentOperator_SUNImplicitSetup(self, x, fx, jok, jcur, gamma)
    SUNImplicitSetup = _swig_new_instance_method(_operators.TimeDependentOperator_SUNImplicitSetup)

    def SUNImplicitSolve(self, b, x, tol):
        r"""SUNImplicitSolve(TimeDependentOperator self, Vector b, Vector x, double tol) -> int"""
        return _operators.TimeDependentOperator_SUNImplicitSolve(self, b, x, tol)
    SUNImplicitSolve = _swig_new_instance_method(_operators.TimeDependentOperator_SUNImplicitSolve)

    def SUNMassSetup(self):
        r"""SUNMassSetup(TimeDependentOperator self) -> int"""
        return _operators.TimeDependentOperator_SUNMassSetup(self)
    SUNMassSetup = _swig_new_instance_method(_operators.TimeDependentOperator_SUNMassSetup)

    def SUNMassSolve(self, b, x, tol):
        r"""SUNMassSolve(TimeDependentOperator self, Vector b, Vector x, double tol) -> int"""
        return _operators.TimeDependentOperator_SUNMassSolve(self, b, x, tol)
    SUNMassSolve = _swig_new_instance_method(_operators.TimeDependentOperator_SUNMassSolve)

    def SUNMassMult(self, x, v):
        r"""SUNMassMult(TimeDependentOperator self, Vector x, Vector v) -> int"""
        return _operators.TimeDependentOperator_SUNMassMult(self, x, v)
    SUNMassMult = _swig_new_instance_method(_operators.TimeDependentOperator_SUNMassMult)
    __swig_destroy__ = _operators.delete_TimeDependentOperator
    def __disown__(self):
        self.this.disown()
        _operators.disown_TimeDependentOperator(self)
        return weakref.proxy(self)

# Register TimeDependentOperator in _operators:
_operators.TimeDependentOperator_swigregister(TimeDependentOperator)

class TimeDependentAdjointOperator(TimeDependentOperator):
    r"""Proxy of C++ mfem::TimeDependentAdjointOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _operators.delete_TimeDependentAdjointOperator

    def QuadratureIntegration(self, y, qdot):
        r"""QuadratureIntegration(TimeDependentAdjointOperator self, Vector y, Vector qdot)"""
        return _operators.TimeDependentAdjointOperator_QuadratureIntegration(self, y, qdot)
    QuadratureIntegration = _swig_new_instance_method(_operators.TimeDependentAdjointOperator_QuadratureIntegration)

    def AdjointRateMult(self, y, yB, yBdot):
        r"""AdjointRateMult(TimeDependentAdjointOperator self, Vector y, Vector yB, Vector yBdot)"""
        return _operators.TimeDependentAdjointOperator_AdjointRateMult(self, y, yB, yBdot)
    AdjointRateMult = _swig_new_instance_method(_operators.TimeDependentAdjointOperator_AdjointRateMult)

    def QuadratureSensitivityMult(self, y, yB, qBdot):
        r"""QuadratureSensitivityMult(TimeDependentAdjointOperator self, Vector y, Vector yB, Vector qBdot)"""
        return _operators.TimeDependentAdjointOperator_QuadratureSensitivityMult(self, y, yB, qBdot)
    QuadratureSensitivityMult = _swig_new_instance_method(_operators.TimeDependentAdjointOperator_QuadratureSensitivityMult)

    def SUNImplicitSetupB(self, t, x, xB, fxB, jokB, jcurB, gammaB):
        r"""SUNImplicitSetupB(TimeDependentAdjointOperator self, double const t, Vector x, Vector xB, Vector fxB, int jokB, int * jcurB, double gammaB) -> int"""
        return _operators.TimeDependentAdjointOperator_SUNImplicitSetupB(self, t, x, xB, fxB, jokB, jcurB, gammaB)
    SUNImplicitSetupB = _swig_new_instance_method(_operators.TimeDependentAdjointOperator_SUNImplicitSetupB)

    def SUNImplicitSolveB(self, x, b, tol):
        r"""SUNImplicitSolveB(TimeDependentAdjointOperator self, Vector x, Vector b, double tol) -> int"""
        return _operators.TimeDependentAdjointOperator_SUNImplicitSolveB(self, x, b, tol)
    SUNImplicitSolveB = _swig_new_instance_method(_operators.TimeDependentAdjointOperator_SUNImplicitSolveB)

    def GetAdjointHeight(self):
        r"""GetAdjointHeight(TimeDependentAdjointOperator self) -> int"""
        return _operators.TimeDependentAdjointOperator_GetAdjointHeight(self)
    GetAdjointHeight = _swig_new_instance_method(_operators.TimeDependentAdjointOperator_GetAdjointHeight)

# Register TimeDependentAdjointOperator in _operators:
_operators.TimeDependentAdjointOperator_swigregister(TimeDependentAdjointOperator)

class SecondOrderTimeDependentOperator(TimeDependentOperator):
    r"""Proxy of C++ mfem::SecondOrderTimeDependentOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(SecondOrderTimeDependentOperator self, int n=0, double t_=0.0, mfem::TimeDependentOperator::Type type_=EXPLICIT) -> SecondOrderTimeDependentOperator
        __init__(SecondOrderTimeDependentOperator self, int h, int w, double t_=0.0, mfem::TimeDependentOperator::Type type_=EXPLICIT) -> SecondOrderTimeDependentOperator
        """
        _operators.SecondOrderTimeDependentOperator_swiginit(self, _operators.new_SecondOrderTimeDependentOperator(*args))

    def Mult(self, *args):
        r"""
        Mult(SecondOrderTimeDependentOperator self, Vector x, Vector y)
        Mult(SecondOrderTimeDependentOperator self, Vector x, Vector dxdt, Vector y)
        """
        return _operators.SecondOrderTimeDependentOperator_Mult(self, *args)
    Mult = _swig_new_instance_method(_operators.SecondOrderTimeDependentOperator_Mult)

    def ImplicitSolve(self, *args):
        r"""
        ImplicitSolve(SecondOrderTimeDependentOperator self, double const dt, Vector x, Vector k)
        ImplicitSolve(SecondOrderTimeDependentOperator self, double const fac0, double const fac1, Vector x, Vector dxdt, Vector k)
        """
        return _operators.SecondOrderTimeDependentOperator_ImplicitSolve(self, *args)
    ImplicitSolve = _swig_new_instance_method(_operators.SecondOrderTimeDependentOperator_ImplicitSolve)
    __swig_destroy__ = _operators.delete_SecondOrderTimeDependentOperator

# Register SecondOrderTimeDependentOperator in _operators:
_operators.SecondOrderTimeDependentOperator_swigregister(SecondOrderTimeDependentOperator)

class Solver(Operator):
    r"""Proxy of C++ mfem::Solver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterative_mode = property(_operators.Solver_iterative_mode_get, _operators.Solver_iterative_mode_set, doc=r"""iterative_mode : bool""")

    def __init__(self, *args):
        r"""
        __init__(Solver self, int s=0, bool iter_mode=False) -> Solver
        __init__(Solver self, int h, int w, bool iter_mode=False) -> Solver
        """
        if self.__class__ == Solver:
            _self = None
        else:
            _self = self
        _operators.Solver_swiginit(self, _operators.new_Solver(_self, *args))

    def SetOperator(self, op):
        r"""SetOperator(Solver self, Operator op)"""
        return _operators.Solver_SetOperator(self, op)
    SetOperator = _swig_new_instance_method(_operators.Solver_SetOperator)
    __swig_destroy__ = _operators.delete_Solver
    def __disown__(self):
        self.this.disown()
        _operators.disown_Solver(self)
        return weakref.proxy(self)

# Register Solver in _operators:
_operators.Solver_swigregister(Solver)

class IdentityOperator(Operator):
    r"""Proxy of C++ mfem::IdentityOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, n):
        r"""__init__(IdentityOperator self, int n) -> IdentityOperator"""
        _operators.IdentityOperator_swiginit(self, _operators.new_IdentityOperator(n))

    def Mult(self, x, y):
        r"""Mult(IdentityOperator self, Vector x, Vector y)"""
        return _operators.IdentityOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.IdentityOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(IdentityOperator self, Vector x, Vector y)"""
        return _operators.IdentityOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.IdentityOperator_MultTranspose)
    __swig_destroy__ = _operators.delete_IdentityOperator

# Register IdentityOperator in _operators:
_operators.IdentityOperator_swigregister(IdentityOperator)


def IsIdentityProlongation(P):
    r"""IsIdentityProlongation(Operator P) -> bool"""
    return _operators.IsIdentityProlongation(P)
IsIdentityProlongation = _operators.IsIdentityProlongation
class ScaledOperator(Operator):
    r"""Proxy of C++ mfem::ScaledOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, A, a):
        r"""__init__(ScaledOperator self, Operator A, double a) -> ScaledOperator"""
        _operators.ScaledOperator_swiginit(self, _operators.new_ScaledOperator(A, a))

    def Mult(self, x, y):
        r"""Mult(ScaledOperator self, Vector x, Vector y)"""
        return _operators.ScaledOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.ScaledOperator_Mult)
    __swig_destroy__ = _operators.delete_ScaledOperator

# Register ScaledOperator in _operators:
_operators.ScaledOperator_swigregister(ScaledOperator)

class TransposeOperator(Operator):
    r"""Proxy of C++ mfem::TransposeOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(TransposeOperator self, Operator a) -> TransposeOperator
        __init__(TransposeOperator self, Operator a) -> TransposeOperator
        """
        _operators.TransposeOperator_swiginit(self, _operators.new_TransposeOperator(*args))

    def Mult(self, x, y):
        r"""Mult(TransposeOperator self, Vector x, Vector y)"""
        return _operators.TransposeOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.TransposeOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(TransposeOperator self, Vector x, Vector y)"""
        return _operators.TransposeOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.TransposeOperator_MultTranspose)
    __swig_destroy__ = _operators.delete_TransposeOperator

# Register TransposeOperator in _operators:
_operators.TransposeOperator_swigregister(TransposeOperator)

class ProductOperator(Operator):
    r"""Proxy of C++ mfem::ProductOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, A, B, ownA, ownB):
        r"""__init__(ProductOperator self, Operator A, Operator B, bool ownA, bool ownB) -> ProductOperator"""
        _operators.ProductOperator_swiginit(self, _operators.new_ProductOperator(A, B, ownA, ownB))

    def Mult(self, x, y):
        r"""Mult(ProductOperator self, Vector x, Vector y)"""
        return _operators.ProductOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.ProductOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(ProductOperator self, Vector x, Vector y)"""
        return _operators.ProductOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.ProductOperator_MultTranspose)
    __swig_destroy__ = _operators.delete_ProductOperator

# Register ProductOperator in _operators:
_operators.ProductOperator_swigregister(ProductOperator)

class RAPOperator(Operator):
    r"""Proxy of C++ mfem::RAPOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, Rt_, A_, P_):
        r"""__init__(RAPOperator self, Operator Rt_, Operator A_, Operator P_) -> RAPOperator"""
        _operators.RAPOperator_swiginit(self, _operators.new_RAPOperator(Rt_, A_, P_))

    def GetMemoryClass(self):
        r"""GetMemoryClass(RAPOperator self) -> mfem::MemoryClass"""
        return _operators.RAPOperator_GetMemoryClass(self)
    GetMemoryClass = _swig_new_instance_method(_operators.RAPOperator_GetMemoryClass)

    def Mult(self, x, y):
        r"""Mult(RAPOperator self, Vector x, Vector y)"""
        return _operators.RAPOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.RAPOperator_Mult)

    def AssembleDiagonal(self, diag):
        r"""AssembleDiagonal(RAPOperator self, Vector diag)"""
        return _operators.RAPOperator_AssembleDiagonal(self, diag)
    AssembleDiagonal = _swig_new_instance_method(_operators.RAPOperator_AssembleDiagonal)

    def MultTranspose(self, x, y):
        r"""MultTranspose(RAPOperator self, Vector x, Vector y)"""
        return _operators.RAPOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.RAPOperator_MultTranspose)
    __swig_destroy__ = _operators.delete_RAPOperator

# Register RAPOperator in _operators:
_operators.RAPOperator_swigregister(RAPOperator)

class TripleProductOperator(Operator):
    r"""Proxy of C++ mfem::TripleProductOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, A, B, C, ownA, ownB, ownC):
        r"""__init__(TripleProductOperator self, Operator A, Operator B, Operator C, bool ownA, bool ownB, bool ownC) -> TripleProductOperator"""
        _operators.TripleProductOperator_swiginit(self, _operators.new_TripleProductOperator(A, B, C, ownA, ownB, ownC))

    def GetMemoryClass(self):
        r"""GetMemoryClass(TripleProductOperator self) -> mfem::MemoryClass"""
        return _operators.TripleProductOperator_GetMemoryClass(self)
    GetMemoryClass = _swig_new_instance_method(_operators.TripleProductOperator_GetMemoryClass)

    def Mult(self, x, y):
        r"""Mult(TripleProductOperator self, Vector x, Vector y)"""
        return _operators.TripleProductOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.TripleProductOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(TripleProductOperator self, Vector x, Vector y)"""
        return _operators.TripleProductOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.TripleProductOperator_MultTranspose)
    __swig_destroy__ = _operators.delete_TripleProductOperator

# Register TripleProductOperator in _operators:
_operators.TripleProductOperator_swigregister(TripleProductOperator)

class ConstrainedOperator(Operator):
    r"""Proxy of C++ mfem::ConstrainedOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(ConstrainedOperator self, Operator A, intArray list, bool own_A=False, mfem::Operator::DiagonalPolicy diag_policy=DIAG_ONE) -> ConstrainedOperator"""
        _operators.ConstrainedOperator_swiginit(self, _operators.new_ConstrainedOperator(*args, **kwargs))

    def GetMemoryClass(self):
        r"""GetMemoryClass(ConstrainedOperator self) -> mfem::MemoryClass"""
        return _operators.ConstrainedOperator_GetMemoryClass(self)
    GetMemoryClass = _swig_new_instance_method(_operators.ConstrainedOperator_GetMemoryClass)

    def SetDiagonalPolicy(self, diag_policy_):
        r"""SetDiagonalPolicy(ConstrainedOperator self, mfem::Operator::DiagonalPolicy const diag_policy_)"""
        return _operators.ConstrainedOperator_SetDiagonalPolicy(self, diag_policy_)
    SetDiagonalPolicy = _swig_new_instance_method(_operators.ConstrainedOperator_SetDiagonalPolicy)

    def AssembleDiagonal(self, diag):
        r"""AssembleDiagonal(ConstrainedOperator self, Vector diag)"""
        return _operators.ConstrainedOperator_AssembleDiagonal(self, diag)
    AssembleDiagonal = _swig_new_instance_method(_operators.ConstrainedOperator_AssembleDiagonal)

    def EliminateRHS(self, x, b):
        r"""EliminateRHS(ConstrainedOperator self, Vector x, Vector b)"""
        return _operators.ConstrainedOperator_EliminateRHS(self, x, b)
    EliminateRHS = _swig_new_instance_method(_operators.ConstrainedOperator_EliminateRHS)

    def Mult(self, x, y):
        r"""Mult(ConstrainedOperator self, Vector x, Vector y)"""
        return _operators.ConstrainedOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.ConstrainedOperator_Mult)
    __swig_destroy__ = _operators.delete_ConstrainedOperator

# Register ConstrainedOperator in _operators:
_operators.ConstrainedOperator_swigregister(ConstrainedOperator)

class RectangularConstrainedOperator(Operator):
    r"""Proxy of C++ mfem::RectangularConstrainedOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, A, trial_list, test_list, own_A=False):
        r"""__init__(RectangularConstrainedOperator self, Operator A, intArray trial_list, intArray test_list, bool own_A=False) -> RectangularConstrainedOperator"""
        _operators.RectangularConstrainedOperator_swiginit(self, _operators.new_RectangularConstrainedOperator(A, trial_list, test_list, own_A))

    def GetMemoryClass(self):
        r"""GetMemoryClass(RectangularConstrainedOperator self) -> mfem::MemoryClass"""
        return _operators.RectangularConstrainedOperator_GetMemoryClass(self)
    GetMemoryClass = _swig_new_instance_method(_operators.RectangularConstrainedOperator_GetMemoryClass)

    def EliminateRHS(self, x, b):
        r"""EliminateRHS(RectangularConstrainedOperator self, Vector x, Vector b)"""
        return _operators.RectangularConstrainedOperator_EliminateRHS(self, x, b)
    EliminateRHS = _swig_new_instance_method(_operators.RectangularConstrainedOperator_EliminateRHS)

    def Mult(self, x, y):
        r"""Mult(RectangularConstrainedOperator self, Vector x, Vector y)"""
        return _operators.RectangularConstrainedOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.RectangularConstrainedOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(RectangularConstrainedOperator self, Vector x, Vector y)"""
        return _operators.RectangularConstrainedOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_operators.RectangularConstrainedOperator_MultTranspose)
    __swig_destroy__ = _operators.delete_RectangularConstrainedOperator

# Register RectangularConstrainedOperator in _operators:
_operators.RectangularConstrainedOperator_swigregister(RectangularConstrainedOperator)

class PowerMethod(object):
    r"""Proxy of C++ mfem::PowerMethod class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(PowerMethod self) -> PowerMethod"""
        _operators.PowerMethod_swiginit(self, _operators.new_PowerMethod())

    def EstimateLargestEigenvalue(self, opr, v0, numSteps=10, tolerance=1e-8, seed=12345):
        r"""EstimateLargestEigenvalue(PowerMethod self, Operator opr, Vector v0, int numSteps=10, double tolerance=1e-8, int seed=12345) -> double"""
        return _operators.PowerMethod_EstimateLargestEigenvalue(self, opr, v0, numSteps, tolerance, seed)
    EstimateLargestEigenvalue = _swig_new_instance_method(_operators.PowerMethod_EstimateLargestEigenvalue)
    __swig_destroy__ = _operators.delete_PowerMethod

# Register PowerMethod in _operators:
_operators.PowerMethod_swigregister(PowerMethod)

class PyOperatorBase(Operator):
    r"""Proxy of C++ mfem::PyOperatorBase class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(PyOperatorBase self, int s=0) -> PyOperatorBase
        __init__(PyOperatorBase self, int h, int w) -> PyOperatorBase
        """
        if self.__class__ == PyOperatorBase:
            _self = None
        else:
            _self = self
        _operators.PyOperatorBase_swiginit(self, _operators.new_PyOperatorBase(_self, *args))

    def Mult(self, x, y):
        r"""Mult(PyOperatorBase self, Vector x, Vector y)"""
        return _operators.PyOperatorBase_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.PyOperatorBase_Mult)

    def _EvalMult(self, arg0):
        r"""_EvalMult(PyOperatorBase self, Vector arg0) -> Vector"""
        return _operators.PyOperatorBase__EvalMult(self, arg0)
    _EvalMult = _swig_new_instance_method(_operators.PyOperatorBase__EvalMult)
    __swig_destroy__ = _operators.delete_PyOperatorBase
    def __disown__(self):
        self.this.disown()
        _operators.disown_PyOperatorBase(self)
        return weakref.proxy(self)

# Register PyOperatorBase in _operators:
_operators.PyOperatorBase_swigregister(PyOperatorBase)

class PyTimeDependentOperatorBase(TimeDependentOperator):
    r"""Proxy of C++ mfem::PyTimeDependentOperatorBase class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(PyTimeDependentOperatorBase self, int n=0, double _t=0.0) -> PyTimeDependentOperatorBase
        __init__(PyTimeDependentOperatorBase self, int h, int w, double _t=0.0) -> PyTimeDependentOperatorBase
        """
        if self.__class__ == PyTimeDependentOperatorBase:
            _self = None
        else:
            _self = self
        _operators.PyTimeDependentOperatorBase_swiginit(self, _operators.new_PyTimeDependentOperatorBase(_self, *args))

    def Mult(self, x, y):
        r"""Mult(PyTimeDependentOperatorBase self, Vector x, Vector y)"""
        return _operators.PyTimeDependentOperatorBase_Mult(self, x, y)
    Mult = _swig_new_instance_method(_operators.PyTimeDependentOperatorBase_Mult)

    def _EvalMult(self, arg0):
        r"""_EvalMult(PyTimeDependentOperatorBase self, Vector arg0) -> Vector"""
        return _operators.PyTimeDependentOperatorBase__EvalMult(self, arg0)
    _EvalMult = _swig_new_instance_method(_operators.PyTimeDependentOperatorBase__EvalMult)
    __swig_destroy__ = _operators.delete_PyTimeDependentOperatorBase
    def __disown__(self):
        self.this.disown()
        _operators.disown_PyTimeDependentOperatorBase(self)
        return weakref.proxy(self)

# Register PyTimeDependentOperatorBase in _operators:
_operators.PyTimeDependentOperatorBase_swigregister(PyTimeDependentOperatorBase)


class PyOperator(PyOperatorBase):
   def __init__(self, *args):
       PyOperatorBase.__init__(self, *args)
   def _EvalMult(self, x):
       return self.EvalMult(x.GetDataArray())
   def EvalMult(self, x):
       raise NotImplementedError('you must specify this method')

class PyTimeDependentOperator(PyTimeDependentOperatorBase):
   def __init__(self, *args):  
       PyTimeDependentOperatorBase.__init__(self, *args)
   def _EvalMult(self, x):
       return self.EvalMult(x.GetDataArray())
   def EvalMult(self, x):
       raise NotImplementedError('you must specify this method')




