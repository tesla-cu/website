+++
title = "Numerical simulation of acoustic waves scattering by isolated vortex structures"

# Date first published.
date = "2013-03-01"

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["olga_doronina", "N. S. Zdanova"]

# Publication type.
# Legend:
# 0 = Uncategorized
# 1 = Conference proceedings
# 2 = Journal
# 3 = Work in progress
# 4 = Technical report
# 5 = Book
# 6 = Book chapter
publication_types = ["2"]

# Publication name and optional abbreviated version.
publication = "Matematicheskoe Modelirovanie"
publication_short = "Matem. Mod."

# Abstract and optional shortened version.
abstract = "We consider a linear sound scattering by an isolated vortex as one of the fundamental problems in order to investigate an interaction of the vortex flow and acoustic waves. We present numerical simulation results for a planar wave scattered by a Gaussian-core vortex and a cylindrical point source acoustic wave scattered by a Rankine vortex. For numerical simulation we use the EBR scheme on meshes of different types. We compare results to the benchmark solution and we also compare different approaches to numerical simulation of the problem."
abstract_short = ""

# Featured image thumbnail (optional)
image_preview = ""

# Links (optional).
url_pdf = "http://www.mathnet.ru/links/6c0221c724e477d42d3a23867c190774/mm3403.pdf"
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
links = [ {name = "Webpage", url= "http://mi.mathnet.ru/eng/mm3403"}]

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++
The problem of sound scattering by an isolated vortex  is of interest in itself and the basis for understanding the interaction between acoustic waves and a vortex flow, including the process of sound generation by turbulence.

In order to solve this problem we use the linearized Euler equations in the nonuniform average field, taking into account isoentropic medium. For numerical simulation, we also use a scheme based on the quasi-one-dimensional reconstruction of the 5th order of accuracy. Calculations are performed using the parallel research code NOISEtte (KIAM RAS).

We give the calculational results of the plane acoustic wave scattering by isoentropic Gaussian-core vortex of a constant velocity circulation and demonstrate the convergence of solutions to the benchmark solution. Unlike the other authors  results, not only Cartesian meshes, but quasi-uniform unstructured triangular meshes are also used. It is found that in both cases the results are almost the identical for the same number of nodes.

Further, we consider the problem of the cylindrical point source acoustic wave scattering by the Rankine vortex. We carry out the calculations on unstructured meshes and compare the results of different approaches to the problem: a finite-volume approach (NOISEtte), a finite element approach (Actran DGM) and a finite-difference Cabaret scheme.

In particular, the results confirm that the software system NOISEtte and the used method can be successfully applied to the numerical simulation of interaction between acoustic waves and vortex structures.
