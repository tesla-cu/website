---
title: "Lagrangian analysis of high-speed turbulent premixed reacting flows: Thermochemical trajectories in hydrogen–air flames"

# Date first published.
date: "2019-10-28"
doi: "https://doi.org/10.1016/j.jcp.2019.109054"
# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors:
  - Y. Kozak
  - S. S. Dammati
  - L. G. Bravo 
  -  peter_hamlington
  - Alexei Y. Poludnenko

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
publication: "Journal of Computational Physics"
publication_short: "J. Comput. Phys."

# Abstract and optional shortened version.
abstract: "Lagrangian particles can be used either to analyze different complex flows, as massless tracers, or to model multiphase flows, as particles with mass. As particles can have arbitrary positions within the computational domain, interpolation of different flow quantities from the Eulerian grid is essential. Low-order centered interpolation schemes generally do not provide a sufficient level of accuracy for many flow configurations of interest. Thus, typically, high-order centered interpolation schemes are utilized. The current study demonstrates that for highly compressible non-reacting and reacting flow regimes, in which discontinuities in the flow field, e.g., shock waves arise, centered interpolation schemes tend to smear the shock and high order schemes also produce numerical oscillations. It is shown that this problem can be remedied by using Weighted- Essentially-Non-Oscillatory (WENO) interpolation schemes. Extensive numerical tests are performed in order to demonstrate this, comparing the performance of WENO-3 and WENO-5 interpolation schemes with a variety of centered interpolation schemes. The first test case involves specially designed steady state two-dimensional vortex flows. For a smooth flow, WENO schemes provide comparable accuracy to other high-order centered schemes. For flow fields with discontinuities, WENO-3 and WENO-5 interpolation schemes can decrease the interpolation error by more than two and three orders of magnitude, respectively, in comparison with centered schemes. Solution accuracy is further studied with a normal shock wave test. It is demonstrated that centered schemes tend to smear the shock, whereas, WENO schemes capture it in a much sharper manner. Moreover, high-order centered schemes tend to oscillate in the vicinity of the discontinuity leading to non- physical results, such as negative absolute pressure values. The same trends are retained for an unsteady three-dimensional spherical blast wave, where the shock is smeared across several grid cells, which is typical for shock-capturing flow solvers. Finally, the benefits of WENO schemes for the Lagrangian-particle tracking analysis of highly compressible reactive flows are explored by comparing various Lagrangian particle trajectories and joint probability density functions (PDFs) for a two-dimensional cellular detonation. The results indicate that high-order centered schemes lead to unphysical results, whereas WENO schemes can provide high-order interpolation that is free of severe numerical oscillations and non-physical artifacts, which is critical for the proper analysis of the flow."
abstract_short: ""

projects:
    - "turbulent_combustion"

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
