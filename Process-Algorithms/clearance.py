# -*- coding: utf-8 -*-
"""
Copyright 2018
Dan Aukes, Cole Brauer
"""

import coloredlogs
import model_tools as model
import mesh_tools as mesh
import opengl_plot_tools as plot
import numpy as np
  
if __name__=='__main__':
    coloredlogs.install(level='DEBUG')

    # Import model
    joint1 = model.import_vox('sample-object-1.vox')

    model1 = model.clearance(joint1, 'mill') * 21

    # Initialize application 1
    app1, w1 = plot.prep()

    # Convert model to mesh data
    #v, vc, t = mesh.create_from_model(model.union(joint1, model1))
    v, vc, t = mesh.create_from_model(model1)

    # Create mesh item and add to plot
    mi = plot.make_mi(v, t, vc, drawEdges = True)
    w1.addItem(mi)

    # Show plot 1
    plot.show(w1, joint1, grids = True)

    # Save screenshot of plot 1
    # w1.paintGL()
    # w1.grabFrameBuffer().save('clearance-fig1.png')

    app1.exec_()