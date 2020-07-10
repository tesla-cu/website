+++
title = "wildFireFoam"
summary = "OpenFOAM solver for biomass diffusion flames using adaptive mesh refinement"

# Date first published.
date = "2020-01-01"

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["caelan_lapointe", "peter_hamlington"]

# Abstract and optional shortened version.
abstract = ""
abstract_short = ""

# Featured image thumbnail (optional)
image_preview = ""

# Is this a selected publication? (true/false)
selected = false

# Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter the filename (excluding '.md') of your project file in `content/project/`.
#   E.g. `projects = ["deep-learning"]` references `content/project/deep-learning.md`.
projects = ["wildland_fire"]
software = ["wildfirefoam"]

# Links (optional).
url_pdf = ""
url_preprint = ""
url_code = ""
url_dataset = ""
url_project = ""
url_slides = ""
url_video = ""
url_poster = ""
url_source = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom = [{name = "Custom Link", url = "http://example.org"}]

# Does the content use math formatting?
math = true

# Does the content use source code highlighting?
highlight = true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++
wildFireFoam is an extension of fireFoam, an OpenFOAM solver for "...fires and turbulent diffusion flames with reacting particle clouds, surface film and pyrolysis modelling." It retains all functionality originally included in fireFoam for efficient simulation of complex fire phenomena. Similar to diffusionFireFoam, it also incorporates  adaptive mesh refinement (AMR) to increase simualtion efficiency without sacrificing accuracy by updating the computational mesh at runtime and adding resolution only in regions of interest (e.g. where reactions are occuring). It has been designed specifically to reduce computational cost of fire spread and suppression simulations for use in outer-loop processes (e.g. optimization and uncertainty quantification).
