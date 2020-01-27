import bpy
from bpy.types import Operator

from bpy.props import BoolProperty

from . fsc_bool_util import *

class FSC_OT_Remesh_Operator(Operator):
    bl_idname = "object.fsc_remesh"
    bl_label = "Remesh"
    bl_description = "Voxel remesh operator" 
    bl_options = {'REGISTER', 'UNDO'}

    join_b4_remesh : BoolProperty(name="Join", options={'HIDDEN'}, default=False)

    def invoke(self, context, event):

        if self.join_b4_remesh:
            bpy.ops.object.join()

        execute_remesh(context) 
        return {'FINISHED'}