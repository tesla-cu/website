---
title: "Optimization of wind plant layouts using an adjoint approach"
date: 2017-03-01
publishDate: 2020-06-27T15:52:06.516857Z
authors: ["ryan_king", "Katherine Dykes", "Peter Graf", "peter_hamlington"]
publication_types: ["2"]
abstract: "Using adjoint optimization and three-dimensional steady-state Reynolds-averaged Navier–Stokes (RANS) simulations, we present a new gradient-based approach for optimally siting wind turbines within utilityscale wind plants. By solving the adjoint equations of the ﬂow model, the gradients needed for optimization are found at a cost that is independent of the number of control variables, thereby permitting optimization of large wind plants with many turbine locations. Moreover, compared to the common approach of superimposing prescribed wake deﬁcits onto linearized ﬂow models, the computational efﬁciency of the adjoint approach allows the use of higher-ﬁdelity RANS ﬂow models which can capture nonlinear turbulent ﬂow physics within a wind plant. The steady-state RANS ﬂow model is implemented in the Python ﬁnite-element package FEniCS and the derivation and solution of the discrete adjoint equations are automated within the dolfin-adjoint framework. Gradient-based optimization of wind turbine locations is demonstrated for idealized test cases that reveal new optimization heuristics such as rotational symmetry, local speedups, and nonlinear wake curvature effects. Layout optimization is also demonstrated on more complex wind rose shapes, including a full annual energy production (AEP) layout optimization over 36 inﬂow directions and 5 wind speed bins."
featured: false
publication: "*Wind Energy Science*"
url_pdf: "https://wes.copernicus.org/articles/2/115/2017/"
doi: "10.5194/wes-2-115-2017"
projects:
  - wind_energy
---

