+++
title = "amrPOD"
summary = "Proper orthogonal decomposition of data from adaptive mesh refinement simulations"

# Date first published.
date = "2020-01-01"

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["michael_meehan", "sam_simons_wellin", "peter_hamlington"]

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
# projects = ["openfoam"]
software = ["amrpod"]

# Links (optional).
url_pdf = ""
url_preprint = ""
url_code = "https://github.com/tesla-cu/amrPOD"
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

Adaptive mesh refinement (AMR) plays a fundamental role in simulating particular flow phenomena that have vastly different resolution requirements throughout the computational domain. Proper orthogonal decomposition (POD), on the other hand, serves as a popular tool to extract coherent structures from the fluid data and build reduced order models. We present a new method to perform POD on AMR data sets that eliminates repeated operations that arise from using nearest neighbor interpolation of the data onto a uniform grid before performing POD. More fundamentally, we believe that this is the first algorithm to eliminate redundant operations for matrix multiplications with repeated values in each matrix.

We provide all code [here](https://github.com/tesla-cu/amrPOD) for `amrPOD` to evaluate the efficiency of the algorithm as shown in the [paper](https://github.com/tesla-cu/amrPOD). Specifically, we stress the algorithm using synthetically generated AMR data to identify where the new algorithm out performs standard matrix operations since the new algorithm requires additional overhead of checking the grid level at various locations. Additionally, we show with genuine AMR data of an axisymmetric buoyant jet and a compiled and optimized version of the code, our algorithm reduces the CPU time. Details of how to use the code are provided in the `README.md` on [github](https://github.com/tesla-cu/amrPOD).
