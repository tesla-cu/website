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
publication_short = "Matem. Mod. (Russian)"

# Abstract and optional shortened version.
abstract = "We studied linear sound scattering by an isolated vortex to investigate the interaction of the vortex flow and acoustic waves. This problem is fundamental for understanding the process of sound generation by turbulence. We present numerical simulation results for a planar wave scattered by a Gaussian-core vortex and a cylindrical point source acoustic wave scattered by a Rankine vortex. For numerical simulation, we use the EBR scheme on grids of different types. We also compare our simulation results to different numerical approaches and the benchmark solution to test the EBR scheme's ability to model such problems on unstructured grids and assess its accuracy and efficiency compared to other approaches. The results confirm that NOISEtte and its numerical method can be successfully used to simulate the interaction between acoustic waves and vortex structures."
abstract_short = "We study linear sound scattering by an isolated vortex, namely, a planar wave scattered by a Gaussian-core vortex and a cylindrical point source acoustic wave scattered by a Rankine vortex. We compare the results of different numerical approaches and the benchmark solution. The results confirm that NOISEtte and its numerical method can be successfully used to simulate the interaction between acoustic waves and vortex structures."


# Featured image thumbnail (optional)
image_preview = ""

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
links = [ {name = "URL", url= "http://mi.mathnet.ru/eng/mm3403"}]

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
[header]
image = ""
caption = ""

+++
The problem of sound scattering by an isolated vortex is not only interesting to study, but it is also fundamental for understanding the interaction between acoustic waves and vortex flow, including the process of sound generation by turbulence. Understanding the sound generation process is essential for many practical applications.

When turbulence is represented by a distribution of localized vortices with certain static properties, the acoustic field scattered by such a flow is a superposition of scattered acoustic fields from each vortex. Therefore, the description of the elementary event of sound scattering sound by an isolated vortex can be used to predict the impact of turbulence on the acoustic field.

For the numerical simulation of this problem, we used a linear approximation of the mathematical model. This approximation is quite realistic because it reveals the main properties of the studied phenomena. Thus, we modeled the problem using a system of linearized Euler equations, in which a vortex is defined as a background field.

One of the goals of this study was to test the ability of the EBR (Edge-Based Reconstruction) numerical scheme to model considered problems on unstructured grids and to assess its accuracy and efficiency compared to other approaches. Thus, we used the EBR scheme (the fifth-order scheme based on the quasi-one-dimensional reconstruction), implemented in a highly parallel research code NOISEtte (KIAM RAS). 

First, we showed the simulation results of the plane acoustic wave scattering by isentropic Gaussian-core vortex with a constant circulation velocity. We also provided the study of grid convergence to the benchmark solution. Besides Cartesian grids, we used quasi-uniform unstructured triangular grids and demonstrated that the results are almost identical for the same number of grid points.

We also consider the problem of the cylindrical point source acoustic wave scattering by the Rankine vortex. We perform simulations on unstructured grids and compare the results of different numerical approaches: a finite-volume approach (NOISEtte EBR), a finite element approach (Actran DGM), and a finite-difference (Cabaret scheme).

The results confirm that NOISEtte and its numerical method can be successfully used to simulate the interaction between acoustic waves and vortex structures.