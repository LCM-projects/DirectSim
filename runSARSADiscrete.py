__author__ = 'manuelli'
from simulator import Simulator

sim = Simulator(autoInitialize=False, verbose=False)

sim.sarsaType = "discrete"
sim.Sarsa_numInnerBins = 5
sim.Sarsa_numOuterBins = 4
sim.Sensor_rayLength = 10


sim.randomSeed = 11
sim.randomizeControl       = True
sim.percentObsDensity      = 3.5
sim.nonRandomWorld         = True
sim.circleRadius           = 2.5
sim.worldScale             = 1
sim.supervisedTrainingTime = 3000
sim.learningRandomTime = 4000
sim.learningEvalTime = 500
sim.defaultControllerTime = 500
sim.options['SARSA']['burnInTime'] = sim.supervisedTrainingTime/2.0
sim.options['Reward']['actionCost'] = 0.2
sim.options['Reward']['raycastCost'] = 40.0
# sim.options['Reward']['collisionPenalty'] = 200



# world from Test
sim.randomSeed = 8
sim.randomizeControl       = True
sim.percentObsDensity      = 4
sim.nonRandomWorld         = True
sim.circleRadius           = 2.5
sim.worldScale             = 1
sim.options['World']['obstaclesInnerFraction'] = 0.8


# sim.supervisedTrainingTime = 10
# sim.learningRandomTime = 10
# sim.learningEvalTime = 10
# sim.defaultControllerTime = 10

sim.initialize()
sim.run()