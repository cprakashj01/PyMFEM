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
    from . import _pbilinearform
else:
    import _pbilinearform

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _pbilinearform.SWIG_PyInstanceMethod_New
_swig_new_static_method = _pbilinearform.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _pbilinearform.MFEM_VERSION
MFEM_VERSION_STRING = _pbilinearform.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pbilinearform.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pbilinearform.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pbilinearform.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pbilinearform.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pbilinearform.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pbilinearform.MFEM_VERSION_PATCH
import mfem._par.handle
import mfem._par.operators
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
import mfem._par.hypre
import mfem._par.globals
import mfem._par.sparsemat
import mfem._par.matrix
import mfem._par.densemat
import mfem._par.bilinearform
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.symmat
import mfem._par.intrules
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.doftrans
import mfem._par.restriction
import mfem._par.pfespace
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class ParBilinearForm(mfem._par.bilinearform.BilinearForm):
    r"""Proxy of C++ mfem::ParBilinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ParBilinearForm self, ParFiniteElementSpace pf) -> ParBilinearForm
        __init__(ParBilinearForm self, ParFiniteElementSpace pf, ParBilinearForm bf) -> ParBilinearForm
        """
        _pbilinearform.ParBilinearForm_swiginit(self, _pbilinearform.new_ParBilinearForm(*args))

    def KeepNbrBlock(self, knb=True):
        r"""KeepNbrBlock(ParBilinearForm self, bool knb=True)"""
        return _pbilinearform.ParBilinearForm_KeepNbrBlock(self, knb)
    KeepNbrBlock = _swig_new_instance_method(_pbilinearform.ParBilinearForm_KeepNbrBlock)

    def SetOperatorType(self, tid):
        r"""SetOperatorType(ParBilinearForm self, mfem::Operator::Type tid)"""
        return _pbilinearform.ParBilinearForm_SetOperatorType(self, tid)
    SetOperatorType = _swig_new_instance_method(_pbilinearform.ParBilinearForm_SetOperatorType)

    def Assemble(self, skip_zeros=1):
        r"""Assemble(ParBilinearForm self, int skip_zeros=1)"""
        return _pbilinearform.ParBilinearForm_Assemble(self, skip_zeros)
    Assemble = _swig_new_instance_method(_pbilinearform.ParBilinearForm_Assemble)

    def AssembleDiagonal(self, diag):
        r"""AssembleDiagonal(ParBilinearForm self, Vector diag)"""
        return _pbilinearform.ParBilinearForm_AssembleDiagonal(self, diag)
    AssembleDiagonal = _swig_new_instance_method(_pbilinearform.ParBilinearForm_AssembleDiagonal)

    def ParallelAssembleElim(self, *args):
        r"""
        ParallelAssembleElim(ParBilinearForm self) -> HypreParMatrix
        ParallelAssembleElim(ParBilinearForm self, OperatorHandle A_elim)
        """
        return _pbilinearform.ParBilinearForm_ParallelAssembleElim(self, *args)
    ParallelAssembleElim = _swig_new_instance_method(_pbilinearform.ParBilinearForm_ParallelAssembleElim)

    def ParallelAssemble(self, *args):
        r"""
        ParallelAssemble(ParBilinearForm self) -> HypreParMatrix
        ParallelAssemble(ParBilinearForm self, SparseMatrix m) -> HypreParMatrix
        ParallelAssemble(ParBilinearForm self, OperatorHandle A)
        ParallelAssemble(ParBilinearForm self, OperatorHandle A, SparseMatrix A_local)
        """
        return _pbilinearform.ParBilinearForm_ParallelAssemble(self, *args)
    ParallelAssemble = _swig_new_instance_method(_pbilinearform.ParBilinearForm_ParallelAssemble)

    def ParallelEliminateEssentialBC(self, *args):
        r"""
        ParallelEliminateEssentialBC(ParBilinearForm self, intArray bdr_attr_is_ess, HypreParMatrix A, HypreParVector X, HypreParVector B)
        ParallelEliminateEssentialBC(ParBilinearForm self, intArray bdr_attr_is_ess, HypreParMatrix A) -> HypreParMatrix
        """
        return _pbilinearform.ParBilinearForm_ParallelEliminateEssentialBC(self, *args)
    ParallelEliminateEssentialBC = _swig_new_instance_method(_pbilinearform.ParBilinearForm_ParallelEliminateEssentialBC)

    def ParallelEliminateTDofs(self, tdofs_list, A):
        r"""ParallelEliminateTDofs(ParBilinearForm self, intArray tdofs_list, HypreParMatrix A) -> HypreParMatrix"""
        return _pbilinearform.ParBilinearForm_ParallelEliminateTDofs(self, tdofs_list, A)
    ParallelEliminateTDofs = _swig_new_instance_method(_pbilinearform.ParBilinearForm_ParallelEliminateTDofs)

    def TrueAddMult(self, x, y, a=1.0):
        r"""TrueAddMult(ParBilinearForm self, Vector x, Vector y, double const a=1.0)"""
        return _pbilinearform.ParBilinearForm_TrueAddMult(self, x, y, a)
    TrueAddMult = _swig_new_instance_method(_pbilinearform.ParBilinearForm_TrueAddMult)

    def ParFESpace(self):
        r"""ParFESpace(ParBilinearForm self) -> ParFiniteElementSpace"""
        return _pbilinearform.ParBilinearForm_ParFESpace(self)
    ParFESpace = _swig_new_instance_method(_pbilinearform.ParBilinearForm_ParFESpace)

    def SCParFESpace(self):
        r"""SCParFESpace(ParBilinearForm self) -> ParFiniteElementSpace"""
        return _pbilinearform.ParBilinearForm_SCParFESpace(self)
    SCParFESpace = _swig_new_instance_method(_pbilinearform.ParBilinearForm_SCParFESpace)

    def GetProlongation(self):
        r"""GetProlongation(ParBilinearForm self) -> Operator"""
        return _pbilinearform.ParBilinearForm_GetProlongation(self)
    GetProlongation = _swig_new_instance_method(_pbilinearform.ParBilinearForm_GetProlongation)

    def GetRestrictionTranspose(self):
        r"""GetRestrictionTranspose(ParBilinearForm self) -> Operator"""
        return _pbilinearform.ParBilinearForm_GetRestrictionTranspose(self)
    GetRestrictionTranspose = _swig_new_instance_method(_pbilinearform.ParBilinearForm_GetRestrictionTranspose)

    def GetRestriction(self):
        r"""GetRestriction(ParBilinearForm self) -> Operator"""
        return _pbilinearform.ParBilinearForm_GetRestriction(self)
    GetRestriction = _swig_new_instance_method(_pbilinearform.ParBilinearForm_GetRestriction)

    def RecoverFEMSolution(self, X, b, x):
        r"""RecoverFEMSolution(ParBilinearForm self, Vector X, Vector b, Vector x)"""
        return _pbilinearform.ParBilinearForm_RecoverFEMSolution(self, X, b, x)
    RecoverFEMSolution = _swig_new_instance_method(_pbilinearform.ParBilinearForm_RecoverFEMSolution)

    def Update(self, nfes=None):
        r"""Update(ParBilinearForm self, FiniteElementSpace nfes=None)"""
        return _pbilinearform.ParBilinearForm_Update(self, nfes)
    Update = _swig_new_instance_method(_pbilinearform.ParBilinearForm_Update)

    def EliminateVDofsInRHS(self, vdofs, x, b):
        r"""EliminateVDofsInRHS(ParBilinearForm self, intArray vdofs, Vector x, Vector b)"""
        return _pbilinearform.ParBilinearForm_EliminateVDofsInRHS(self, vdofs, x, b)
    EliminateVDofsInRHS = _swig_new_instance_method(_pbilinearform.ParBilinearForm_EliminateVDofsInRHS)
    __swig_destroy__ = _pbilinearform.delete_ParBilinearForm

    def FormLinearSystem(self, *args):
        r"""
        FormLinearSystem(ParBilinearForm self)
        FormLinearSystem(ParBilinearForm self, intArray ess_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B, int copy_interior=0)
        FormLinearSystem(ParBilinearForm self, intArray ess_tdof_list, Vector x, Vector b, SparseMatrix A, Vector X, Vector B, int copy_interior=0)
        FormLinearSystem(ParBilinearForm self, intArray ess_tdof_list, Vector x, Vector b, HypreParMatrix A, Vector X, Vector B, int copy_interior=0)
        """
        return _pbilinearform.ParBilinearForm_FormLinearSystem(self, *args)
    FormLinearSystem = _swig_new_instance_method(_pbilinearform.ParBilinearForm_FormLinearSystem)

    def FormSystemMatrix(self, *args):
        r"""
        FormSystemMatrix(ParBilinearForm self)
        FormSystemMatrix(ParBilinearForm self, intArray ess_tdof_list, OperatorHandle A)
        FormSystemMatrix(ParBilinearForm self, intArray ess_tdof_list, SparseMatrix A)
        FormSystemMatrix(ParBilinearForm self, intArray ess_tdof_list, HypreParMatrix A)
        """
        return _pbilinearform.ParBilinearForm_FormSystemMatrix(self, *args)
    FormSystemMatrix = _swig_new_instance_method(_pbilinearform.ParBilinearForm_FormSystemMatrix)

# Register ParBilinearForm in _pbilinearform:
_pbilinearform.ParBilinearForm_swigregister(ParBilinearForm)

class ParMixedBilinearForm(mfem._par.bilinearform.MixedBilinearForm):
    r"""Proxy of C++ mfem::ParMixedBilinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ParMixedBilinearForm self, ParFiniteElementSpace trial_fes, ParFiniteElementSpace test_fes) -> ParMixedBilinearForm
        __init__(ParMixedBilinearForm self, ParFiniteElementSpace trial_fes, ParFiniteElementSpace test_fes, ParMixedBilinearForm mbf) -> ParMixedBilinearForm
        """
        _pbilinearform.ParMixedBilinearForm_swiginit(self, _pbilinearform.new_ParMixedBilinearForm(*args))

    def ParallelAssemble(self, *args):
        r"""
        ParallelAssemble(ParMixedBilinearForm self) -> HypreParMatrix
        ParallelAssemble(ParMixedBilinearForm self, OperatorHandle A)
        """
        return _pbilinearform.ParMixedBilinearForm_ParallelAssemble(self, *args)
    ParallelAssemble = _swig_new_instance_method(_pbilinearform.ParMixedBilinearForm_ParallelAssemble)

    def FormRectangularSystemMatrix(self, *args):
        r"""
        FormRectangularSystemMatrix(ParMixedBilinearForm self)
        FormRectangularSystemMatrix(ParMixedBilinearForm self, intArray trial_tdof_list, intArray test_tdof_list, OperatorHandle A)
        """
        return _pbilinearform.ParMixedBilinearForm_FormRectangularSystemMatrix(self, *args)
    FormRectangularSystemMatrix = _swig_new_instance_method(_pbilinearform.ParMixedBilinearForm_FormRectangularSystemMatrix)

    def FormRectangularLinearSystem(self, *args):
        r"""
        FormRectangularLinearSystem(ParMixedBilinearForm self)
        FormRectangularLinearSystem(ParMixedBilinearForm self, intArray trial_tdof_list, intArray test_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B)
        """
        return _pbilinearform.ParMixedBilinearForm_FormRectangularLinearSystem(self, *args)
    FormRectangularLinearSystem = _swig_new_instance_method(_pbilinearform.ParMixedBilinearForm_FormRectangularLinearSystem)

    def TrueAddMult(self, x, y, a=1.0):
        r"""TrueAddMult(ParMixedBilinearForm self, Vector x, Vector y, double const a=1.0)"""
        return _pbilinearform.ParMixedBilinearForm_TrueAddMult(self, x, y, a)
    TrueAddMult = _swig_new_instance_method(_pbilinearform.ParMixedBilinearForm_TrueAddMult)
    __swig_destroy__ = _pbilinearform.delete_ParMixedBilinearForm

# Register ParMixedBilinearForm in _pbilinearform:
_pbilinearform.ParMixedBilinearForm_swigregister(ParMixedBilinearForm)

class ParDiscreteLinearOperator(mfem._par.bilinearform.DiscreteLinearOperator):
    r"""Proxy of C++ mfem::ParDiscreteLinearOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, dfes, rfes):
        r"""__init__(ParDiscreteLinearOperator self, ParFiniteElementSpace dfes, ParFiniteElementSpace rfes) -> ParDiscreteLinearOperator"""
        _pbilinearform.ParDiscreteLinearOperator_swiginit(self, _pbilinearform.new_ParDiscreteLinearOperator(dfes, rfes))

    def ParallelAssemble(self, *args):
        r"""
        ParallelAssemble(ParDiscreteLinearOperator self) -> HypreParMatrix
        ParallelAssemble(ParDiscreteLinearOperator self, OperatorHandle A)
        """
        return _pbilinearform.ParDiscreteLinearOperator_ParallelAssemble(self, *args)
    ParallelAssemble = _swig_new_instance_method(_pbilinearform.ParDiscreteLinearOperator_ParallelAssemble)

    def GetParBlocks(self, blocks):
        r"""GetParBlocks(ParDiscreteLinearOperator self, mfem::Array2D< mfem::HypreParMatrix * > & blocks)"""
        return _pbilinearform.ParDiscreteLinearOperator_GetParBlocks(self, blocks)
    GetParBlocks = _swig_new_instance_method(_pbilinearform.ParDiscreteLinearOperator_GetParBlocks)

    def FormRectangularSystemMatrix(self, *args):
        r"""
        FormRectangularSystemMatrix(ParDiscreteLinearOperator self)
        FormRectangularSystemMatrix(ParDiscreteLinearOperator self, OperatorHandle A)
        """
        return _pbilinearform.ParDiscreteLinearOperator_FormRectangularSystemMatrix(self, *args)
    FormRectangularSystemMatrix = _swig_new_instance_method(_pbilinearform.ParDiscreteLinearOperator_FormRectangularSystemMatrix)
    __swig_destroy__ = _pbilinearform.delete_ParDiscreteLinearOperator

# Register ParDiscreteLinearOperator in _pbilinearform:
_pbilinearform.ParDiscreteLinearOperator_swigregister(ParDiscreteLinearOperator)



