---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title: | 
        **Turbulence and Energy Systems Laboratory (TESLa)**
      subtitle: |
        **Paul M. Rady Department of Mechanical Engineering, University of Colorado, Boulder**
        {style="color: white"}
    design:
      columns: '1'
      background:
        image: 
          filename: /headers/Flatirons_Winter.jpg
          filters:
            brightness: 0.4
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ["50px", "0px", "10px", "0"]

  - block: portfolio
    id: projects
    content:
      title: Research Areas
      filters:
        folders:
          - project
    design:
      spacing:
        padding: ["25px", "100px", "25px", "100px"]

  - block: portfolio
    id: software
    content:
      title: Software
      filters:
        folders:
          - software
    design:
      spacing:
        padding: ["25px", "100px", "25px", "100px"]

  - block: people
    id: people
    content:
      user_groups:
        - Principal Investigator
        - Researchers
    design:
      show_interests: false
      spacing:
        padding: ["25px", "100px", "25px", "100px"]

  - block: collection
    id: publications
    content:
      title: Recent Publications
      count: 6
      filters:
        folders:
          - publication
      sort_by: 'Date'
      sort_ascending: false
      archive:
        enable: true
        text: SEE ALL PUBLICATIONS
        link: publication/
    design:
      view: 4
      columns: '2'
      spacing:
        padding: ["25px", "100px", "25px", "100px"]

  - block: markdown
    id: seminars
    content:
      title: Community
      text: |
        [Rocky Mountain Fluid Mechanics Research Symposium](http://rockymountainfluids.org)

        [Boulder Thermal Fluid Sciences Seminar Series](http://boulderfluidsseminar.org)
    design:
      columns: '2'
      spacing:
        padding: ["15px", "100px", "15px", "100px"]

  - block: contact
    id: contact
    content:
      title: Contact
      subtitle: ''
      text: ''
      # Contact details - edit or remove options as needed
      email: ""
      phone: (303) 492-0555
      appointment_url: ""
      address:
        street: 427 UCB, 1111 Engineering Dr
        city: Boulder
        region: CO
        postcode: '80309'
        country: United States
        country_code: US
      directions: TESLa is located in the Mechanical Engineering wing of the Engineering Center at the University of Colorado, Boulder. Peter Hamlington can be found in office ECME 177 and the student office is ECME 217.
      contact_links:
        - icon: twitter
          icon_pack: fab
          name: TESLa CU
          link: 'https://twitter.com/tesla_cu'
        # - icon: skype
        #   icon_pack: fab
        #   name: Skype Me
        #   link: 'skype:echo123?call'
        # - icon: video
        #   icon_pack: fas
        #   name: Zoom Me
        #   link: 'https://zoom.com'
      # Automatically link email and phone or display them just as text?
      autolink: true
      # Choose an email form provider (netlify/formspree)
      form:
        provider: netlify
        formspree:
          # If using Formspree, enter your Formspree form ID
          id: ''
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
      # Coordinates to display a map - set your map provider in `params.yaml`
      coordinates:
        latitude: '40.007617'
        longitude: '-105.263679'
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '2'
      spacing:
        padding: ["15px", "100px", "0px", "100px"]
---
