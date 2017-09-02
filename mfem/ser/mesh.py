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
        mname = '.'.join((pkg, '_mesh')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_mesh')
    _mesh = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mesh', [dirname(__file__)])
        except ImportError:
            import _mesh
            return _mesh
        try:
            _mod = imp.load_module('_mesh', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _mesh = swig_import_helper()
    del swig_import_helper
else:
    import _mesh
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

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _mesh.new_intp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mesh.delete_intp
    __del__ = lambda self: None

    def assign(self, value):
        return _mesh.intp_assign(self, value)

    def value(self):
        return _mesh.intp_value(self)

    def cast(self):
        return _mesh.intp_cast(self)
    if _newclass:
        frompointer = staticmethod(_mesh.intp_frompointer)
    else:
        frompointer = _mesh.intp_frompointer
intp_swigregister = _mesh.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t):
    return _mesh.intp_frompointer(t)
intp_frompointer = _mesh.intp_frompointer

import matrix
import vector
import array
import ostream_typemap
import operators
import ncmesh
import gridfunc
import coefficient
import intrules
import sparsemat
import densemat
import eltrans
import fe
import fespace
import fe_coll
import lininteg
import bilininteg
import linearform
import element
import geom
import table
import vertex
class Mesh(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Mesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Mesh, name)
    __repr__ = _swig_repr
    NONE = _mesh.Mesh_NONE
    REFINE = _mesh.Mesh_REFINE
    DEREFINE = _mesh.Mesh_DEREFINE
    REBALANCE = _mesh.Mesh_REBALANCE
    __swig_getmethods__["attributes"] = _mesh.Mesh_attributes_get
    if _newclass:
        attributes = _swig_property(_mesh.Mesh_attributes_get)
    __swig_getmethods__["bdr_attributes"] = _mesh.Mesh_bdr_attributes_get
    if _newclass:
        bdr_attributes = _swig_property(_mesh.Mesh_bdr_attributes_get)
    __swig_setmethods__["NURBSext"] = _mesh.Mesh_NURBSext_set
    __swig_getmethods__["NURBSext"] = _mesh.Mesh_NURBSext_get
    if _newclass:
        NURBSext = _swig_property(_mesh.Mesh_NURBSext_get, _mesh.Mesh_NURBSext_set)
    __swig_setmethods__["ncmesh"] = _mesh.Mesh_ncmesh_set
    __swig_getmethods__["ncmesh"] = _mesh.Mesh_ncmesh_get
    if _newclass:
        ncmesh = _swig_property(_mesh.Mesh_ncmesh_get, _mesh.Mesh_ncmesh_set)

    def NewElement(self, geom):
        return _mesh.Mesh_NewElement(self, geom)

    def AddVertex(self, arg2):
        return _mesh.Mesh_AddVertex(self, arg2)

    def AddTri(self, vi, attr=1):
        return _mesh.Mesh_AddTri(self, vi, attr)

    def AddTriangle(self, vi, attr=1):
        return _mesh.Mesh_AddTriangle(self, vi, attr)

    def AddQuad(self, vi, attr=1):
        return _mesh.Mesh_AddQuad(self, vi, attr)

    def AddTet(self, vi, attr=1):
        return _mesh.Mesh_AddTet(self, vi, attr)

    def AddHex(self, vi, attr=1):
        return _mesh.Mesh_AddHex(self, vi, attr)

    def AddHexAsTets(self, vi, attr=1):
        return _mesh.Mesh_AddHexAsTets(self, vi, attr)

    def AddElement(self, elem):
        return _mesh.Mesh_AddElement(self, elem)

    def AddBdrElement(self, elem):
        return _mesh.Mesh_AddBdrElement(self, elem)

    def AddBdrSegment(self, vi, attr=1):
        return _mesh.Mesh_AddBdrSegment(self, vi, attr)

    def AddBdrTriangle(self, vi, attr=1):
        return _mesh.Mesh_AddBdrTriangle(self, vi, attr)

    def AddBdrQuad(self, vi, attr=1):
        return _mesh.Mesh_AddBdrQuad(self, vi, attr)

    def AddBdrQuadAsTriangles(self, vi, attr=1):
        return _mesh.Mesh_AddBdrQuadAsTriangles(self, vi, attr)

    def GenerateBoundaryElements(self):
        return _mesh.Mesh_GenerateBoundaryElements(self)

    def FinalizeTriMesh(self, generate_edges=0, refine=0, fix_orientation=True):
        return _mesh.Mesh_FinalizeTriMesh(self, generate_edges, refine, fix_orientation)

    def FinalizeQuadMesh(self, generate_edges=0, refine=0, fix_orientation=True):
        return _mesh.Mesh_FinalizeQuadMesh(self, generate_edges, refine, fix_orientation)

    def FinalizeTetMesh(self, generate_edges=0, refine=0, fix_orientation=True):
        return _mesh.Mesh_FinalizeTetMesh(self, generate_edges, refine, fix_orientation)

    def FinalizeHexMesh(self, generate_edges=0, refine=0, fix_orientation=True):
        return _mesh.Mesh_FinalizeHexMesh(self, generate_edges, refine, fix_orientation)

    def FinalizeTopology(self):
        return _mesh.Mesh_FinalizeTopology(self)

    def Finalize(self, refine=False, fix_orientation=False):
        return _mesh.Mesh_Finalize(self, refine, fix_orientation)

    def SetAttributes(self):
        return _mesh.Mesh_SetAttributes(self)

    def ReorderElements(self, ordering, reorder_vertices=True):
        return _mesh.Mesh_ReorderElements(self, ordering, reorder_vertices)

    def Load(self, input, generate_edges=0, refine=1, fix_orientation=True):
        return _mesh.Mesh_Load(self, input, generate_edges, refine, fix_orientation)

    def Clear(self):
        return _mesh.Mesh_Clear(self)

    def MeshGenerator(self):
        return _mesh.Mesh_MeshGenerator(self)

    def GetNV(self):
        return _mesh.Mesh_GetNV(self)

    def GetNE(self):
        return _mesh.Mesh_GetNE(self)

    def GetNBE(self):
        return _mesh.Mesh_GetNBE(self)

    def GetNEdges(self):
        return _mesh.Mesh_GetNEdges(self)

    def GetNFaces(self):
        return _mesh.Mesh_GetNFaces(self)

    def GetNumFaces(self):
        return _mesh.Mesh_GetNumFaces(self)

    def ReduceInt(self, value):
        return _mesh.Mesh_ReduceInt(self, value)

    def GetGlobalNE(self):
        return _mesh.Mesh_GetGlobalNE(self)

    def EulerNumber(self):
        return _mesh.Mesh_EulerNumber(self)

    def EulerNumber2D(self):
        return _mesh.Mesh_EulerNumber2D(self)

    def Dimension(self):
        return _mesh.Mesh_Dimension(self)

    def SpaceDimension(self):
        return _mesh.Mesh_SpaceDimension(self)

    def GetVertex(self, *args):
        return _mesh.Mesh_GetVertex(self, *args)

    def GetElementData(self, geom, elem_vtx, attr):
        return _mesh.Mesh_GetElementData(self, geom, elem_vtx, attr)

    def GetBdrElementData(self, geom, bdr_elem_vtx, bdr_attr):
        return _mesh.Mesh_GetBdrElementData(self, geom, bdr_elem_vtx, bdr_attr)

    def ChangeVertexDataOwnership(self, vertices, len_vertices, zerocopy=False):
        return _mesh.Mesh_ChangeVertexDataOwnership(self, vertices, len_vertices, zerocopy)

    def GetElementsArray(self):
        return _mesh.Mesh_GetElementsArray(self)

    def GetElement(self, *args):
        return _mesh.Mesh_GetElement(self, *args)

    def GetBdrElement(self, *args):
        return _mesh.Mesh_GetBdrElement(self, *args)

    def GetFace(self, i):
        return _mesh.Mesh_GetFace(self, i)

    def GetFaceBaseGeometry(self, i):
        return _mesh.Mesh_GetFaceBaseGeometry(self, i)

    def GetElementBaseGeometry(self, i=0):
        return _mesh.Mesh_GetElementBaseGeometry(self, i)

    def GetBdrElementBaseGeometry(self, i=0):
        return _mesh.Mesh_GetBdrElementBaseGeometry(self, i)

    def GetElementVertices(self, i):
        from  .array import intArray
        ivert = intArray()
        _mesh.Mesh_GetElementVertices(self, i, ivert)
        return ivert.ToList()



    def GetBdrElementVertices(self, i):
        from  .array import intArray
        ivert = intArray()
        _mesh.Mesh_GetBdrElementVertices(self, i, ivert)
        return ivert.ToList()



    def GetElementEdges(self, i):
        from  .array import intArray
        ia = intArray()
        ib = intArray()      
        _mesh.Mesh_GetElementEdges(self, i, ia, ib)
        return ia.ToList(), ib.ToList()      



    def GetBdrElementEdges(self, i):
        from  .array import intArray
        ia = intArray()
        ib = intArray()      
        _mesh.Mesh_GetBdrElementEdges(self, i, ia, ib)
        return ia.ToList(), ib.ToList()



    def GetFaceEdges(self, i):
        from  .array import intArray
        ia = intArray()
        ib = intArray()      
        _mesh.Mesh_GetFaceEdges(self, i, ia, ib)
        return ia.ToList(), ib.ToList()



    def GetFaceVertices(self, i):
        from  .array import intArray
        ia = intArray()
        _mesh.Mesh_GetFaceVertices(self, i, ia)
        return ia.ToList()



    def GetEdgeVertices(self, i):
        from  .array import intArray
        ia = intArray()
        _mesh.Mesh_GetEdgeVertices(self, i, ia)
        return ia.ToList()



    def GetFaceEdgeTable(self):
        return _mesh.Mesh_GetFaceEdgeTable(self)

    def GetEdgeVertexTable(self):
        return _mesh.Mesh_GetEdgeVertexTable(self)

    def GetElementFaces(self, i):
        from  .array import intArray
        ia = intArray()
        ib = intArray()      
        _mesh.Mesh_GetElementFaces(self, i, ia, ib)
        return ia.ToList(), ib.ToList()



    def GetBdrElementEdgeIndex(self, i):
        return _mesh.Mesh_GetBdrElementEdgeIndex(self, i)

    def GetBdrElementAdjacentElement(self, bdr_el, el, info):
        return _mesh.Mesh_GetBdrElementAdjacentElement(self, bdr_el, el, info)

    def GetElementType(self, i):
        return _mesh.Mesh_GetElementType(self, i)

    def GetBdrElementType(self, i):
        return _mesh.Mesh_GetBdrElementType(self, i)

    def GetPointMatrix(self, i, pointmat):
        return _mesh.Mesh_GetPointMatrix(self, i, pointmat)

    def GetBdrPointMatrix(self, i, pointmat):
        return _mesh.Mesh_GetBdrPointMatrix(self, i, pointmat)
    if _newclass:
        GetTransformationFEforElementType = staticmethod(_mesh.Mesh_GetTransformationFEforElementType)
    else:
        GetTransformationFEforElementType = _mesh.Mesh_GetTransformationFEforElementType

    def GetElementTransformation(self, *args):
        return _mesh.Mesh_GetElementTransformation(self, *args)

    def GetBdrElementTransformation(self, *args):
        return _mesh.Mesh_GetBdrElementTransformation(self, *args)

    def GetFaceTransformation(self, *args):
        return _mesh.Mesh_GetFaceTransformation(self, *args)

    def GetEdgeTransformation(self, *args):
        return _mesh.Mesh_GetEdgeTransformation(self, *args)

    def GetFaceElementTransformations(self, FaceNo, mask=31):
        return _mesh.Mesh_GetFaceElementTransformations(self, FaceNo, mask)

    def GetInteriorFaceTransformations(self, FaceNo):
        return _mesh.Mesh_GetInteriorFaceTransformations(self, FaceNo)

    def GetBdrFaceTransformations(self, BdrElemNo):
        return _mesh.Mesh_GetBdrFaceTransformations(self, BdrElemNo)

    def FaceIsInterior(self, FaceNo):
        return _mesh.Mesh_FaceIsInterior(self, FaceNo)

    def GetFaceElements(self, Face):
        Elem1 = intp()
        Elem2 = intp()  
        val = _mesh.Mesh_GetFaceElements(self, Face, Elem1, Elem2)
        return Elem1.value(), Elem2.value()



    def GetFaceInfos(self, Face, Inf1, Inf2):
        return _mesh.Mesh_GetFaceInfos(self, Face, Inf1, Inf2)

    def GetFaceGeometryType(self, Face):
        return _mesh.Mesh_GetFaceGeometryType(self, Face)

    def GetFaceElementType(self, Face):
        return _mesh.Mesh_GetFaceElementType(self, Face)

    def CheckElementOrientation(self, fix_it=True):
        return _mesh.Mesh_CheckElementOrientation(self, fix_it)

    def CheckBdrElementOrientation(self, fix_it=True):
        return _mesh.Mesh_CheckBdrElementOrientation(self, fix_it)

    def GetAttribute(self, i):
        return _mesh.Mesh_GetAttribute(self, i)

    def SetAttribute(self, i, attr):
        return _mesh.Mesh_SetAttribute(self, i, attr)

    def GetBdrAttribute(self, i):
        return _mesh.Mesh_GetBdrAttribute(self, i)

    def ElementToElementTable(self):
        return _mesh.Mesh_ElementToElementTable(self)

    def ElementToFaceTable(self):
        return _mesh.Mesh_ElementToFaceTable(self)

    def ElementToEdgeTable(self):
        return _mesh.Mesh_ElementToEdgeTable(self)

    def GetVertexToElementTable(self):
        return _mesh.Mesh_GetVertexToElementTable(self)

    def GetFaceToElementTable(self):
        return _mesh.Mesh_GetFaceToElementTable(self)

    def ReorientTetMesh(self):
        return _mesh.Mesh_ReorientTetMesh(self)

    def CartesianPartitioning(self, nxyz):
        return _mesh.Mesh_CartesianPartitioning(self, nxyz)

    def GeneratePartitioning(self, nparts, part_method=1):
        return _mesh.Mesh_GeneratePartitioning(self, nparts, part_method)

    def CheckPartitioning(self, partitioning):
        return _mesh.Mesh_CheckPartitioning(self, partitioning)

    def CheckDisplacements(self, displacements, tmax):
        return _mesh.Mesh_CheckDisplacements(self, displacements, tmax)

    def MoveVertices(self, displacements):
        return _mesh.Mesh_MoveVertices(self, displacements)

    def GetVertices(self, vert_coord):
        return _mesh.Mesh_GetVertices(self, vert_coord)

    def SetVertices(self, vert_coord):
        return _mesh.Mesh_SetVertices(self, vert_coord)

    def GetNode(self, i, coord):
        return _mesh.Mesh_GetNode(self, i, coord)

    def SetNode(self, i, coord):
        return _mesh.Mesh_SetNode(self, i, coord)

    def MoveNodes(self, displacements):
        return _mesh.Mesh_MoveNodes(self, displacements)

    def SetNodes(self, node_coord):
        return _mesh.Mesh_SetNodes(self, node_coord)

    def OwnsNodes(self):
        return _mesh.Mesh_OwnsNodes(self)

    def SetNodesOwner(self, nodes_owner):
        return _mesh.Mesh_SetNodesOwner(self, nodes_owner)

    def NewNodes(self, nodes, make_owner=False):
        return _mesh.Mesh_NewNodes(self, nodes, make_owner)

    def SwapNodes(self, nodes, own_nodes_):
        return _mesh.Mesh_SwapNodes(self, nodes, own_nodes_)

    def GetNodes(self, *args):
        return _mesh.Mesh_GetNodes(self, *args)

    def SetNodalFESpace(self, nfes):
        return _mesh.Mesh_SetNodalFESpace(self, nfes)

    def SetNodalGridFunction(self, nodes, make_owner=False):
        return _mesh.Mesh_SetNodalGridFunction(self, nodes, make_owner)

    def GetNodalFESpace(self):
        return _mesh.Mesh_GetNodalFESpace(self)

    def SetCurvature(self, order, discont=False, space_dim=-1, ordering=1):
        return _mesh.Mesh_SetCurvature(self, order, discont, space_dim, ordering)

    def UniformRefinement(self):
        return _mesh.Mesh_UniformRefinement(self)

    def GeneralRefinement(self, *args):
        return _mesh.Mesh_GeneralRefinement(self, *args)

    def RandomRefinement(self, prob, aniso=False, nonconforming=-1, nc_limit=0):
        return _mesh.Mesh_RandomRefinement(self, prob, aniso, nonconforming, nc_limit)

    def RefineAtVertex(self, vert, eps=0.0, nonconforming=-1):
        return _mesh.Mesh_RefineAtVertex(self, vert, eps, nonconforming)

    def RefineByError(self, *args):
        return _mesh.Mesh_RefineByError(self, *args)

    def DerefineByError(self, *args):
        return _mesh.Mesh_DerefineByError(self, *args)

    def KnotInsert(self, kv):
        return _mesh.Mesh_KnotInsert(self, kv)

    def DegreeElevate(self, t):
        return _mesh.Mesh_DegreeElevate(self, t)

    def EnsureNCMesh(self, triangles_nonconforming=False):
        return _mesh.Mesh_EnsureNCMesh(self, triangles_nonconforming)

    def Conforming(self):
        return _mesh.Mesh_Conforming(self)

    def Nonconforming(self):
        return _mesh.Mesh_Nonconforming(self)

    def GetRefinementTransforms(self):
        return _mesh.Mesh_GetRefinementTransforms(self)

    def GetLastOperation(self):
        return _mesh.Mesh_GetLastOperation(self)

    def GetSequence(self):
        return _mesh.Mesh_GetSequence(self)

    def PrintXG(self, *args):
        return _mesh.Mesh_PrintXG(self, *args)

    def Print(self, *args):
        return _mesh.Mesh_Print(self, *args)

    def PrintVTK(self, *args):
        return _mesh.Mesh_PrintVTK(self, *args)

    def GetElementColoring(self, colors, el0=0):
        return _mesh.Mesh_GetElementColoring(self, colors, el0)

    def PrintWithPartitioning(self, partitioning, out, elem_attr=0):
        return _mesh.Mesh_PrintWithPartitioning(self, partitioning, out, elem_attr)

    def PrintElementsWithPartitioning(self, partitioning, out, interior_faces=0):
        return _mesh.Mesh_PrintElementsWithPartitioning(self, partitioning, out, interior_faces)

    def PrintSurfaces(self, Aface_face, out):
        return _mesh.Mesh_PrintSurfaces(self, Aface_face, out)

    def ScaleSubdomains(self, sf):
        return _mesh.Mesh_ScaleSubdomains(self, sf)

    def ScaleElements(self, sf):
        return _mesh.Mesh_ScaleElements(self, sf)

    def Transform(self, *args):
        return _mesh.Mesh_Transform(self, *args)

    def RemoveUnusedVertices(self):
        return _mesh.Mesh_RemoveUnusedVertices(self)

    def RemoveInternalBoundaries(self):
        return _mesh.Mesh_RemoveInternalBoundaries(self)

    def GetElementSize(self, *args):
        return _mesh.Mesh_GetElementSize(self, *args)

    def GetElementVolume(self, i):
        return _mesh.Mesh_GetElementVolume(self, i)

    def GetBoundingBox(self, ref = 2):
        from  .vector import Vector
        min = Vector()
        max = Vector()      
        _mesh.Mesh_GetBoundingBox(self, min, max, ref)      
        return min.GetDataArray().copy(), max.GetDataArray().copy()



    def GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max, Vh=None, Vk=None):
        return _mesh.Mesh_GetCharacteristics(self, h_min, h_max, kappa_min, kappa_max, Vh, Vk)

    def PrintCharacteristics(self, *args):
        return _mesh.Mesh_PrintCharacteristics(self, *args)

    def PrintInfo(self, *args):
        return _mesh.Mesh_PrintInfo(self, *args)
    __swig_destroy__ = _mesh.delete_Mesh
    __del__ = lambda self: None

    def __init__(self, *args):
        this = _mesh.new_Mesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def PrintToFile(self, mesh_file, precision):
        return _mesh.Mesh_PrintToFile(self, mesh_file, precision)

    def GetAttributeArray(self):
        return _mesh.Mesh_GetAttributeArray(self)

    def GetVertexArray(self, i):
        return _mesh.Mesh_GetVertexArray(self, i)

    def GetBdrElementFace(self, *args):
        return _mesh.Mesh_GetBdrElementFace(self, *args)

    def GetBdrAttributeArray(self):
        return _mesh.Mesh_GetBdrAttributeArray(self)

    def GetBdrArray(self, idx):
        return _mesh.Mesh_GetBdrArray(self, idx)
Mesh_swigregister = _mesh.Mesh_swigregister
Mesh_swigregister(Mesh)

def Mesh_GetTransformationFEforElementType(arg2):
    return _mesh.Mesh_GetTransformationFEforElementType(arg2)
Mesh_GetTransformationFEforElementType = _mesh.Mesh_GetTransformationFEforElementType


def __lshift__(*args):
    return _mesh.__lshift__(*args)
__lshift__ = _mesh.__lshift__
class NodeExtrudeCoefficient(coefficient.VectorCoefficient):
    __swig_setmethods__ = {}
    for _s in [coefficient.VectorCoefficient]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NodeExtrudeCoefficient, name, value)
    __swig_getmethods__ = {}
    for _s in [coefficient.VectorCoefficient]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, NodeExtrudeCoefficient, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetLayer(self, l):
        return _mesh.NodeExtrudeCoefficient_SetLayer(self, l)

    def Eval(self, *args):
        return _mesh.NodeExtrudeCoefficient_Eval(self, *args)
    __swig_destroy__ = _mesh.delete_NodeExtrudeCoefficient
    __del__ = lambda self: None
NodeExtrudeCoefficient_swigregister = _mesh.NodeExtrudeCoefficient_swigregister
NodeExtrudeCoefficient_swigregister(NodeExtrudeCoefficient)


def Extrude1D(mesh, ny, sy, closed=False):
    return _mesh.Extrude1D(mesh, ny, sy, closed)
Extrude1D = _mesh.Extrude1D
class named_ifgzstream(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, named_ifgzstream, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, named_ifgzstream, name)
    __repr__ = _swig_repr
    __swig_setmethods__["filename"] = _mesh.named_ifgzstream_filename_set
    __swig_getmethods__["filename"] = _mesh.named_ifgzstream_filename_get
    if _newclass:
        filename = _swig_property(_mesh.named_ifgzstream_filename_get, _mesh.named_ifgzstream_filename_set)

    def __init__(self, mesh_name):
        this = _mesh.new_named_ifgzstream(mesh_name)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mesh.delete_named_ifgzstream
    __del__ = lambda self: None
named_ifgzstream_swigregister = _mesh.named_ifgzstream_swigregister
named_ifgzstream_swigregister(named_ifgzstream)

# This file is compatible with both classic and new-style classes.


