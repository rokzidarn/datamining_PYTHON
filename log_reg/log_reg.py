__author__ = 'Rok'

import pylab
import numpy
from scipy.optimize import fmin_l_bfgs_b #2 parametra - cost,grad

def load(name):
    """
    Open the file. Return a data matrix X (columns are features)
    and a vector of classes.
    """
    data = numpy.loadtxt(name)
    X, y = data[:,:-1], data[:,-1].astype(numpy.int)
    return X,y

def h(x, theta): #sigmuida
    """
    Predict the probability for class 1 for the current instance
    and a vector theta.
    """
    xn = numpy.array(x)
    tn = numpy.array(theta)

    return 1/(1 + numpy.exp(-theta.dot(x.transpose())))
    #return 1/(1+numpy.exp(numpy.dot(-tn,xn)))

def cost(theta, X, y, lambda_): #logL, cenilka; potrebno deliti s število primerov
    """
    Return the value of the cost function. Because the optimization algorithm
    used can only do minimization you will have to slightly adapt equations from
    the lectures.
    """
    cost_val = 0
    for l in range(len(X)):
        p = numpy.dot(y[l],(h(X[l],theta)))
        pnot = numpy.dot((1-y[l]),(1-h(X[l],theta)))
        cost_val = cost_val + numpy.log(p + pnot)

    num = (cost_val/len(X))*-1
    return num

def grad(theta, X, y, lambda_): #REGULARIZACIJA!!!
    """
    The gradient of the cost function. Return a numpy vector of the same
    size at theta.
    """

    d = (y - h(X,theta))
    theta_tmp = (numpy.dot(d,X))/len(X)*-1

    for i in range(len(theta)):
        theta_tmp[i] = theta_tmp[i] + lambda_* (y[i] - h(X[i], theta))
    """
    l = len(theta)
    theta_tmp = numpy.zeros(l)
    for j in range(l):
        sum = 0
        xij = 0
        for i in range(len(X)):
            xij = X[i][j]
            sum = sum + (y[i] - h(X[i],theta))

        theta_tmp[j] = theta[j] + lambda_ * sum * xij
    """
    return numpy.array(theta_tmp)

def draw_decision(X, y, classifier, at1, at2, grid=50):

    points = numpy.take(X, [at1, at2], axis=1)
    maxx, maxy = numpy.max(points, axis=0)
    minx, miny = numpy.min(points, axis=0)
    difx = maxx - minx
    dify = maxy - miny
    maxx += 0.02*difx
    minx -= 0.02*difx
    maxy += 0.02*dify
    miny -= 0.02*dify

    for c,(x,y) in zip(y,points):
        pylab.text(x,y,str(c), ha="center", va="center")
        pylab.scatter([x],[y],c=["b","r"][c!=0], s=200)

    num = grid
    prob = numpy.zeros([num, num])
    for xi,x in enumerate(numpy.linspace(minx, maxx, num=num)):
        for yi,y in enumerate(numpy.linspace(miny, maxy, num=num)):
            #probability of the closest example
            diff = points - numpy.array([x,y])
            dists = (diff[:,0]**2 + diff[:,1]**2)**0.5 #euclidean
            ind = numpy.argsort(dists)
            prob[yi,xi] = classifier(X[ind[0]])[1]

    pylab.imshow(prob, extent=(minx,maxx,maxy,miny))

    pylab.xlim(minx, maxx)
    pylab.ylim(miny, maxy)
    pylab.xlabel(at1)
    pylab.ylabel(at2)

    pylab.show()

class LogRegLearner(object): #iz učnih podatkov zgradi učni model LogRegClassifier

    def __init__(self, lambda_=0.0):
        self.lambda_ = lambda_

    def __call__(self, X, y):
        """
        Build a prediction model for date X with classes y.
        """
        X = numpy.hstack((numpy.ones((len(X),1)), X))

        #optimization as minimization
        theta = fmin_l_bfgs_b(cost,
            x0=numpy.zeros(X.shape[1]),
            args=(X, y, self.lambda_),
            fprime=grad)[0]

        return LogRegClassifier(theta)

class LogRegClassifier(object): #na podlagi značilk napove verjetnosti enega in drugega razreda

    def __init__(self, th):
        self.th = th

    def __call__(self, x):
        """
        Predict the class for a vector of feature values.
        Return a list of [ class_0_probability, class_1_probability ].
        """
        x = numpy.hstack(([1.], x))
        p1 = h(x, self.th)
        return [ 1-p1, p1 ]

if __name__ == "__main__":

    X,y = load('reg.data')

    learner = LogRegLearner(lambda_=0.0) # .02 .03 .04
    classifier = learner(X,y) # we get a model

    prediction = classifier(X[0]) # prediction for the first training example
    #print(prediction)

    draw_decision(X, y, classifier, 0, 1)