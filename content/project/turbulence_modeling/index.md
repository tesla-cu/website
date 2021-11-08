---
title: Turbulent flows
summary: Studies of turbulence physics for model development and calibration
tags:
- ABC
- LES
- RANS
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
# url_code: "https://github.com/olgadoronina/turbABC"
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
    - olga_doronina
    - julian_quick
    - peter_hamlington


collaborators:
    - "Scott Murman"
    - "Ryan King"
    - "Werner J.A. Dahm"

---

## Turbulence model development using Approximate Bayesian Computation

Real-world turbulent flows are challenging to simulate due to the high computational cost of resolving all their relevant spatial and temporal scales. There are two common approaches to reduce the cost of such simulations:

- [Large-Eddy Simulations (LES)](https://en.wikipedia.org/wiki/Large_eddy_simulation), which directly resolve turbulence on large scales and use subgrid-scale (SGS) models to represent small-scale physics

- [Reynolds averaged Navier-Stokes (RANS)](https://en.wikipedia.org/wiki/Reynolds-averaged_Navier%E2%80%93Stokes_equations) approaches, which resolve only averaged quantities and model turbulent fluctuations

However, there is no universally accurate turbulence model in either of these approaches. Besides that, all models rely on empirical coefficients that we must calibrate for different flows and geometries.

We suggest using the [Approximate Bayesian Computation (ABC)](https://en.wikipedia.org/wiki/Approximate_Bayesian_computation) methods, also known as likelihood-free methods. ABC is a data-driven approach, which uses experimental or higher fidelity data to approximate the probability distribution of model parameters. As a result, we can choose model parameters and quantify their uncertainty based on (or even sample from) this estimated probability distribution.

ABC is based on the Bayesian approach but does not require knowing the analytical expression for a likelihood function. The primary advantages of ABC are its lower cost relative to full Bayesian methods and its flexibility in parameter estimation for complex models, e.g., turbulence models, which consist of partial differential equations.

We created a framework called [turbABC](https://github.com/olgadoronina/turbABC) for turbulent model parameters estimation.  TurbABC combines ABC with Markov chain Monte Carlo (MCMC) sampling, an adaptive proposal, and calibration steps to accelerate the parameter estimation process. We demonstrate the efficiency and effectiveness of TurbABC by estimating parameters of:

- nonlinear SGS closures using reference data from direct numerical simulations of homogeneous isotropic turbulence

- nonequilibrium anisotropy RANS closure in homogeneous turbulent flow with rapidly changing strain tensor

- RANS model parameters estimation in inhomogeneous turbulent flow (axisymmetric transonic bump)
