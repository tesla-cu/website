---
title: Wind energy
summary: Optimization and control of wind plants using high-fidelity simulations
tags:
- Optimization
- UQ 
- RANS

# date: "2016-04-27T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Photo by rawpixel on Unsplash
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
  - julian_quick
  - peter_hamlington
---

Using adjoint optimization and three-dimensional Reynolds-averaged Navier Stokes (RANS) simulations, we developed a new gradient-based approach for optimally siting wind turbines within utility-scale wind plants. By solving the adjoint equations of the flow model, the gradients needed for optimization were found at a cost that was independent of the number of control variables, thereby permitting optimization of large wind plants with many turbine locations. Moreover, compared to the common approach of superimposing prescribed wake deficits onto linearized flow models, the computational efficiency of the adjoint approach allowed the use of higher-fidelity RANS flow models that can capture nonlinear turbulent flow physics within a wind plant. The RANS flow model was implemented in the Python finite element package FEniCS and the derivation of the adjoint equations was automated within the dolfin-adjoint framework. Layout optimization was demonstrated for complex wind roses, including a full annual energy production (AEP) layout optimization over 36 inflow directions and 5 windspeed bins.

