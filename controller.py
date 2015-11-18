import numpy as np
import scipy.integrate as integrate

class ControllerObj(object):

    def __init__(self, sensor):
        self.Sensor = sensor

    def computeControlInput(self, state, t, frame, raycastDistance=None):
        # test cases
        # u = 0
        # u = np.sin(t)
        if raycastDistance is None:
            distances = self.Sensor.raycastAll(frame)
        else:
            distances = raycastDistance



        # #Barry 12 controller
        numRays = self.Sensor.numRays
        # rays = self.Sensor.rays

        # c_1 = 1
        # c_2 = 1
        # c_3 = 1

        # F = distances*0.0

        # for i in range(0,numRays):
        #     r = distances[i]
        #     if r is not None:
        #         r_hat = rays[:,i]
        #         x_hat = np.array(frame.transform.TransformNormal(rays[:,numRays/2]))

        #         G_hat = x_hat

        #         F[i] = np.dot(-c_1 * x_hat, r_hat * (1.0 - (r/c_3))**2.0 / (1.0 + (r/c_3)**3.0))

        # Ftot = np.sum(F)
        # F_G = np.dot(-c_2 * G_hat, x_hat)

        # u = F_G + Ftot
        # print u


        # Count stuff controller
        firstHalf = distances[0:numRays/2]
        secondHalf = distances[numRays/2:]
        tol = 1e-3;

        numLeft = np.size(np.where(firstHalf < self.Sensor.rayLength - tol))
        numRight = np.size(np.where(secondHalf < self.Sensor.rayLength - tol))

        if numLeft == numRight:
            u = 0
        elif numLeft > numRight:
            u = 2
        else:
            u = -2

        return u