
import math

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Function to map tabular data to speed using distance between points
def RealSpeed(d,t):
    # compute speed
    try:
        return float(d/t*3600.)
    except:
        return None

# Euclidean distance
def distance(lat1, lon1 ,lat2 , lon2):
    # compute distance between two points
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - math.cos((lat2 - lat1) * p) / 2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((lon2 - lon1) * p)) / 2
    return 12742 * math.asin(math.sqrt(a)) #2*R*asin...


def FindMiddlePoints(mus, T, draw=False):
    a = np.array([(1 / 2. * n) for n in range(2 * T + 1)])
    tau = sp.symbols('tau_0:24')
    t = sp.Symbol('t')
    E = []
    for N in range(0, T):
        if N > 0 and N < T - 1:
            y1 = ((tau[N] - tau[N - 1])) / (a[2 * N + 1] - a[2 * N - 1]) * (t - a[2 * N - 1]) + tau[N - 1]
            y2 = ((tau[N + 1] - tau[N])) / (a[2 * N + 3] - a[2 * N + 1]) * (t - a[2 * N + 1]) + tau[N]
            eq1 = sp.integrate(y1, (t, a[2 * N], a[2 * N + 1]))
            eq2 = sp.integrate(y2, (t, a[2 * N + 1], a[2 * N + 2]))
            e = eq1 + eq2 - mus[N]
            E.append(e)
            # print(e)
        elif N == 0:
            y1 = ((tau[N] - tau[T - 1])) / (a[2 * N + 1] - (-a[2 * N + 1])) * (t - (-a[2 * N + 1])) + tau[T - 1]
            y2 = ((tau[N + 1] - tau[N])) / (a[2 * N + 3] - a[2 * N + 1]) * (t - a[2 * N + 1]) + tau[N]
            eq1 = sp.integrate(y1, (t, a[2 * N], a[2 * N + 1]))
            eq2 = sp.integrate(y2, (t, a[2 * N + 1], a[2 * N + 2]))
            e = eq1 + eq2 - mus[N]
            E.append(e)
            # print(e)
        else:
            y1 = ((tau[N] - tau[N - 1])) / (a[2 * N + 1] - a[2 * N - 1]) * (t - a[2 * N - 1]) + tau[N - 1]
            y2 = ((tau[0] - tau[N])) / (a[2 * N + 1] + 1 - a[2 * N + 1]) * (t - a[2 * N + 1]) + tau[N]
            eq1 = sp.integrate(y1, (t, a[2 * N], a[2 * N + 1]))
            eq2 = sp.integrate(y2, (t, a[2 * N + 1], a[2 * N + 2]))
            e = eq1 + eq2 - mus[N]
            E.append(e)
            # print(e)

    salida = sp.linsolve(E, (tau))
    # print(salida)
    results = next(iter(salida))

    if draw:
        plt.figure(figsize=(10, 5))
        plt.bar([0.5 + i for i in range(T)], mus, label="Predicted hourly travel time", width=0.95, align='center',
                color='lightgray')
        plt.plot([0.5 + i for i in range(T)], results, label="Interpolation")
        plt.xlabel('Hour')
        plt.ylabel(r'Travel Time (s)')
        plt.legend(prop={'size': 8})
        plt.savefig('./Images/Middle_points_reg.pdf')
        plt.show()

    results = [int(i) for i in results]
    return results


def FindMiddlePointsSymbol(T):
    a = np.array([(1 / 2. * n) for n in range(2 * T + 1)])
    tau = sp.symbols(str('tau_0:') + str(T))
    t = sp.Symbol('t')
    mus = sp.symbols('u_0:24')
    E = []
    for N in range(0, T):
        if N > 0 and N < T - 1:
            y1 = ((tau[N] - tau[N - 1])) / (a[2 * N + 1] - a[2 * N - 1]) * (t - a[2 * N - 1]) + tau[N - 1]
            y2 = ((tau[N + 1] - tau[N])) / (a[2 * N + 3] - a[2 * N + 1]) * (t - a[2 * N + 1]) + tau[N]
            eq1 = sp.integrate(y1, (t, a[2 * N], a[2 * N + 1]))
            eq2 = sp.integrate(y2, (t, a[2 * N + 1], a[2 * N + 2]))
            e = eq1 + eq2 - mus[N]
            E.append(e)
            # print(e)
        elif N == 0:
            y1 = ((tau[N] - tau[T - 1])) / (a[2 * N + 1] - (-a[2 * N + 1])) * (t - (-a[2 * N + 1])) + tau[T - 1]
            y2 = ((tau[N + 1] - tau[N])) / (a[2 * N + 3] - a[2 * N + 1]) * (t - a[2 * N + 1]) + tau[N]
            eq1 = sp.integrate(y1, (t, a[2 * N], a[2 * N + 1]))
            eq2 = sp.integrate(y2, (t, a[2 * N + 1], a[2 * N + 2]))
            e = eq1 + eq2 - mus[N]
            E.append(e)
            # print(e)
        else:
            y1 = ((tau[N] - tau[N - 1])) / (a[2 * N + 1] - a[2 * N - 1]) * (t - a[2 * N - 1]) + tau[N - 1]
            y2 = ((tau[0] - tau[N])) / (a[2 * N + 1] + 1 - a[2 * N + 1]) * (t - a[2 * N + 1]) + tau[N]
            eq1 = sp.integrate(y1, (t, a[2 * N], a[2 * N + 1]))
            eq2 = sp.integrate(y2, (t, a[2 * N + 1], a[2 * N + 2]))
            e = eq1 + eq2 - mus[N]
            E.append(e)
            # print(e)

    salida = sp.linsolve(E, (tau))
    # print(salida)
    results = next(iter(salida))

    # results=[int(i) for i in results]
    return results

