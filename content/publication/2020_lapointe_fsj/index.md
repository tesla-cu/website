---
title: "Efficient simulation of turbulent diffusion flames in OpenFOAM using adaptive mesh refinement"

date: "2019-10-28"
doi: "https://doi.org/10.1016/j.firesaf.2019.102934"
authors:
  - caelan_lapointe
  - nick_wimer
  - jeff_glusman
  - Amanda S. Makowiecki
  - John W. Daily
  - Gregory B. Rieker
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
publication_types: ["2"]

# Publication name and optional abbreviated version.
publication: "Fire Safety Journal"
publication_short: "Fire Safety Journal"

# Abstract and optional shortened version.
abstract: "We address the challenge of resolving wide spatial scale ranges in fire simulations through the development of a new OpenFOAM-based adaptive mesh refinement (AMR) computational capability for large eddy simulations of turbulent diffusion flames. The AMR approach provides increased resolution in localized regions based on user- defined criteria, resulting in a simulation that dynamically tracks fire spread and reduces computational cost compared to uniform and static mesh approaches. The new AMR-enabled solver, called diffusionFireFoam, is an extension of the fireFoam solver and incorporates dynamic meshing capabilities already available in OpenFOAM. We outline details of the new solver and demonstrate its basic functionality, accuracy, and computational effi- ciency for a small-scale methane pool fire verification case. We show that both first- and second-order statistics from the AMR simulation are in good agreement with results from a statically refined simulation that has the same fine-scale resolution, but a larger overall mesh. We then show for a larger-scale methane pool fire that an AMR simulation in diffusionFireFoam agrees with results from static mesh simulations, experiments, and prior computational studies. Once again, substantial computational savings are achieved, with roughly 5 times fewer grid cells in the AMR simulations than in prior static mesh simulations."
abstract_short: ""

projects:
  - wildland_fire

# Links (optional).
#- name: Custom Link
#  url: http://example.org
# url_pdf: ""
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

#tags:
#- Source Themes

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#  focal_point: ""
#  preview_only: false

---
