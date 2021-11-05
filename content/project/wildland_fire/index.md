---
title: Fire dynamics
summary: High-fidelity simulations of fire in both natural and built environments
tags:
- Turbulence

# date: "2016-04-27T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: 
  focal_point: Smart

links:
#- icon: twitter
#  icon_pack: fab
#  name: Follow
#  url: https://twitter.com/georgecushen
# url_code: "https://github.com/olgadoronina/ABC_MCMC"
#url_pdf: ""
#url_slides: ""
#url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example

authors:
- caelan_lapointe
- jeff_glusman
- prakriti_sardana
- peter_hamlington

---

Novel computational techniques are required to offset the cost of high-fidelity simulations of fire in both built and natural environments. Such fires are nearly always distinguished by wide ranges of spatiotemporal scales and physical phenomena, thus placing considerable constraints on the achievable size and complexity of simulations. We have made new progress in using a well-known technique – Adaptive Mesh Refinement (AMR) – to overcome these limitations. With AMR, grid cells are placed only where they are needed to resolve large gradients in velocity, temperature, species, and other user-defined flow quantities. We demonstrate the use of an AMR-enabled FireFOAM solver for simulations of pool fires, and compare simulation results with experimental data and prior computational efforts. Capabilities of the new solver are outlined, with a view towards providing this tool, once completed, to the broader fire modeling community. We also highlight the potential of AMR to enable future direct numerical simulations (DNS) of fire dynamics, in particular using the multi-physics code PeleLM. Such simulations will provide some of the highest-fidelity predictions of fire dynamics to date, and will be made possible through the use of AMR to minimize the computational cost that typically accompanies DNS.  