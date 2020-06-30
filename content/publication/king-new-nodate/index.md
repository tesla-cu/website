---
title: "A new autonomic closure for large eddy simulations"
date: 2016-01-01
publishDate: 2020-06-27T15:52:06.540479Z
authors: ["ryan_king", "peter_hamlington", "werner_dahm"]
publication_types: ["1"]
abstract: "We present a fundamentally new autonomic subgridscale closure for large eddy simulations (LES) that solves a nonlinear, nonparametric system identiﬁcation problem instead of using a predeﬁned turbulence model. The autonomic approach expresses the local SGS stress tensor as the most general unknown nonlinear function of the resolvedscale primitive variables at all locations and times using a Volterra series. This series is analogous to a Taylor series expansion in both time and space, and incorporates nonlinear, nonlocal, and nonequilibrium turbulence effects. The series introduces a large number of convolution kernel coefﬁcients that are found by solving an inverse problem to minimize the error in representing known subgrid-scale stresses at a test ﬁlter scale. The optimized coefﬁcients are then projected to the LES scale by invoking scale similarity in the inertial range and applying appropriate renormalizations. This new closure approach avoids the need to specify a turbulent constitutive model and instead identiﬁes an optimal model on the ﬂy. Here we present the most general formulation of the new autonomic approach and outline an inverse modeling method for optimizing the coefﬁcients. We then explore truncations of the series expansion and demonstrate the effects of regularization and sampling on the optimal coefﬁcients. Finally, we perform a priori tests of this approach using data from direct numerical simulations of homogeneous isotropic and sheared turbulence. We ﬁnd substantial improvements over the Dynamic Smagorinsky model, even for a 2nd order time-local truncation of the present closure."
featured: false
publication: ""
projects:
  - turbulence_modeling
---

