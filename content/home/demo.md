+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.
widget = "demo"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.

title = "**Turbulence and Energy Systems Laboratory (TESLa)**"
#subtitle = "Mechanical Engineering, University of Colorado, Boulder"

about = """Turbulence and Energy Systems Laboratory is the research lab in the
         Department of Mechanical Engineering at the University of Colorado,
         Boulder, led by Prof. Peter Hamlington. We study turbulence, combustion, 
         renewable energy systems, and geophysical flows."""
         
motivation = """The accurate prediction of turbulent flows using numerical simulations is the 
                fundamental challenge. Such simulations are critical for the design of efficient 
                propulsion systems, optimization of energy output and turbine lifespan in large-scale 
                wind farms, and reliable forecasting of the climate and weather."""
                
approach = """We use a range of simulation approaches to enable more accurate and reliable 
              large-scale simulations of propulsion, energy, and climate/weather problems. 
              DNS and LES are carried out to
              understand fundamental turbulent flow physics and insights from these
              studies are used to develop physics-based closures for LES and RANS simulations."""


[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
   columns = "1"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  # color = "navy"

  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"

  # Background image.
  image = "headers/turbulent_flames.png"  # Name of image in `static/img/`.
  image_darken = 0.4  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.
  image_size = "cover"  #  Options are `cover` (default), `contain`, or `actual` size.
  image_position = "center"  # Options include `left`, `center` (default), or `right`.
  image_parallax = false  # Use a fun parallax-like fixed background effect? true/false

  # Text color (true=light or false=dark).
  text_color_light = true

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS.
 css_style = ""

 # CSS class.
 css_class = ""
+++
