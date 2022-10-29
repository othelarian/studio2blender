import bpy

# select all empties and clear parent inverse

objs = bpy.context.scene.objects
for obj in objs:
    obj.select_set("dot_dat" in obj.name)
bpy.ops.object.parent_clear(type="CLEAR_INVERSE")

# select meshes and clear parent but keep transformation

for obj in objs:
    obj.select_set(obj.type == "MESH")
bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

# delete all empties

for obj in objs:
    obj.select_set("dot_dat" in obj.name or obj.name == "Model")
bpy.ops.object.delete(confirm=False)

# make single user for object & data

for obj in objs:
    obj.select_set(obj.type == "MESH")
bpy.ops.object.make_single_user(object=True, obdata=True)

# apply scale

bpy.ops.object.transform_apply(
    location=False,
    rotation=False,
    properties=False,
    isolate_users=True)

# select all vertices, merge by distance

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles()
bpy.ops.object.mode_set(mode='OBJECT')

# active normals auto smooth

sel_objs = bpy.context.selected_objects
for sel_obj in sel_objs:
    mesh = sel_obj.data
    mesh.use_auto_smooth = True
