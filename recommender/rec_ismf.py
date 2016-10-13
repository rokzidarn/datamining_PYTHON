__author__ = 'Rok'

from math import sqrt
import numpy
import random

def find_movie(movie_name, movies):
    for i in range(len(movies)):
        if(movie_name == movies[i]):
            return i

    return None

def get_data(f, num_lines):
    users = []
    movies = []

    for i in range(num_lines):
        line = f.readline().split("\t")
        users.append(int(line[0])); movies.append(line[1])

    users = sorted(set(users),key=int)
    movies = sorted(set(movies))

    data = [[0 for j in range(len(movies))] for i in range(len(users))]

    train_f = "train.txt"
    file = open(train_f,"r",encoding="utf-8")

    for k in range(num_lines):
        line = file.readline().split("\t")
        data[int(line[0])-1][find_movie(line[1],movies)] = int(line[2])

    return [data, users, movies]

def get_tau(train_d):
    k = 0
    for i in range(len(train_d)):
        for j in range(len(train_d[0])):
            if(train_d[i][j] != 0):
                k = k + 1

    return k

def get_derr(p,q, real, i, j, reg): #error derivative
    pq = numpy.dot(p,q)
    score = numpy.sum(pq)
    print(score)
    err = real - score

    pi = numpy.dot(p[i], numpy.transpose(p[i]))
    qj = numpy.dot(q[j], numpy.transpose(q[j]))
    #return 0.5 * err**2
    return (err**2 + reg*pi + reg*qj)/2


def ismf(data, users, movies, kstep, lr, reg): #700 - train, 243 - validate
    train_u = users[:700]
    train_d = data[:700] # partition

    test_d = data[700:]
    tau = get_tau(test_d)

    p = [[random.triangular(-0.01, 0.01, 0.01) for j in range(kstep)] for i in range(len(train_u))]
    q = [[random.triangular(-0.01, 0.01, 0.01) for j in range(len(data[0]))] for i in range(kstep)]

    rmse = 5
    k = 0
    for iters in range(40): #terminal condition
        sse = 0
        for i in range(len(train_d)):
            for j in range(len(train_d[0])):
                for k in range(kstep):
                    qk = [q[i] for i in range(j)]
                    pk = numpy.array(p)
                    pk2 = pk[:,j]
                    err_der = get_derr(pk2, qk, train_d[i][j], i, j, reg)
                    sse = sse + err_der

                pgrad_err = [0 for i in range(kstep)]
                qgrad_err = [0 for i in range(kstep)]
                for k in range(kstep):
                    pgrad_err[k] = -err_der*q[k][j] + reg*p[i][k]
                    qgrad_err[k] = -err_der*p[i][k] + reg*q[k][j]

                pn = [[0 for j in range(kstep)] for i in range(len(train_u))]
                qn = [[0 for j in range(len(data[0]))] for i in range(kstep)]

                for k in range(kstep):
                    pn = p[i][k] + lr*(pgrad_err[k]*q[k][j] - reg*p[i][k])
                    qn = q[k][j] + lr*(qgrad_err[k]*p[i][k] - reg*q[k][j])

        rmsen = sqrt(sse/tau)
        if(rmsen < rmse):
            p = pn; q = qn

    return [p,q]

#main

f = open("train.txt","r",encoding="utf-8")
num_lines = sum(1 for line in open("train.txt"))
info = get_data(f,num_lines)
data = info[0]; users = info[1]; movies = info[2]

k = 2; lr = 0.01; reg = 0.01
m = ismf(data, users, movies, k, lr, reg)
result = numpy.dot(m[0], m[1])

num_test = sum(1 for linef in open("test.txt"))
fr = open("test.txt","r",encoding="utf-8")

for k in range(num_lines):
    line = fr.readline().split("\t")
    calculated = result[int(line[0])][find_movie(line[1], movies)]
    print(line[0], line[1], "real:", line[2], "calculated:", calculated)