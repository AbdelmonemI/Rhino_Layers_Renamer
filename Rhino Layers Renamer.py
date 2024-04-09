import rhinoscriptsyntax as rs

def rename_layers():
    layers = rs.LayerNames()
    base_name = "Layer"
    for i, layer in enumerate(layers):
        new_name = base_name + "_" + str(i + 1)
        rs.RenameLayer(layer, new_name)

rename_layers()