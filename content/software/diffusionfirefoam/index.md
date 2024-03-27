+++
title = "diffusionFireFoam"
summary = "OpenFOAM solver for diffusion flames using adaptive mesh refinement"

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
software = ["diffusionfirefoam"]

# Links (optional).
url_pdf = ""
url_preprint = ""
url_code = "https://github.com/clapointe2011/public"
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

diffusionFireFoam is an extension of fireFoam, an OpenFOAM solver for "...fires and turbulent diffusion flames with reacting particle clouds, surface film and pyrolysis modelling." It is a stripped-down version of fireFoam designed specifically for simulation of turbulent diffusion flames and  employs adaptive mesh refinement (AMR) to increase simualtion efficiency without sacrificing accuracy by updating the computational mesh at runtime and adding resolution only in regions of interest (e.g. where reactions are occuring). The solver has been shown to accurately reproduce results from static (i.e. time-invariant) simulaitons as well as experimental data.
