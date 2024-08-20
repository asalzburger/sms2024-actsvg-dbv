import json
import actsvg
import os

# Opening JSON file
with open('../data/odd-sensitives.json') as json_file:
    # load the surface dictionary
    surfaces_dict = json.load(json_file)
    surfaces = surfaces_dict["entries"]
    
    print(">> Loaded   : ",len(surfaces),"surfaces")

    volumes = {}

    # Sets up the file structure
    if not os.path.isdir("svg"):
        os.makedirs("svg")

    for s in surfaces:
        volumes[s["volume"]] = {}

    for s in surfaces:
        volumes[s["volume"]][s["layer"]] = []

    for s in surfaces:
        volumes[s["volume"]][s["layer"]].append(s["sensitive"])
        if not os.path.isdir("svg/vol" + str(s["volume"])):
            os.makedirs("svg/vol" + str(s["volume"]))
        if not os.path.isdir("svg/vol" + str(s["volume"]) + "/lay" + str(s["layer"])):
            os.makedirs("svg/vol" + str(s["volume"]) + "/lay" + str(s["layer"]))

    

    # select all of a certain volume layer

    fill = actsvg.style.fill()
    stroke = actsvg.style.stroke()
    font = actsvg.style.font()

    for i in volumes:
        for j in volumes[i]:
            if i != 16 or j != 4:
                continue

            volume = i
            layer = j

            selected_surfaces = [ s for s in surfaces if s["volume"] == volume and s["layer"] == layer ]
            
            print(">> Selected : ",len(selected_surfaces),"surfaces for volume", volume, "and layer", layer)
            
            proto_surfaces = [ actsvg.json.read_surface(s) for s in selected_surfaces ]
            
            svg_surfaces = actsvg.display.surfaces(proto_surfaces, "xy")

            svg_file = actsvg.io.file()
            svg_file.add_objects(svg_surfaces)
            it = 0
            for s in selected_surfaces:
                info_box = actsvg.draw.connected_info_box("vol_" + str(i) + "_layer_" + str(j) + "_modules/_sen" + str(s["sensitive"]), [50.0,50.0], "", fill, font, [""], fill, font, stroke, svg_surfaces[it], ["mouseover", "mouseout"])
                svg_file.add_object(info_box)
                it+=1

                
            svg_file.write("svg/vol" + str(volume) + "/lay" + str(layer) + "/vol_"+str(volume)+"_layer_"+str(layer)+"_modules.svg")
                
            for k in volumes[i][j]: 
                # single surface
                sensitive = k
                single_surface = [ s for s in surfaces if s["volume"] == volume and s["layer"] == layer and s["sensitive"] == sensitive ]
                
                single_proto_surface = [ actsvg.json.read_surface(s, apply_transform=False) for s in single_surface ]
                
                svg_single_surface = actsvg.display.surfaces(single_proto_surface, "xy")
                
                
                svg_single_file = actsvg.io.file()
                svg_single_file.add_objects(svg_single_surface)

                info_box = actsvg.draw.connected_info_box("module_vol" + str(i) + "_lay" + str(j) + "_sen" + str(k), [50.0,50.0], "", fill, font, [""], fill, font, stroke, svg_single_surface[0], ["mouseover", "mouseout"])
                svg_single_file.add_object(info_box)

                
                svg_single_file.write("svg/vol" + str(volume) + "/lay" + str(layer) + "/volume"+str(volume)+"_layer"+str(layer)+"sensitive"+str(sensitive)+".svg")




"""
# Opening JSON file
with open('../json/odd-sensitives.json') as json_file:
    # load the surface dictionary
    surfaces_dict = json.load(json_file)
    surfaces = surfaces_dict["entries"]
    
    print(">> Loaded   : ",len(surfaces),"surfaces")
    
    vlm_dict = {}

    for i in range(len(surfaces)):
        vkey = surfaces[i]["volume"]
        vlm_dict[vkey] = {}

    for i in range(len(surfaces)):
        vkey = surfaces[i]["volume"]
        lkey = surfaces[i]["layer"]
        vlm_dict[vkey][lkey] = []
        
    for i in range(len(surfaces)):
        vkey = surfaces[i]["volume"]
        lkey = surfaces[i]["layer"]
        vlm_dict[vkey][lkey].append(surfaces[i]["sensitive"])

    for vol in vlm_dict:
        for lay in vlm_dict[vol]:
            # select all of a certain volume layer
            volume = vol
            layer = lay    

            if not os.path.isdir("svg/vol" + str(vol)):
                os.makedirs("svg/vol" + str(vol))

            if not os.path.isdir("svg/vol" + str(vol) + "/lay" + str(lay)):
                os.makedirs("svg/vol" + str(vol) + "/lay" + str(lay))

            selected_surfaces = [ s for s in surfaces if s["volume"] == volume and s["layer"] == layer ]
            
            print(">> Selected : ",len(selected_surfaces),"surfaces for volume", volume, "and layer", layer)
            
            proto_surfaces = [ actsvg.json.read_surface(s) for s in selected_surfaces ]
            
            svg_surfaces = actsvg.display.surfaces(proto_surfaces, "xy")
            
            svg_file = actsvg.io.file()
            svg_file.add_objects(svg_surfaces)
            svg_file.write("svg/vol" + str(vol) + "/lay" + str(lay) + "/volume"+str(volume)+"_layer"+str(layer)+".svg")

            for sen in vlm_dict[vkey][lkey]:
                sensitive = sen
                single_surface = [ s for s in surfaces if s["volume"] == volume and s["layer"] == layer and s["sensitive"] == sensitive ]
                
                single_proto_surface = [ actsvg.json.read_surface(s, apply_transform=False) for s in single_surface ]
                    
                svg_single_surface = actsvg.display.surfaces(single_proto_surface, "xy")
                
                svg_single_file = actsvg.io.file()
                svg_single_file.add_objects(svg_single_surface)
                svg_single_file.write("svg/vol" + str(vol) + "/lay" + str(lay) + "/volume"+str(volume)+"_layer"+str(layer)+"sensitive"+str(sensitive)+".svg")

                """