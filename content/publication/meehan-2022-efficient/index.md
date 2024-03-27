---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: Efficient algorithm for proper orthogonal decomposition of block-structured
  adaptively refined numerical simulations
subtitle: ''
summary: ''
authors:
- michael_meehan
- sam_simons_wellin
- peter_hamlington
tags: []
categories: []
date: '2022-08-18'
lastmod: 2023-01-22T09:50:26-07:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-01-22T16:50:26.598672Z'
publication_types:
- '2'
abstract: 'Adaptive mesh refinement (AMR) is increasingly being used to simulate fluid flows that have vastly different resolution requirements throughout the computational domain. Proper orthogonal decomposition (POD) is a common tool to extract coherent structures from flow data and build reduced order models, but current POD algorithms do not take advantage of potential efficiency gains enabled by multi-resolution data from AMR simulations. Here, we explore a new method for performing POD on AMR data that eliminates repeated operations arising from nearest-neighbor interpolation of multi-resolution data onto uniform grids. We first outline our approach to reduce the number of computations with examples and provide the complete algorithms in the appendix. We examine the computational acceleration of the new algorithms compared to the standard POD method using synthetically generated AMR data and operation counting. We then use CPU times and operation counting to analyze data from an AMR simulation of an axisymmetric buoyant plume, finding that we are able to reduce the computational time by a factor of approximately 2 − 5 when using three levels of grid refinement. The new POD algorithm is the first to eliminate redundant operations for matrix multiplications with repeated values in each matrix, making it ideal for POD of data from AMR simulations.'
publication: '*Journal of Computational Physics*'
url_pdf: "https://pdf.sciencedirectassets.com/272570/1-s2.0-S0021999122X00193/1-s2.0-S0021999122005897/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLWVhc3QtMSJHMEUCIQDAjojG3XEUL2Jr92XsSf70vtmZV%2BGA8lVlo2z2RDyBnAIgcVeNOIiV3pZ4BJfeh2ztJqH1kg3nlLNQTXSNuV9Q6ogq1QQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAFGgwwNTkwMDM1NDY4NjUiDJ%2B0x8ZW4eO7YQr%2FziqpBLb6UeoIGvzfNcSYL%2BIc9Qo8wnfDa5xQ%2BLfAkkfHYg7pHIIicE60s0YzsS4c95DUmzrmBJD7RPqTseZXoXWLevINpcEHwv4Kovov5cDp69kbSvnWMMN1RiZVSOi2LnKEvvKHHQc%2F61Khb%2FtlIweWpnWCMO7xenkg%2FnoeEA03SNyY61lfUl6mtbExqVhFSgRgqV1mUzJgL19jtoVhoufn5%2FRsnqWK0lyOxXvWUEMuQOtZN810%2BKsK%2FoCJq3mqOoca6BWkackjzgTJZDkjjB3N5eTE87YqVOHtSyuioNBeLpKnb8LAhIQejp%2BjPFaRZ2A5m63nv1so5Tzj0YJTQy%2BIOQcyZ%2FMgZ0S7UpCFAvvmfT%2B2zE853tm%2ByPprLuuNcAA6zIXLIstqyIXIjT3XxEh3jlFGklia9K%2FMywH8wziZEkpozt0aDE%2BNfQjm%2Fp6o6opCUdOi%2FMKW1WezQRSiSrxdWUZryDCaLIy0spow02RwKdugi7YsEMCpih3uN1KarDVbY0J1pnZY3tKjNWkovO%2BiQIT1BK3I4IznLgVAUnRz3y%2FlB7F81o5bybz7By0YDkmGa2CG4bSJNEt3b9%2FKPQGlL3P5LvSPQbbSD%2B6wrCQ%2FzYGdxvxqBjizlXpLD0pDX228w3xhUCJ4q3B6JHhNfWdxdpcaeP4X%2Bk%2BHPGxnFLu1SDQ9EHNeIOt4dN1yj%2FkbV5Q5gvwEFen7nqK5E3hN%2B9CFWCoSHVYikH1ux2ow66%2B1ngY6qQGf%2BlHMrzoXpKPZgN%2FSvDt9HCXcFexHCTJFSD%2FgyTMgWBy0zmV6gM9PMUBhmYT2iaoNzSoy4W6db4FeojBfdRZ5sS0SBKKRUddYc7qQbjEqS6KLyYu9O7ybPj5CqJuMvGwUXvx4gzeAsABjGw%2BGSIGSns94eF54fghwXde99%2BxcLeZCrRBHgxTfzw4Quz1F6crPB%2BdDEHrscv8KVMEaKclT0TnCraf9c5LN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230122T165937Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYS4LDHAUR%2F20230122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=c1c429bff4dd8cad8a23c84e405b13748c21f84f22eb87cf2d155fd1c0809a38&hash=2ba923cab72859c6a66a9546594a587c8cfda197feb1e618ab8126697c5438e3&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0021999122005897&tid=spdf-b1c18cae-0db8-4d84-8abb-89523bf9e4ff&sid=de847fbc7ec1f94f7e9bcf38c405d42d9ea3gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=1014515b06580b575a50&rr=78d9d757aecf1f34&cc=us"
doi: "10.1016/j.jcp.2022.111527"

software:
- amrPOD
---
