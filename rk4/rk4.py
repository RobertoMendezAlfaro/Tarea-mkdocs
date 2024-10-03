#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

oOper = np.array([[0, 1], [1, 0]])

yInit = np.array([[1, 0], [0, 0]])

def dyn_generator(oper, state):
    """Function f(t,y) = -i[O, y(t)].

    Examples:
        >>> dyn_generator([[0, 1],[1, 0]], [[1, 0],[0, 0]])
        [0.-0.j  0.+1.j]
        [0.-1.j  0.-0.j]

    Args:
        oper (array):  First argument
        state (array): Second argument

    Returns:
        (array): Returns the value of -i[oper, state]

    """

    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))




def rk4(func, time, stateInit, h):
    """Implements the Runge-Kutta method

    Examples:
        >>> rk4(dyn_generator, [[0, 1],[1, 0]], [[1, 0],[0, 0]], 40)
        [ 1.54284144e+10+0.0000000e+00j   0.00000000e+00-3.9513516e+08j]
        [ 0.00000000e+00+3.9513516e+08j  -1.54284144e+10+0.0000000e+00j]

    Args:
        func (function):   Equation used
        time (array):      Second Argument
        stateInit (array): Third Argument
        h (int):           Fourth Argument

    Returns:
        yN (array): Returns the next value of a dynamic system
    """
    k_1 = h * func(time, stateInit)

    k_2 = h * func(time + (0.5 * h), stateInit + (k_1 / 2))

    k_3 = h * func(time + (0.5 * h), stateInit + (k_2 / 2))

    k_4 = h * func(time + h, stateInit + k_3)

    state_after = stateInit + (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)

    return state_after


h = 40


times = np.linspace(0,10,h)

yCopy = yInit.copy()


stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

for tt in range(times.size):

    stateQuant00[tt] = yInit[0,0]
    stateQuant11[tt] = yInit[1,1]

    yN = rk4(dyn_generator, times[tt], yInit, h)

    yInit = yN


X = times
Ya = stateQuant00
Yb = stateQuant11

plt.plot(X, Ya)
plt.plot(X, Yb)
plt.show()
