import json
import actsvg
import os

import actHTMLCSS

from actHTMLCSS.actHTMLCSS import createOutputDirectory


path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

# Opening JSON file
with open(os.path.join(path, 'data', 'odd-sensitives.json')) as json_file:
    # load the surface dictionary
    surfaces_dict = json.load(json_file)
    surfaces = surfaces_dict["entries"]
    
    print(">> Loaded   : ",len(surfaces),"surfaces")

    volumes = {}

    svg_path = os.path.join(createOutputDirectory(path), "svg")

    # Sets up the file structure
    if not os.path.isdir(svg_path):
        os.makedirs(svg_path)

    for s in surfaces:
        volumes[s["volume"]] = {}

    for s in surfaces:
        volumes[s["volume"]][s["layer"]] = []

    for s in surfaces:
        volumes[s["volume"]][s["layer"]].append(s["sensitive"])
        if not os.path.isdir(os.path.join(svg_path, "vol" + str(s["volume"]))):
            os.makedirs(os.path.join(svg_path, "vol" + str(s["volume"])))
        if not os.path.isdir(os.path.join(svg_path, "vol" + str(s["volume"]), "lay" + str(s["layer"]))):
            os.makedirs(os.path.join(svg_path, "vol" + str(s["volume"]), "lay" + str(s["layer"])))

    

    # select all of a certain volume layer

    fill = actsvg.style.fill()
    stroke = actsvg.style.stroke()
    font = actsvg.style.font()

    for i in volumes:
        for j in volumes[i]:

            volume = i
            layer = j

            selected_surfaces = [ s for s in surfaces if s["volume"] == volume and s["layer"] == layer ]
            
            print(">> Selected : ",len(selected_surfaces),"surfaces for volume", volume, "and layer", layer)
            
            proto_surfaces = [ actsvg.json.read_surface(s) for s in selected_surfaces ]
            
            svg_surfaces = actsvg.display.surfaces(proto_surfaces, "xy")

            svg_file = actsvg.io.file()
            svg_file.add_objects(svg_surfaces)
            it = 0
            onerror_string = "this.onerror=null;this.href.baseVal='../../../../src/NoPull.png';"
            for s in selected_surfaces:
                id_string = "vol_" + str(i) + "_layer_" + str(j) + "_modules/_sen" + str(s["sensitive"])
                href_string = "../../../css/img/" + id_string + ".png"
                image_box = actsvg.draw.image_box(id_string, href_string, "300", "300", "180", "-26", svg_surfaces[it], ["mouseover", "mouseout"], onerror_string)
                svg_file.add_object(image_box)
                it+=1

                
            svg_file.write(os.path.join(svg_path, "vol" + str(volume), "lay" + str(layer), "vol_"+str(volume)+"_layer_"+str(layer)+"_modules.svg"))
                
            for k in volumes[i][j]: 
                # single surface
                sensitive = k
                single_surface = [ s for s in surfaces if s["volume"] == volume and s["layer"] == layer and s["sensitive"] == sensitive ]
                
                single_proto_surface = [ actsvg.json.read_surface(s, apply_transform=False) for s in single_surface ]
                
                svg_single_surface = actsvg.display.surfaces(single_proto_surface, "xy")
                
                
                svg_single_file = actsvg.io.file()
                svg_single_file.add_objects(svg_single_surface)

                id_string = "module_vol" + str(i) + "_lay" + str(j) + "_sen" + str(k)
                href_string = "../../../css/img/" + id_string + ".png"

                image_box = actsvg.draw.image_box(id_string, href_string, "300", "300", "180", "-26", svg_single_surface[0], ["mouseover", "mouseout"], onerror_string)
                svg_single_file.add_object(image_box)

                
                svg_single_file.write(os.path.join(svg_path, "vol" + str(volume), "lay" + str(layer), "volume"+str(volume)+"_layer"+str(layer)+"sensitive"+str(sensitive)+".svg"))