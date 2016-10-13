import linear
import numpy

if __name__ == "__main__":

    X = numpy.array([[1,3,9],
                     [2,2,4],
                     [3,3,9],
                     [4,5,25]])

    y = numpy.array([10,11,12,16]) #cas trajanja voznje

    lr = linear.LinearLearner(lambda_=1.)
    napovednik = lr(X,y)

    print("Koeficienti", napovednik.th) #prvi je konstanten faktor

    nov_primer = numpy.array([2,11,121])
    print("Napoved", napovednik(nov_primer))