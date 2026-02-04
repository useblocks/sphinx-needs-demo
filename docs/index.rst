.. Sphinx-Needs Demo documentation master file, created by
   sphinx-quickstart on Mon Feb 12 16:32:39 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx-Needs Demo
=================

This is a demo documentation for showing the features of `Sphinx-Needs <https://sphinx-needs.readthedocs.io/en/latest/>`__.

.. image:: /_images/sphinx-needs-logo-bg.png
   :align: center
   :width: 75%

.. grid:: 1 1 2 2

   .. grid-item::
      :columns: 12 12 8 8

      A simple Automotive SW project is used as playground, with elements
      for:

      * Requirements
      * Specifications
      * Implementations
      * Test Cases
      * and Test Results

   .. grid-item::
      :columns: 12 12 4 4

      .. button-link:: https://gitpod.io/#https://github.com/useblocks/sphinx-needs-demo
         :color: primary
         :shadow:

         Open this playground in Gitpod Online Editor!

      .. button-link:: https://codespaces.new/useblocks/sphinx-needs-demo/
         :color: primary
         :shadow:

         Open this playground in GitHub Codespaces!

Architecture diagrams get described by PlantUML.

There are also Dashboard pages to show specific information for
different process roles.

The complete source code can be found here: https://github.com/useblocks/sphinx-needs-demo

Features and technical details are described inside dropdowns like
this one:

.. tip:: Really, this is just an example. Nothing more.
   :title: Demo feature hint: Just an example
   :collapsible:

Demo Content
------------

Most of the need content was created using AI. Also most of the images
were generated this way.

However, all the meta-data, configuration, and analysis were set by
hand, so that the setup shows examples of a real-world use cases and
solutions.

GitPod Demo playground
----------------------

This Demo includes also a specialized docs-as-code setup for a Gitpod
online IDE.

You can open it by simply clicking this link: `Gitpod Sphinx-Needs-Demo IDE <gitpod.io/#https://github.com/useblocks/sphinx-needs-demo>`__.

A login with a Gitpod or GitHub account is needed. After this, you can
use the online IDE for 50 hours per month for free.

The Gitpod IDE provides the following features:

* Automatical clone of the requested repository
* Starting a selected docker container and using it as the build
  environment
* Install all needed Python dependencies (Sphinx + extensions)
* Load preconfigured VS Code extensions (Restructured text support,
  Esbonio, Previewer)
* Launch configuration to build the Sphinx demo project

Codespaces Demo playground
--------------------------

This Demo includes also a specialized docs-as-code setup for a GitHub
Codespaces online IDE. Everything that applies for the Gitpod IDE also
applies here.

In addition, Codespaces provides the ubCode extension.

Page Content
------------

.. toctree::
   :maxdepth: 2
   :caption: Explanation

   demo_details
   online_editor

.. toctree::
   :maxdepth: 2
   :caption: Demonstration

   basic_example/index
   automotive-adas/index
   safety_example/index
   coffee-machine/index
