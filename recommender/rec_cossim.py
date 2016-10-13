__author__ = 'Rok'

from math import sqrt

def cosine_distance(v1,v2):
    sumxx = sum(v1[i]**2 for i in range(len(v1)))
    sumyy = sum(v2[i]**2 for i in range(len(v2)))
    sumxy = 0
    for j in range(len(v1)):
        if(v1[j]!=0 and v2[j]!=0):
            sumxy = sumxy + v1[j]*v2[j]

    dist = (sumxy/(sqrt(sumxx)*sqrt(sumyy)))
    return 1/(1+dist)

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

def find_movie(movie_name, movies):
    for i in range(len(movies)):
        if(movie_name == movies[i]):
            return i

    return None

def get_movie_data(data, movie):
    movie_data = [0 for j in range(len(data))]
    for i in range(len(data)):
        movie_data[i] = data[i][movie]

    return movie_data

def get_score(movie_pos, user_pos, data, movies):
    if(movie_pos == None):
        return 3.5
    else:
        dist = 2
        movie_index = -1

        for m in range(len(movies)):
            if(m != movie_pos and data[user_pos][m] != 0):
                m1 = get_movie_data(data, movie_pos)
                m2 = get_movie_data(data,m)
                d = cosine_distance(m1,m2)
                if(d < dist):
                    dist = d
                    movie_index = m

        return data[user_pos][movie_index]

def get_scoreRec(movie_pos, user_pos, data, movies):
    if(movie_pos == None):
        return 3.5
    else:
        im = 0; st = 0
        for m in range(len(movies)):
            if(m != movie_pos and data[user_pos][m] != 0):
                m1 = get_movie_data(data, movie_pos)
                m2 = get_movie_data(data,m)
                d = cosine_distance(m1,m2)
                st = st + d*data[user_pos][m]
                im = im + d

        return st/im

#main

f = open("train.txt","r",encoding="utf-8")
num_lines = sum(1 for line in open("train.txt"))
info = get_data(f,num_lines)
data = info[0]; users = info[1]; movies = info[2]

num_test = sum(1 for line in open("test.txt"))
fr = open("test.txt","r",encoding="utf-8")

rmse = 0
for k in range(num_test):
    line = fr.readline().split("\t")
    movie_pos = find_movie(line[1], movies)
    user_pos = int(line[0])-1
    score = get_scoreRec(movie_pos, user_pos, data, movies)
    rmse = rmse + sqrt((score - int(line[2]))**2)

print(rmse/num_test) #0.839


