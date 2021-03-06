#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2011, Florent Lamiraux, Thomas Moulard, JRL, CNRS/AIST
#
# This file is part of dynamic-graph.
# dynamic-graph is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# dynamic-graph is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# dynamic-graph. If not, see <http://www.gnu.org/licenses/>.

from dynamic_graph.sot.dynamics.tools import *
from __main__ import robot, solver

#  Operational points tasks
solver.sot.push(robot.name + '_task_right-ankle')
solver.sot.push(robot.name + '_task_left-ankle')
solver.sot.push(robot.name + '_task_right-wrist')
solver.sot.push(robot.name + '_task_gaze')

# Move right wrist
reach(robot, 'right-wrist', 0.25, 0, 0.25)
