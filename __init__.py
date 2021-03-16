# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

bl_info = {
    "name" : "RLtoBlender",
    "author" : "BladeBTW",
    "description" : "Sync RL Camera to Blender Camera",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}


from . RLtoBlender_op import RLTOBLENDER_OT_Start_Socket_Connection_Op,HttpHandler,RLTOBLENDER_OT_Print_Data
from . RLtoBlender_pnl import RLTOBLENDER_PT_Panel

classes = (RLTOBLENDER_OT_Start_Socket_Connection_Op,RLTOBLENDER_PT_Panel,RLTOBLENDER_OT_Print_Data)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
