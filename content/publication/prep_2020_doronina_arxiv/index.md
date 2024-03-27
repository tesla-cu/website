---
title: "Parameter Estimation for Subgrid-Scale Models Using Markov Chain Monte Carlo Approximate Bayesian Computation"
date: "2020-01-01"
authors:
  - olga_doronina
  - colin_towery
  - peter_hamlington

# Publication type.
# Legend:
# 0 = Uncategorized
# 1 = Conference proceedings
# 2 = Journal
# 3 = Work in progress
# 4 = Technical report
# 5 = Book
# 6 = Book chapter
publication_types: ["3"]

# Publication name and optional abbreviated version.
publication: "arXiv"
publication_short: "arXiv"

# Abstract and optional shortened version.
abstract: "We use approximate Bayesian computation (ABC) combined with an “improved” Markov chain Monte Carlo (IMCMC) method to estimate posterior distributions of model parameters in subgrid-scale (SGS) closures for large eddy simulations (LES) of turbulent flows. The ABC-IMCMC approach avoids the need to directly compute a likelihood function during the parameter estimation, enabling a substantial speed-up and greater flexibility as compared to full Bayesian approaches. The method also naturally provides uncertainties in parameter estimates, avoiding the artificial certainty implied by many optimization methods for determining model parameters. In this study, we outline details of the present ABC-IMCMC approach, including the use of an adaptive proposal and a calibration step to accelerate the parameter estimation process. We demonstrate the approach by estimating parameters in two nonlinear SGS closures using reference data from direct numerical simulations of homogeneous isotropic turbulence. We show that the resulting parameter values give excellent agreement with reference probability density functions of the SGS stress and kinetic energy production rate in a priori tests, while also providing stable solutions in forward LES (i.e., a posteriori tests) for homogeneous isotropic turbulence. The ABC-IMCMC method is thus shown to be an effective and efficient approach for estimating unknown parameters, including their uncertainties, in SGS closure models for LES of turbulent flows."
abstract_short: ""

projects:
  - turbulence_modeling

software: 
    - turbabc

# Links (optional).
#- name: Custom Link
#  url: http://example.org
url_pdf: "https://arxiv.org/pdf/2005.13993.pdf"
#url_preprint: ""
#url_code: ""
#url_dataset: = ""
#url_project: = ""
#url_slides: = ""
#url_video: ""
#url_poster: ""
#url_source: ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom:[{name = "Custom Link", url = "http://example.org"}]

# Does the content use math formatting?
math: true
# Does the content use source code highlighting?
highlight: true

#tags:
#- Source Themes
featured: true

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
# focal_point: ""
# preview_only: false

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""

---
