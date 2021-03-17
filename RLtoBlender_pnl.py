import bpy

from bpy.types import Panel

class RLTOBLENDER_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "RLtoBlender Options"
    bl_category = "RLtoBlender Util"

    def draw(self, context):
        
        layout = self.layout

        # 2 Colums with buttons
        row = layout.row()
        col = row.column()
        col.operator("generic.start_socket_connection", text="Toggle RL Connection")

        # col = row.column()
        # col.operator("generic.stop_socket_connection", text="Toggle RL Connection")

        row = layout.row()
        col = row.column()
        col.operator("generic.print_data", text="Print Data")

        # col = row.column()
        # col.operator("generic.link_cam", text="Stop Cam Link")