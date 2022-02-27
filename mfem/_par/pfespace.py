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
    from . import _pfespace
else:
    import _pfespace

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _pfespace.SWIG_PyInstanceMethod_New
_swig_new_static_method = _pfespace.SWIG_PyStaticMethod_New

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

MFEM_VERSION = _pfespace.MFEM_VERSION
MFEM_VERSION_STRING = _pfespace.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pfespace.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pfespace.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pfespace.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pfespace.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pfespace.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pfespace.MFEM_VERSION_PATCH
import mfem._par.operators
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.globals
import mfem._par.matrix
import mfem._par.symmat
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
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
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class ParFiniteElementSpace(mfem._par.fespace.FiniteElementSpace):
    r"""Proxy of C++ mfem::ParFiniteElementSpace class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    num_face_nbr_dofs = property(_pfespace.ParFiniteElementSpace_num_face_nbr_dofs_get, _pfespace.ParFiniteElementSpace_num_face_nbr_dofs_set, doc=r"""num_face_nbr_dofs : int""")
    face_nbr_element_dof = property(_pfespace.ParFiniteElementSpace_face_nbr_element_dof_get, _pfespace.ParFiniteElementSpace_face_nbr_element_dof_set, doc=r"""face_nbr_element_dof : mfem::Table""")
    face_nbr_element_fos = property(_pfespace.ParFiniteElementSpace_face_nbr_element_fos_get, _pfespace.ParFiniteElementSpace_face_nbr_element_fos_set, doc=r"""face_nbr_element_fos : mfem::Table""")
    face_nbr_ldof = property(_pfespace.ParFiniteElementSpace_face_nbr_ldof_get, _pfespace.ParFiniteElementSpace_face_nbr_ldof_set, doc=r"""face_nbr_ldof : mfem::Table""")
    face_nbr_glob_dof_map = property(_pfespace.ParFiniteElementSpace_face_nbr_glob_dof_map_get, doc=r"""face_nbr_glob_dof_map : mfem::Array<(HYPRE_BigInt)>""")
    send_face_nbr_ldof = property(_pfespace.ParFiniteElementSpace_send_face_nbr_ldof_get, _pfespace.ParFiniteElementSpace_send_face_nbr_ldof_set, doc=r"""send_face_nbr_ldof : mfem::Table""")

    def __init__(self, *args):
        r"""
        __init__(ParFiniteElementSpace self, ParFiniteElementSpace orig, ParMesh pmesh=None, FiniteElementCollection fec=None) -> ParFiniteElementSpace
        __init__(ParFiniteElementSpace self, FiniteElementSpace orig, ParMesh pmesh, FiniteElementCollection fec=None) -> ParFiniteElementSpace
        __init__(ParFiniteElementSpace self, ParMesh pm, FiniteElementSpace global_fes, int const * partitioning, FiniteElementCollection f=None) -> ParFiniteElementSpace
        __init__(ParFiniteElementSpace self, ParMesh pm, FiniteElementCollection f, int dim=1, int ordering=byNODES) -> ParFiniteElementSpace
        __init__(ParFiniteElementSpace self, ParMesh pm, mfem::NURBSExtension * ext, FiniteElementCollection f, int dim=1, int ordering=byNODES) -> ParFiniteElementSpace
        """
        _pfespace.ParFiniteElementSpace_swiginit(self, _pfespace.new_ParFiniteElementSpace(*args))

    def GetComm(self):
        r"""GetComm(ParFiniteElementSpace self) -> MPI_Comm"""
        return _pfespace.ParFiniteElementSpace_GetComm(self)
    GetComm = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetComm)

    def GetNRanks(self):
        r"""GetNRanks(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetNRanks(self)
    GetNRanks = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetNRanks)

    def GetMyRank(self):
        r"""GetMyRank(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetMyRank(self)
    GetMyRank = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetMyRank)

    def GetParMesh(self):
        r"""GetParMesh(ParFiniteElementSpace self) -> ParMesh"""
        return _pfespace.ParFiniteElementSpace_GetParMesh(self)
    GetParMesh = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetParMesh)

    def GetDofSign(self, i):
        r"""GetDofSign(ParFiniteElementSpace self, int i) -> int"""
        return _pfespace.ParFiniteElementSpace_GetDofSign(self, i)
    GetDofSign = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetDofSign)

    def GetDofOffsets(self):
        r"""GetDofOffsets(ParFiniteElementSpace self) -> HYPRE_BigInt *"""
        return _pfespace.ParFiniteElementSpace_GetDofOffsets(self)
    GetDofOffsets = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetDofOffsets)

    def GetTrueDofOffsets(self):
        r"""GetTrueDofOffsets(ParFiniteElementSpace self) -> HYPRE_BigInt *"""
        return _pfespace.ParFiniteElementSpace_GetTrueDofOffsets(self)
    GetTrueDofOffsets = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetTrueDofOffsets)

    def GlobalVSize(self):
        r"""GlobalVSize(ParFiniteElementSpace self) -> HYPRE_BigInt"""
        return _pfespace.ParFiniteElementSpace_GlobalVSize(self)
    GlobalVSize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GlobalVSize)

    def GlobalTrueVSize(self):
        r"""GlobalTrueVSize(ParFiniteElementSpace self) -> HYPRE_BigInt"""
        return _pfespace.ParFiniteElementSpace_GlobalTrueVSize(self)
    GlobalTrueVSize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GlobalTrueVSize)

    def GetTrueVSize(self):
        r"""GetTrueVSize(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetTrueVSize(self)
    GetTrueVSize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetTrueVSize)

    def GetElementDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetElementDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetBdrElementDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetBdrElementDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFaceDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetFaceDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFE(self, i):
        r"""GetFE(ParFiniteElementSpace self, int i) -> FiniteElement"""
        return _pfespace.ParFiniteElementSpace_GetFE(self, i)
    GetFE = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFE)

    def GetFaceRestriction(self, *args, **kwargs):
        r"""GetFaceRestriction(ParFiniteElementSpace self, mfem::ElementDofOrdering e_ordering, mfem::FaceType type, mfem::L2FaceValues mul=DoubleValued) -> FaceRestriction"""
        return _pfespace.ParFiniteElementSpace_GetFaceRestriction(self, *args, **kwargs)
    GetFaceRestriction = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceRestriction)

    def GetSharedEdgeDofs(self, group, ei):
        from  .array import intArray
        dofs = intArray() 
        _pfespace.ParFiniteElementSpace_GetSharedEdgeDofs(self, group, ei, dofs)
        return dofs.ToList()



    def GetSharedTriangleDofs(self, group, fi):
        from  .array import intArray
        dofs = intArray()
        _pfespace.ParFiniteElementSpace_GetSharedTriangleDofs(self, group, fi, dofs)
        return dofs.ToList()



    def GetSharedQuadrilateralDofs(self, group, fi):
        from  .array import intArray
        dofs = intArray()
        _pfespace.ParFiniteElementSpace_GetSharedQuadrilateralDofs(self, group, fi, dofs)
        return dofs.ToList()



    def Dof_TrueDof_Matrix(self):
        r"""Dof_TrueDof_Matrix(ParFiniteElementSpace self) -> HypreParMatrix"""
        return _pfespace.ParFiniteElementSpace_Dof_TrueDof_Matrix(self)
    Dof_TrueDof_Matrix = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_Dof_TrueDof_Matrix)

    def GetPartialConformingInterpolation(self):
        r"""GetPartialConformingInterpolation(ParFiniteElementSpace self) -> HypreParMatrix"""
        return _pfespace.ParFiniteElementSpace_GetPartialConformingInterpolation(self)
    GetPartialConformingInterpolation = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetPartialConformingInterpolation)

    def NewTrueDofVector(self):
        r"""NewTrueDofVector(ParFiniteElementSpace self) -> HypreParVector"""
        return _pfespace.ParFiniteElementSpace_NewTrueDofVector(self)
    NewTrueDofVector = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_NewTrueDofVector)

    def DivideByGroupSize(self, vec):
        r"""DivideByGroupSize(ParFiniteElementSpace self, double * vec)"""
        return _pfespace.ParFiniteElementSpace_DivideByGroupSize(self, vec)
    DivideByGroupSize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_DivideByGroupSize)

    def GroupComm(self, *args):
        r"""
        GroupComm(ParFiniteElementSpace self) -> GroupCommunicator
        GroupComm(ParFiniteElementSpace self) -> GroupCommunicator
        """
        return _pfespace.ParFiniteElementSpace_GroupComm(self, *args)
    GroupComm = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GroupComm)

    def ScalarGroupComm(self):
        r"""ScalarGroupComm(ParFiniteElementSpace self) -> GroupCommunicator"""
        return _pfespace.ParFiniteElementSpace_ScalarGroupComm(self)
    ScalarGroupComm = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_ScalarGroupComm)

    def Synchronize(self, ldof_marker):
        r"""Synchronize(ParFiniteElementSpace self, intArray ldof_marker)"""
        return _pfespace.ParFiniteElementSpace_Synchronize(self, ldof_marker)
    Synchronize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_Synchronize)

    def GetEssentialVDofs(self, bdr_attr_is_ess, ess_dofs, component=-1):
        r"""GetEssentialVDofs(ParFiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_dofs, int component=-1)"""
        return _pfespace.ParFiniteElementSpace_GetEssentialVDofs(self, bdr_attr_is_ess, ess_dofs, component)
    GetEssentialVDofs = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetEssentialVDofs)

    def GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component=-1):
        r"""GetEssentialTrueDofs(ParFiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_tdof_list, int component=-1)"""
        return _pfespace.ParFiniteElementSpace_GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component)
    GetEssentialTrueDofs = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetEssentialTrueDofs)

    def GetLocalTDofNumber(self, ldof):
        r"""GetLocalTDofNumber(ParFiniteElementSpace self, int ldof) -> int"""
        return _pfespace.ParFiniteElementSpace_GetLocalTDofNumber(self, ldof)
    GetLocalTDofNumber = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetLocalTDofNumber)

    def GetGlobalTDofNumber(self, ldof):
        r"""GetGlobalTDofNumber(ParFiniteElementSpace self, int ldof) -> HYPRE_BigInt"""
        return _pfespace.ParFiniteElementSpace_GetGlobalTDofNumber(self, ldof)
    GetGlobalTDofNumber = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetGlobalTDofNumber)

    def GetGlobalScalarTDofNumber(self, sldof):
        r"""GetGlobalScalarTDofNumber(ParFiniteElementSpace self, int sldof) -> HYPRE_BigInt"""
        return _pfespace.ParFiniteElementSpace_GetGlobalScalarTDofNumber(self, sldof)
    GetGlobalScalarTDofNumber = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetGlobalScalarTDofNumber)

    def GetMyDofOffset(self):
        r"""GetMyDofOffset(ParFiniteElementSpace self) -> HYPRE_BigInt"""
        return _pfespace.ParFiniteElementSpace_GetMyDofOffset(self)
    GetMyDofOffset = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetMyDofOffset)

    def GetMyTDofOffset(self):
        r"""GetMyTDofOffset(ParFiniteElementSpace self) -> HYPRE_BigInt"""
        return _pfespace.ParFiniteElementSpace_GetMyTDofOffset(self)
    GetMyTDofOffset = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetMyTDofOffset)

    def GetProlongationMatrix(self):
        r"""GetProlongationMatrix(ParFiniteElementSpace self) -> Operator"""
        return _pfespace.ParFiniteElementSpace_GetProlongationMatrix(self)
    GetProlongationMatrix = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetProlongationMatrix)

    def GetRestrictionTransposeOperator(self):
        r"""GetRestrictionTransposeOperator(ParFiniteElementSpace self) -> Operator"""
        return _pfespace.ParFiniteElementSpace_GetRestrictionTransposeOperator(self)
    GetRestrictionTransposeOperator = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetRestrictionTransposeOperator)

    def GetRestrictionOperator(self):
        r"""GetRestrictionOperator(ParFiniteElementSpace self) -> Operator"""
        return _pfespace.ParFiniteElementSpace_GetRestrictionOperator(self)
    GetRestrictionOperator = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetRestrictionOperator)

    def GetRestrictionMatrix(self):
        r"""GetRestrictionMatrix(ParFiniteElementSpace self) -> SparseMatrix"""
        return _pfespace.ParFiniteElementSpace_GetRestrictionMatrix(self)
    GetRestrictionMatrix = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetRestrictionMatrix)

    def ExchangeFaceNbrData(self):
        r"""ExchangeFaceNbrData(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_ExchangeFaceNbrData(self)
    ExchangeFaceNbrData = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_ExchangeFaceNbrData)

    def GetFaceNbrVSize(self):
        r"""GetFaceNbrVSize(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrVSize(self)
    GetFaceNbrVSize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrVSize)

    def GetFaceNbrElementVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetFaceNbrElementVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFaceNbrFaceVDofs(self, i, vdofs):
        r"""GetFaceNbrFaceVDofs(ParFiniteElementSpace self, int i, intArray vdofs)"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrFaceVDofs(self, i, vdofs)
    GetFaceNbrFaceVDofs = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrFaceVDofs)

    def GetFaceNbrFE(self, i):
        r"""GetFaceNbrFE(ParFiniteElementSpace self, int i) -> FiniteElement"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrFE(self, i)
    GetFaceNbrFE = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrFE)

    def GetFaceNbrFaceFE(self, i):
        r"""GetFaceNbrFaceFE(ParFiniteElementSpace self, int i) -> FiniteElement"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrFaceFE(self, i)
    GetFaceNbrFaceFE = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrFaceFE)

    def GetFaceNbrGlobalDofMap(self):
        r"""GetFaceNbrGlobalDofMap(ParFiniteElementSpace self) -> HYPRE_BigInt const *"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrGlobalDofMap(self)
    GetFaceNbrGlobalDofMap = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrGlobalDofMap)

    def GetFaceNbrElementTransformation(self, i):
        r"""GetFaceNbrElementTransformation(ParFiniteElementSpace self, int i) -> ElementTransformation"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrElementTransformation(self, i)
    GetFaceNbrElementTransformation = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrElementTransformation)

    def Lose_Dof_TrueDof_Matrix(self):
        r"""Lose_Dof_TrueDof_Matrix(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_Lose_Dof_TrueDof_Matrix(self)
    Lose_Dof_TrueDof_Matrix = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_Lose_Dof_TrueDof_Matrix)

    def LoseDofOffsets(self):
        r"""LoseDofOffsets(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_LoseDofOffsets(self)
    LoseDofOffsets = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_LoseDofOffsets)

    def LoseTrueDofOffsets(self):
        r"""LoseTrueDofOffsets(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_LoseTrueDofOffsets(self)
    LoseTrueDofOffsets = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_LoseTrueDofOffsets)

    def Conforming(self):
        r"""Conforming(ParFiniteElementSpace self) -> bool"""
        return _pfespace.ParFiniteElementSpace_Conforming(self)
    Conforming = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_Conforming)

    def Nonconforming(self):
        r"""Nonconforming(ParFiniteElementSpace self) -> bool"""
        return _pfespace.ParFiniteElementSpace_Nonconforming(self)
    Nonconforming = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_Nonconforming)

    def SharedNDTriangleDofs(self):
        r"""SharedNDTriangleDofs(ParFiniteElementSpace self) -> bool"""
        return _pfespace.ParFiniteElementSpace_SharedNDTriangleDofs(self)
    SharedNDTriangleDofs = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_SharedNDTriangleDofs)

    def GetTrueTransferOperator(self, coarse_fes, T):
        r"""GetTrueTransferOperator(ParFiniteElementSpace self, FiniteElementSpace coarse_fes, OperatorHandle T)"""
        return _pfespace.ParFiniteElementSpace_GetTrueTransferOperator(self, coarse_fes, T)
    GetTrueTransferOperator = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetTrueTransferOperator)

    def Update(self, want_transform=True):
        r"""Update(ParFiniteElementSpace self, bool want_transform=True)"""
        return _pfespace.ParFiniteElementSpace_Update(self, want_transform)
    Update = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_Update)

    def UpdatesFinished(self):
        r"""UpdatesFinished(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_UpdatesFinished(self)
    UpdatesFinished = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_UpdatesFinished)
    __swig_destroy__ = _pfespace.delete_ParFiniteElementSpace

    def PrintPartitionStats(self):
        r"""PrintPartitionStats(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_PrintPartitionStats(self)
    PrintPartitionStats = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_PrintPartitionStats)

    def TrueVSize(self):
        r"""TrueVSize(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_TrueVSize(self)
    TrueVSize = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_TrueVSize)

    def GetElementDofTransformation(self, elem):
        r"""GetElementDofTransformation(ParFiniteElementSpace self, int elem) -> DofTransformation"""
        return _pfespace.ParFiniteElementSpace_GetElementDofTransformation(self, elem)
    GetElementDofTransformation = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetElementDofTransformation)

    def GetBdrElementDofTransformation(self, bel):
        r"""GetBdrElementDofTransformation(ParFiniteElementSpace self, int bel) -> DofTransformation"""
        return _pfespace.ParFiniteElementSpace_GetBdrElementDofTransformation(self, bel)
    GetBdrElementDofTransformation = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetBdrElementDofTransformation)

    def GetFaceNbrVDofTransformation(self, elem):
        r"""GetFaceNbrVDofTransformation(ParFiniteElementSpace self, int elem) -> DofTransformation"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrVDofTransformation(self, elem)
    GetFaceNbrVDofTransformation = _swig_new_instance_method(_pfespace.ParFiniteElementSpace_GetFaceNbrVDofTransformation)

# Register ParFiniteElementSpace in _pfespace:
_pfespace.ParFiniteElementSpace_swigregister(ParFiniteElementSpace)

class ConformingProlongationOperator(mfem._par.operators.Operator):
    r"""Proxy of C++ mfem::ConformingProlongationOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ConformingProlongationOperator self, int lsize, GroupCommunicator gc_, bool local_=False) -> ConformingProlongationOperator
        __init__(ConformingProlongationOperator self, ParFiniteElementSpace pfes, bool local_=False) -> ConformingProlongationOperator
        """
        _pfespace.ConformingProlongationOperator_swiginit(self, _pfespace.new_ConformingProlongationOperator(*args))

    def GetGroupCommunicator(self):
        r"""GetGroupCommunicator(ConformingProlongationOperator self) -> GroupCommunicator"""
        return _pfespace.ConformingProlongationOperator_GetGroupCommunicator(self)
    GetGroupCommunicator = _swig_new_instance_method(_pfespace.ConformingProlongationOperator_GetGroupCommunicator)

    def Mult(self, x, y):
        r"""Mult(ConformingProlongationOperator self, Vector x, Vector y)"""
        return _pfespace.ConformingProlongationOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_pfespace.ConformingProlongationOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(ConformingProlongationOperator self, Vector x, Vector y)"""
        return _pfespace.ConformingProlongationOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_pfespace.ConformingProlongationOperator_MultTranspose)
    __swig_destroy__ = _pfespace.delete_ConformingProlongationOperator

# Register ConformingProlongationOperator in _pfespace:
_pfespace.ConformingProlongationOperator_swigregister(ConformingProlongationOperator)

class DeviceConformingProlongationOperator(ConformingProlongationOperator):
    r"""Proxy of C++ mfem::DeviceConformingProlongationOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(DeviceConformingProlongationOperator self, GroupCommunicator gc_, SparseMatrix R, bool local_=False) -> DeviceConformingProlongationOperator
        __init__(DeviceConformingProlongationOperator self, ParFiniteElementSpace pfes, bool local_=False) -> DeviceConformingProlongationOperator
        """
        _pfespace.DeviceConformingProlongationOperator_swiginit(self, _pfespace.new_DeviceConformingProlongationOperator(*args))
    __swig_destroy__ = _pfespace.delete_DeviceConformingProlongationOperator

    def Mult(self, x, y):
        r"""Mult(DeviceConformingProlongationOperator self, Vector x, Vector y)"""
        return _pfespace.DeviceConformingProlongationOperator_Mult(self, x, y)
    Mult = _swig_new_instance_method(_pfespace.DeviceConformingProlongationOperator_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(DeviceConformingProlongationOperator self, Vector x, Vector y)"""
        return _pfespace.DeviceConformingProlongationOperator_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_pfespace.DeviceConformingProlongationOperator_MultTranspose)

# Register DeviceConformingProlongationOperator in _pfespace:
_pfespace.DeviceConformingProlongationOperator_swigregister(DeviceConformingProlongationOperator)



