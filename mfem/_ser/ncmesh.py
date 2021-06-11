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
    from . import _ncmesh
else:
    import _ncmesh

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _ncmesh.SWIG_PyInstanceMethod_New
_swig_new_static_method = _ncmesh.SWIG_PyStaticMethod_New

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

import mfem._ser.mesh
import mfem._ser.matrix
import mfem._ser.vector
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.sort_pairs
import mfem._ser.gridfunc
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
class Refinement(object):
    r"""Proxy of C++ mfem::Refinement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    index = property(_ncmesh.Refinement_index_get, _ncmesh.Refinement_index_set, doc=r"""index : int""")
    ref_type = property(_ncmesh.Refinement_ref_type_get, _ncmesh.Refinement_ref_type_set, doc=r"""ref_type : char""")

    def __init__(self, *args):
        r"""
        __init__(Refinement self) -> Refinement
        __init__(Refinement self, int index, int type=7) -> Refinement
        """
        _ncmesh.Refinement_swiginit(self, _ncmesh.new_Refinement(*args))
    __swig_destroy__ = _ncmesh.delete_Refinement

# Register Refinement in _ncmesh:
_ncmesh.Refinement_swigregister(Refinement)

class Embedding(object):
    r"""Proxy of C++ mfem::Embedding class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    parent = property(_ncmesh.Embedding_parent_get, _ncmesh.Embedding_parent_set, doc=r"""parent : int""")
    matrix = property(_ncmesh.Embedding_matrix_get, _ncmesh.Embedding_matrix_set, doc=r"""matrix : int""")

    def __init__(self, *args):
        r"""
        __init__(Embedding self) -> Embedding
        __init__(Embedding self, int elem, int matrix=0) -> Embedding
        """
        _ncmesh.Embedding_swiginit(self, _ncmesh.new_Embedding(*args))
    __swig_destroy__ = _ncmesh.delete_Embedding

# Register Embedding in _ncmesh:
_ncmesh.Embedding_swigregister(Embedding)

class CoarseFineTransformations(object):
    r"""Proxy of C++ mfem::CoarseFineTransformations class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    point_matrices = property(_ncmesh.CoarseFineTransformations_point_matrices_get, _ncmesh.CoarseFineTransformations_point_matrices_set, doc=r"""point_matrices : a(mfem::Geometry::NumGeom).mfem::DenseTensor""")
    embeddings = property(_ncmesh.CoarseFineTransformations_embeddings_get, doc=r"""embeddings : mfem::Array<(mfem::Embedding)>""")

    def GetCoarseToFineMap(self, fine_mesh, coarse_to_fine, coarse_to_ref_type, ref_type_to_matrix, ref_type_to_geom):
        r"""GetCoarseToFineMap(CoarseFineTransformations self, Mesh fine_mesh, Table coarse_to_fine, intArray coarse_to_ref_type, Table ref_type_to_matrix, GeometryTypeArray ref_type_to_geom)"""
        return _ncmesh.CoarseFineTransformations_GetCoarseToFineMap(self, fine_mesh, coarse_to_fine, coarse_to_ref_type, ref_type_to_matrix, ref_type_to_geom)
    GetCoarseToFineMap = _swig_new_instance_method(_ncmesh.CoarseFineTransformations_GetCoarseToFineMap)

    def Clear(self):
        r"""Clear(CoarseFineTransformations self)"""
        return _ncmesh.CoarseFineTransformations_Clear(self)
    Clear = _swig_new_instance_method(_ncmesh.CoarseFineTransformations_Clear)

    def IsInitialized(self):
        r"""IsInitialized(CoarseFineTransformations self) -> bool"""
        return _ncmesh.CoarseFineTransformations_IsInitialized(self)
    IsInitialized = _swig_new_instance_method(_ncmesh.CoarseFineTransformations_IsInitialized)

    def MemoryUsage(self):
        r"""MemoryUsage(CoarseFineTransformations self) -> long"""
        return _ncmesh.CoarseFineTransformations_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_ncmesh.CoarseFineTransformations_MemoryUsage)

    def __init__(self):
        r"""__init__(CoarseFineTransformations self) -> CoarseFineTransformations"""
        _ncmesh.CoarseFineTransformations_swiginit(self, _ncmesh.new_CoarseFineTransformations())
    __swig_destroy__ = _ncmesh.delete_CoarseFineTransformations

# Register CoarseFineTransformations in _ncmesh:
_ncmesh.CoarseFineTransformations_swigregister(CoarseFineTransformations)


def Swap(a, b):
    r"""Swap(CoarseFineTransformations a, CoarseFineTransformations b)"""
    return _ncmesh.Swap(a, b)
Swap = _ncmesh.Swap
class NCMesh(object):
    r"""Proxy of C++ mfem::NCMesh class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(NCMesh self, Mesh mesh) -> NCMesh
        __init__(NCMesh self, std::istream & input, int version, int & curved, int & is_nc) -> NCMesh
        __init__(NCMesh self, NCMesh other) -> NCMesh
        """
        _ncmesh.NCMesh_swiginit(self, _ncmesh.new_NCMesh(*args))
    __swig_destroy__ = _ncmesh.delete_NCMesh

    def Dimension(self):
        r"""Dimension(NCMesh self) -> int"""
        return _ncmesh.NCMesh_Dimension(self)
    Dimension = _swig_new_instance_method(_ncmesh.NCMesh_Dimension)

    def SpaceDimension(self):
        r"""SpaceDimension(NCMesh self) -> int"""
        return _ncmesh.NCMesh_SpaceDimension(self)
    SpaceDimension = _swig_new_instance_method(_ncmesh.NCMesh_SpaceDimension)

    def GetNVertices(self):
        r"""GetNVertices(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNVertices(self)
    GetNVertices = _swig_new_instance_method(_ncmesh.NCMesh_GetNVertices)

    def GetNEdges(self):
        r"""GetNEdges(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNEdges(self)
    GetNEdges = _swig_new_instance_method(_ncmesh.NCMesh_GetNEdges)

    def GetNFaces(self):
        r"""GetNFaces(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNFaces(self)
    GetNFaces = _swig_new_instance_method(_ncmesh.NCMesh_GetNFaces)

    def Refine(self, refinements):
        r"""Refine(NCMesh self, RefinementArray refinements)"""
        return _ncmesh.NCMesh_Refine(self, refinements)
    Refine = _swig_new_instance_method(_ncmesh.NCMesh_Refine)

    def LimitNCLevel(self, max_nc_level):
        r"""LimitNCLevel(NCMesh self, int max_nc_level)"""
        return _ncmesh.NCMesh_LimitNCLevel(self, max_nc_level)
    LimitNCLevel = _swig_new_instance_method(_ncmesh.NCMesh_LimitNCLevel)

    def GetDerefinementTable(self):
        r"""GetDerefinementTable(NCMesh self) -> Table"""
        return _ncmesh.NCMesh_GetDerefinementTable(self)
    GetDerefinementTable = _swig_new_instance_method(_ncmesh.NCMesh_GetDerefinementTable)

    def CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level):
        r"""CheckDerefinementNCLevel(NCMesh self, Table deref_table, intArray level_ok, int max_nc_level)"""
        return _ncmesh.NCMesh_CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level)
    CheckDerefinementNCLevel = _swig_new_instance_method(_ncmesh.NCMesh_CheckDerefinementNCLevel)

    def Derefine(self, derefs):
        r"""Derefine(NCMesh self, intArray derefs)"""
        return _ncmesh.NCMesh_Derefine(self, derefs)
    Derefine = _swig_new_instance_method(_ncmesh.NCMesh_Derefine)

    def GetFaceList(self):
        r"""GetFaceList(NCMesh self) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetFaceList(self)
    GetFaceList = _swig_new_instance_method(_ncmesh.NCMesh_GetFaceList)

    def GetEdgeList(self):
        r"""GetEdgeList(NCMesh self) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetEdgeList(self)
    GetEdgeList = _swig_new_instance_method(_ncmesh.NCMesh_GetEdgeList)

    def GetVertexList(self):
        r"""GetVertexList(NCMesh self) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetVertexList(self)
    GetVertexList = _swig_new_instance_method(_ncmesh.NCMesh_GetVertexList)

    def GetNCList(self, entity):
        r"""GetNCList(NCMesh self, int entity) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetNCList(self, entity)
    GetNCList = _swig_new_instance_method(_ncmesh.NCMesh_GetNCList)

    def MarkCoarseLevel(self):
        r"""MarkCoarseLevel(NCMesh self)"""
        return _ncmesh.NCMesh_MarkCoarseLevel(self)
    MarkCoarseLevel = _swig_new_instance_method(_ncmesh.NCMesh_MarkCoarseLevel)

    def GetRefinementTransforms(self):
        r"""GetRefinementTransforms(NCMesh self) -> CoarseFineTransformations"""
        return _ncmesh.NCMesh_GetRefinementTransforms(self)
    GetRefinementTransforms = _swig_new_instance_method(_ncmesh.NCMesh_GetRefinementTransforms)

    def GetDerefinementTransforms(self):
        r"""GetDerefinementTransforms(NCMesh self) -> CoarseFineTransformations"""
        return _ncmesh.NCMesh_GetDerefinementTransforms(self)
    GetDerefinementTransforms = _swig_new_instance_method(_ncmesh.NCMesh_GetDerefinementTransforms)

    def ClearTransforms(self):
        r"""ClearTransforms(NCMesh self)"""
        return _ncmesh.NCMesh_ClearTransforms(self)
    ClearTransforms = _swig_new_instance_method(_ncmesh.NCMesh_ClearTransforms)

    @staticmethod
    def GridSfcOrdering2D(width, height, coords):
        r"""GridSfcOrdering2D(int width, int height, intArray coords)"""
        return _ncmesh.NCMesh_GridSfcOrdering2D(width, height, coords)
    GridSfcOrdering2D = _swig_new_static_method(_ncmesh.NCMesh_GridSfcOrdering2D)

    @staticmethod
    def GridSfcOrdering3D(width, height, depth, coords):
        r"""GridSfcOrdering3D(int width, int height, int depth, intArray coords)"""
        return _ncmesh.NCMesh_GridSfcOrdering3D(width, height, depth, coords)
    GridSfcOrdering3D = _swig_new_static_method(_ncmesh.NCMesh_GridSfcOrdering3D)

    def GetEdgeVertices(self, edge_id, vert_index, oriented=True):
        r"""GetEdgeVertices(NCMesh self, mfem::NCMesh::MeshId const & edge_id, int [2] vert_index, bool oriented=True)"""
        return _ncmesh.NCMesh_GetEdgeVertices(self, edge_id, vert_index, oriented)
    GetEdgeVertices = _swig_new_instance_method(_ncmesh.NCMesh_GetEdgeVertices)

    def GetEdgeNCOrientation(self, edge_id):
        r"""GetEdgeNCOrientation(NCMesh self, mfem::NCMesh::MeshId const & edge_id) -> int"""
        return _ncmesh.NCMesh_GetEdgeNCOrientation(self, edge_id)
    GetEdgeNCOrientation = _swig_new_instance_method(_ncmesh.NCMesh_GetEdgeNCOrientation)

    def GetFaceVerticesEdges(self, face_id, vert_index, edge_index, edge_orientation):
        r"""GetFaceVerticesEdges(NCMesh self, mfem::NCMesh::MeshId const & face_id, int [4] vert_index, int [4] edge_index, int [4] edge_orientation) -> int"""
        return _ncmesh.NCMesh_GetFaceVerticesEdges(self, face_id, vert_index, edge_index, edge_orientation)
    GetFaceVerticesEdges = _swig_new_instance_method(_ncmesh.NCMesh_GetFaceVerticesEdges)

    def GetEdgeMaster(self, v1, v2):
        r"""GetEdgeMaster(NCMesh self, int v1, int v2) -> int"""
        return _ncmesh.NCMesh_GetEdgeMaster(self, v1, v2)
    GetEdgeMaster = _swig_new_instance_method(_ncmesh.NCMesh_GetEdgeMaster)

    def GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges):
        r"""GetBoundaryClosure(NCMesh self, intArray bdr_attr_is_ess, intArray bdr_vertices, intArray bdr_edges)"""
        return _ncmesh.NCMesh_GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges)
    GetBoundaryClosure = _swig_new_instance_method(_ncmesh.NCMesh_GetBoundaryClosure)

    def GetElementGeometry(self, index):
        r"""GetElementGeometry(NCMesh self, int index) -> mfem::Geometry::Type"""
        return _ncmesh.NCMesh_GetElementGeometry(self, index)
    GetElementGeometry = _swig_new_instance_method(_ncmesh.NCMesh_GetElementGeometry)

    def GetFaceGeometry(self, index):
        r"""GetFaceGeometry(NCMesh self, int index) -> mfem::Geometry::Type"""
        return _ncmesh.NCMesh_GetFaceGeometry(self, index)
    GetFaceGeometry = _swig_new_instance_method(_ncmesh.NCMesh_GetFaceGeometry)

    def GetNumRootElements(self):
        r"""GetNumRootElements(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNumRootElements(self)
    GetNumRootElements = _swig_new_instance_method(_ncmesh.NCMesh_GetNumRootElements)

    def GetElementDepth(self, i):
        r"""GetElementDepth(NCMesh self, int i) -> int"""
        return _ncmesh.NCMesh_GetElementDepth(self, i)
    GetElementDepth = _swig_new_instance_method(_ncmesh.NCMesh_GetElementDepth)

    def GetElementSizeReduction(self, i):
        r"""GetElementSizeReduction(NCMesh self, int i) -> int"""
        return _ncmesh.NCMesh_GetElementSizeReduction(self, i)
    GetElementSizeReduction = _swig_new_instance_method(_ncmesh.NCMesh_GetElementSizeReduction)

    def GetElementFacesAttributes(self, i, faces, fattr):
        r"""GetElementFacesAttributes(NCMesh self, int i, intArray faces, intArray fattr)"""
        return _ncmesh.NCMesh_GetElementFacesAttributes(self, i, faces, fattr)
    GetElementFacesAttributes = _swig_new_instance_method(_ncmesh.NCMesh_GetElementFacesAttributes)

    def Print(self, out):
        r"""Print(NCMesh self, std::ostream & out)"""
        return _ncmesh.NCMesh_Print(self, out)
    Print = _swig_new_instance_method(_ncmesh.NCMesh_Print)

    def IsLegacyLoaded(self):
        r"""IsLegacyLoaded(NCMesh self) -> bool"""
        return _ncmesh.NCMesh_IsLegacyLoaded(self)
    IsLegacyLoaded = _swig_new_instance_method(_ncmesh.NCMesh_IsLegacyLoaded)

    def LegacyToNewVertexOrdering(self, order):
        r"""LegacyToNewVertexOrdering(NCMesh self, intArray order)"""
        return _ncmesh.NCMesh_LegacyToNewVertexOrdering(self, order)
    LegacyToNewVertexOrdering = _swig_new_instance_method(_ncmesh.NCMesh_LegacyToNewVertexOrdering)

    def Trim(self):
        r"""Trim(NCMesh self)"""
        return _ncmesh.NCMesh_Trim(self)
    Trim = _swig_new_instance_method(_ncmesh.NCMesh_Trim)

    def MemoryUsage(self):
        r"""MemoryUsage(NCMesh self) -> long"""
        return _ncmesh.NCMesh_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_ncmesh.NCMesh_MemoryUsage)

    def PrintMemoryDetail(self):
        r"""PrintMemoryDetail(NCMesh self) -> int"""
        return _ncmesh.NCMesh_PrintMemoryDetail(self)
    PrintMemoryDetail = _swig_new_instance_method(_ncmesh.NCMesh_PrintMemoryDetail)

# Register NCMesh in _ncmesh:
_ncmesh.NCMesh_swigregister(NCMesh)

def NCMesh_GridSfcOrdering2D(width, height, coords):
    r"""NCMesh_GridSfcOrdering2D(int width, int height, intArray coords)"""
    return _ncmesh.NCMesh_GridSfcOrdering2D(width, height, coords)
NCMesh_GridSfcOrdering2D = _ncmesh.NCMesh_GridSfcOrdering2D

def NCMesh_GridSfcOrdering3D(width, height, depth, coords):
    r"""NCMesh_GridSfcOrdering3D(int width, int height, int depth, intArray coords)"""
    return _ncmesh.NCMesh_GridSfcOrdering3D(width, height, depth, coords)
NCMesh_GridSfcOrdering3D = _ncmesh.NCMesh_GridSfcOrdering3D

class RefinementArray(object):
    r"""Proxy of C++ mfem::Array< mfem::Refinement > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(RefinementArray self) -> RefinementArray
        __init__(RefinementArray self, mfem::MemoryType mt) -> RefinementArray
        __init__(RefinementArray self, int asize) -> RefinementArray
        __init__(RefinementArray self, Refinement data_, int asize) -> RefinementArray
        __init__(RefinementArray self, RefinementArray src) -> RefinementArray
        """
        _ncmesh.RefinementArray_swiginit(self, _ncmesh.new_RefinementArray(*args))

        if len(args) == 1 and isinstance(args[0], list):
            self.MakeDataOwner()



    __swig_destroy__ = _ncmesh.delete_RefinementArray

    def GetData(self, *args):
        r"""
        GetData(RefinementArray self) -> Refinement
        GetData(RefinementArray self) -> Refinement
        """
        return _ncmesh.RefinementArray_GetData(self, *args)
    GetData = _swig_new_instance_method(_ncmesh.RefinementArray_GetData)

    def GetMemory(self, *args):
        r"""
        GetMemory(RefinementArray self) -> mfem::Memory< mfem::Refinement >
        GetMemory(RefinementArray self) -> mfem::Memory< mfem::Refinement > const &
        """
        return _ncmesh.RefinementArray_GetMemory(self, *args)
    GetMemory = _swig_new_instance_method(_ncmesh.RefinementArray_GetMemory)

    def UseDevice(self):
        r"""UseDevice(RefinementArray self) -> bool"""
        return _ncmesh.RefinementArray_UseDevice(self)
    UseDevice = _swig_new_instance_method(_ncmesh.RefinementArray_UseDevice)

    def OwnsData(self):
        r"""OwnsData(RefinementArray self) -> bool"""
        return _ncmesh.RefinementArray_OwnsData(self)
    OwnsData = _swig_new_instance_method(_ncmesh.RefinementArray_OwnsData)

    def StealData(self, p):
        r"""StealData(RefinementArray self, mfem::Refinement ** p)"""
        return _ncmesh.RefinementArray_StealData(self, p)
    StealData = _swig_new_instance_method(_ncmesh.RefinementArray_StealData)

    def LoseData(self):
        r"""LoseData(RefinementArray self)"""
        return _ncmesh.RefinementArray_LoseData(self)
    LoseData = _swig_new_instance_method(_ncmesh.RefinementArray_LoseData)

    def MakeDataOwner(self):
        r"""MakeDataOwner(RefinementArray self)"""
        return _ncmesh.RefinementArray_MakeDataOwner(self)
    MakeDataOwner = _swig_new_instance_method(_ncmesh.RefinementArray_MakeDataOwner)

    def Size(self):
        r"""Size(RefinementArray self) -> int"""
        return _ncmesh.RefinementArray_Size(self)
    Size = _swig_new_instance_method(_ncmesh.RefinementArray_Size)

    def SetSize(self, *args):
        r"""
        SetSize(RefinementArray self, int nsize)
        SetSize(RefinementArray self, int nsize, Refinement initval)
        SetSize(RefinementArray self, int nsize, mfem::MemoryType mt)
        """
        return _ncmesh.RefinementArray_SetSize(self, *args)
    SetSize = _swig_new_instance_method(_ncmesh.RefinementArray_SetSize)

    def Capacity(self):
        r"""Capacity(RefinementArray self) -> int"""
        return _ncmesh.RefinementArray_Capacity(self)
    Capacity = _swig_new_instance_method(_ncmesh.RefinementArray_Capacity)

    def Reserve(self, capacity):
        r"""Reserve(RefinementArray self, int capacity)"""
        return _ncmesh.RefinementArray_Reserve(self, capacity)
    Reserve = _swig_new_instance_method(_ncmesh.RefinementArray_Reserve)

    def Append(self, *args):
        r"""
        Append(RefinementArray self, Refinement el) -> int
        Append(RefinementArray self, Refinement els, int nels) -> int
        Append(RefinementArray self, RefinementArray els) -> int
        """
        return _ncmesh.RefinementArray_Append(self, *args)
    Append = _swig_new_instance_method(_ncmesh.RefinementArray_Append)

    def Prepend(self, el):
        r"""Prepend(RefinementArray self, Refinement el) -> int"""
        return _ncmesh.RefinementArray_Prepend(self, el)
    Prepend = _swig_new_instance_method(_ncmesh.RefinementArray_Prepend)

    def Last(self, *args):
        r"""
        Last(RefinementArray self) -> Refinement
        Last(RefinementArray self) -> Refinement
        """
        return _ncmesh.RefinementArray_Last(self, *args)
    Last = _swig_new_instance_method(_ncmesh.RefinementArray_Last)

    def DeleteLast(self):
        r"""DeleteLast(RefinementArray self)"""
        return _ncmesh.RefinementArray_DeleteLast(self)
    DeleteLast = _swig_new_instance_method(_ncmesh.RefinementArray_DeleteLast)

    def DeleteAll(self):
        r"""DeleteAll(RefinementArray self)"""
        return _ncmesh.RefinementArray_DeleteAll(self)
    DeleteAll = _swig_new_instance_method(_ncmesh.RefinementArray_DeleteAll)

    def Copy(self, copy):
        r"""Copy(RefinementArray self, RefinementArray copy)"""
        return _ncmesh.RefinementArray_Copy(self, copy)
    Copy = _swig_new_instance_method(_ncmesh.RefinementArray_Copy)

    def MakeRef(self, *args):
        r"""
        MakeRef(RefinementArray self, Refinement arg2, int arg3)
        MakeRef(RefinementArray self, RefinementArray master)
        """
        return _ncmesh.RefinementArray_MakeRef(self, *args)
    MakeRef = _swig_new_instance_method(_ncmesh.RefinementArray_MakeRef)

    def GetSubArray(self, offset, sa_size, sa):
        r"""GetSubArray(RefinementArray self, int offset, int sa_size, RefinementArray sa)"""
        return _ncmesh.RefinementArray_GetSubArray(self, offset, sa_size, sa)
    GetSubArray = _swig_new_instance_method(_ncmesh.RefinementArray_GetSubArray)

    def begin(self, *args):
        r"""
        begin(RefinementArray self) -> Refinement
        begin(RefinementArray self) -> Refinement
        """
        return _ncmesh.RefinementArray_begin(self, *args)
    begin = _swig_new_instance_method(_ncmesh.RefinementArray_begin)

    def end(self, *args):
        r"""
        end(RefinementArray self) -> Refinement
        end(RefinementArray self) -> Refinement
        """
        return _ncmesh.RefinementArray_end(self, *args)
    end = _swig_new_instance_method(_ncmesh.RefinementArray_end)

    def MemoryUsage(self):
        r"""MemoryUsage(RefinementArray self) -> long"""
        return _ncmesh.RefinementArray_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_ncmesh.RefinementArray_MemoryUsage)

    def Read(self, on_dev=True):
        r"""Read(RefinementArray self, bool on_dev=True) -> Refinement"""
        return _ncmesh.RefinementArray_Read(self, on_dev)
    Read = _swig_new_instance_method(_ncmesh.RefinementArray_Read)

    def HostRead(self):
        r"""HostRead(RefinementArray self) -> Refinement"""
        return _ncmesh.RefinementArray_HostRead(self)
    HostRead = _swig_new_instance_method(_ncmesh.RefinementArray_HostRead)

    def Write(self, on_dev=True):
        r"""Write(RefinementArray self, bool on_dev=True) -> Refinement"""
        return _ncmesh.RefinementArray_Write(self, on_dev)
    Write = _swig_new_instance_method(_ncmesh.RefinementArray_Write)

    def HostWrite(self):
        r"""HostWrite(RefinementArray self) -> Refinement"""
        return _ncmesh.RefinementArray_HostWrite(self)
    HostWrite = _swig_new_instance_method(_ncmesh.RefinementArray_HostWrite)

    def ReadWrite(self, on_dev=True):
        r"""ReadWrite(RefinementArray self, bool on_dev=True) -> Refinement"""
        return _ncmesh.RefinementArray_ReadWrite(self, on_dev)
    ReadWrite = _swig_new_instance_method(_ncmesh.RefinementArray_ReadWrite)

    def HostReadWrite(self):
        r"""HostReadWrite(RefinementArray self) -> Refinement"""
        return _ncmesh.RefinementArray_HostReadWrite(self)
    HostReadWrite = _swig_new_instance_method(_ncmesh.RefinementArray_HostReadWrite)

    def __setitem__(self, i, v):
        r"""__setitem__(RefinementArray self, int i, Refinement v)"""
        return _ncmesh.RefinementArray___setitem__(self, i, v)
    __setitem__ = _swig_new_instance_method(_ncmesh.RefinementArray___setitem__)

    def __getitem__(self, i):
        r"""__getitem__(RefinementArray self, int const i) -> Refinement"""
        return _ncmesh.RefinementArray___getitem__(self, i)
    __getitem__ = _swig_new_instance_method(_ncmesh.RefinementArray___getitem__)

    def Assign(self, *args):
        r"""
        Assign(RefinementArray self, Refinement arg2)
        Assign(RefinementArray self, Refinement a)
        """
        return _ncmesh.RefinementArray_Assign(self, *args)
    Assign = _swig_new_instance_method(_ncmesh.RefinementArray_Assign)

    def ToList(self):
        return [self[i] for i in range(self.Size())]



# Register RefinementArray in _ncmesh:
_ncmesh.RefinementArray_swigregister(RefinementArray)



