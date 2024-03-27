+++
title = "BFM17"
summary = "Reduced order upper ocean biogeochemical flux model with 17 state variables"

# Date first published.
date = "2020-01-01"

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["katherine_smith", "skyler_kern", "peter_hamlington", "marco_zavatarelli", "nadia_pinardi"]

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
projects = ["ocean_biogeochemistry"]
software = ["bfm17"]

# Links (optional).
url_pdf = ""
url_preprint = "https://gmd.copernicus.org/preprints/gmd-2020-134/"
url_code = "https://github.com/marco-zavatarelli/BFM17-56"
url_dataset = "http://doi.org/10.5281/zenodo.3840562"
url_project = ""
url_slides = ""
url_video = ""
url_poster = ""
url_source = ""

# Custom links (optional).
# Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
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

The Biogeochemical Flux Model (BFM) is a computational model of biological and chemical oceanographic processes. BFM is able to track dissolved organic matter, particulate organic matter, nutrients, dissolved gases, and various phytoplankton and zooplankton groups. The full BFM has 56 state variables and therefore is referred to as BFM56. The model includes a bacteria group, 2 microzooplankton groups, 2 mesozooplankton groups, and 4 phytoplankton groups. In an effort to study the effects of upper ocean turbulence on the biogeochemical processes, we would like to couple BFM with a large-eddy simulation (LES) code. BFM56 is too large to be coupled to a LES model for process studies of small scale ocean dynamics. A lighter model needed to be developed for future work.

 A reduced model has been produced by simplifying BFM56 to 17 state variables, and is therefore called BFM17. The reduced model has only 1 generic zooplankton group and 1 generic phytoplankton group. BFM17 eliminated the bacteria group by assuming constant remineralization rates between the detritus and nutrients.

BFM has been coupled to a one-dimensional version of the Princeton Ocean Model (POM1D). POM1D is used to simulate a column of water through time. It can be run in prognostic mode or diagnostic mode. Prognostic mode simulates all of the dynamics of a water column, while diagnostic mode can be used to force the physics with prescribed temperature and salinity profiles.

The code, available at the git repository linked above, has both BFM56 and BFM17 run options with POM1D. The code has been set up to model phytoplankton bloom dynamics at the Sargasso Sea. POM1D is being run in diagnostic mode using data from the Bermuda Atlantic Time-series and the Bermuda Testbed Mooring to prescribe temperature, salinity, and boundary conditions. BFM56 and BFM17 have been shown in previous work to produce comparable results.
