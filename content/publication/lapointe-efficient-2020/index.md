---
title: "Efficient simulation of turbulent diffusion flames in OpenFOAM using adaptive mesh refinement"
date: 2020-01-01
publishDate: 2020-06-27T15:52:06.526645Z
authors: ["caelan_lapointe", "nick_wimer", "jeff_glusman", "Amanda Makowiecki", "john_daily", "greg_rieker", "peter_hamlington"]
publication_types: ["2"]
abstract: "We address the challenge of resolving wide spatial scale ranges in fire simulations through the development of a new OpenFOAM-based adaptive mesh refinement (AMR) computational capability for large eddy simulations of turbulent diffusion flames. The AMR approach provides increased resolution in localized regions based on userdefined criteria, resulting in a simulation that dynamically tracks fire spread and reduces computational cost compared to uniform and static mesh approaches. The new AMR-enabled solver, called diffusionFireFoam, is an extension of the fireFoam solver and incorporates dynamic meshing capabilities already available in OpenFOAM. We outline details of the new solver and demonstrate its basic functionality, accuracy, and computational effi­ ciency for a small-scale methane pool fire verification case. We show that both first- and second-order statistics from the AMR simulation are in good agreement with results from a statically refined simulation that has the same fine-scale resolution, but a larger overall mesh. We then show for a larger-scale methane pool fire that an AMR simulation in diffusionFireFoam agrees with results from static mesh simulations, experiments, and prior computational studies. Once again, substantial computational savings are achieved, with roughly 5 times fewer grid cells in the AMR simulations than in prior static mesh simulations."
featured: false
publication: "*Fire Safety Journal*"
url_pdf: "https://linkinghub.elsevier.com/retrieve/pii/S0379711219303807"
doi: "10.1016/j.firesaf.2019.102934"
projects:
  - wildland_fire
  
software:
  - diffusionfirefoam
  - wildfirefoam
---

