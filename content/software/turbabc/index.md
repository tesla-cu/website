+++
title = "turbABC"
summary = "Approximate Bayesian computation toolbox for turbulence model parameter estimation"

# Date first published.
date = "2020-01-01"

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["olga_doronina", "peter_hamlington"]

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
projects = ["turbulence_modeling"]
software = ["turbabc"]

# Links (optional).
url_pdf = "https://arxiv.org/abs/2005.13993"
url_preprint = ""
url_code = "https://github.com/olgadoronina/turbABC"
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
Approximate Bayesian Computation (ABC) is a data-driven approach, which uses experimental or higher fidelity data to
approximate the probability distribution of model parameters. ABC is based on the Bayesian approach but does not
require knowing the analytical expression for a likelihood function. The primary advantages of ABC are its lower
cost relative to full Bayesian methods and its flexibility in parameter estimation for complex models, e.g.,
turbulence models, which consist of partial differential equations.

[`turbABC`](https://github.com/olgadoronina/turbABC) combines ABC with Markov chain Monte Carlo (ABC-MCMC) sampling, an adaptive proposal, and calibration
steps to accelerate the parameter estimation process. It is extremely flexible and applicable to a
large suite of problems.
