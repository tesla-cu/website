---
title: Industrial systems
summary: Modeling and optimization of real-world engineering and industrial systems
tags:
- LES
- RANS
- Optimization

# date: "2016-04-27T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: 
  focal_point: Smart

#links:
#- icon: twitter
#  icon_pack: fab
#  name: Follow
#  url: https://twitter.com/georgecushen
# url_code: "https://github.com/olgadoronina/ABC_MCMC"
# url_pdf: ""
# url_slides: ""
# url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example

authors:
  - sam_simons_wellin
  - caelan_lapointe
  - peter_hamlington

---

With Prof. Greg Rieker at CU, we have performed joint experimental and computational research on catalytic and ribbon burners used for industrial processing of polymer films on chilled rollers. On the computational side, we have developed a simulation testbed in OpenFOAM for the study of temperature, flow fields, and heat transfer processes (i.e., radiation and convection) above the burner and in the burner/roller interaction region. The simulation tool has been used to examine a wide range of conditions, including different roller speeds, burner/roller spacings, burner orientations, and power fluxes. Burners operating in isolation and as part of a larger array have also been studied. Simulations have provided 3D temperature, flow, and heat transfer fields for each of these cases, revealing several useful design heuristics, including the advantage of a down-firing burner configuration, the negative impacts of convective heat transfer on temperature uniformity, and the advantageous effects on uniformity of flow-blocking by the roller.

Approximate Bayesian computation (ABC) is a data-driven technique that uses many low-cost numerical simulations to estimate unknown physical or model parameters (e.g., boundary conditions and material properties), as well as their uncertainties, given reference data from real-world experiments or higher-fidelity numerical simulations. We have used ABC to estimate unknown parameters in simulations of complex thermal-fluid flows, and the technique has been demonstrated for the estimation of unknown boundary conditions in experiments of high temperature burners used for polymer film flame treatments. These tests show that ABC provides accurate and reasonably certain estimates of inflow parameters even when the model simulations imperfectly represent the physics underlying the reference experimental data. We also demonstrate the use of ABC to estimate unknown model parameters in large eddy simulations and Reynolds averaged Navier-Stokes simulations of turbulent flows. ABC is thus shown to be a versatile technique for estimating unknown physical and model parameters, resulting in substantial improvements in simulation accuracy. 