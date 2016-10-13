__author__ = 'Rok'
from math import sqrt

def print_data(data, users):
    for k in range(len(users)):
        print(data[k])

def find_movie(movie_name, movies):
    for i in range(len(movies)):
        if(movie_name==movies[i]):
            return i

    return None

def calc_avg(f,num_lines):
    users = []
    movies = []
    avg_all = 0

    for i in range(num_lines):
        line = f.readline().split("\t")
        users.append(line[0]); movies.append(line[1])
        avg_all = avg_all + int(line[2])

    avg_all = avg_all/num_lines

    users = sorted(set(users),key=int)
    movies = sorted(set(movies))
    avg_users = [0 for i in range(len(users))]
    avg_movies = [0 for j in range(len(movies))]

    data = [[0 for j in range(len(movies))] for i in range(len(users))]

    train_f = "train.txt"
    file = open(train_f,"r",encoding="utf-8")
    user_pos = 0; #user_pos = user_name-1
    sum_user = 0
    num = 0

    for k in range(num_lines):
        line = file.readline().split("\t")

        if(user_pos == int(line[0])-1):
            sum_user = sum_user + int(line[2])
            num = num + 1
        else:
            avg_users[user_pos] = sum_user/num
            user_pos = int(line[0])-1
            sum_user = 0
            num = 0
            sum_user = sum_user + int(line[2])
            num = num + 1

        data[int(line[0])-1][find_movie(line[1],movies)] = int(line[2])

    for j in range(len(movies)):
        sum = 0
        num = 0
        for i in range(len(users)):
            sum = sum + data[i][j]
            if(data[i][j]!=0):
                num = num + 1
        avg_movies[j] = sum/num

    return [avg_all, avg_users, avg_movies, data, users, movies]

def find_avg_u(data, avg_u, users, u):
    index = -1
    for i in range(len(users)):
        if(u == users[i]):
            index = i
    if(index == -1):
        return 0
    else:
        return avg_u[index]

def find_avg_m(data, avg_m, movies, m):
    index = -1
    for i in range(len(movies)):
        if(m == movies[i]):
            index = i

    if(index == -1):
        return 0
    else:
        return avg_m[index]

def avg_bias():
    train_f = "train.txt"
    f = open(train_f,"r",encoding="utf-8")
    num_lines = sum(1 for line in open("train.txt"))

    averages = calc_avg(f,num_lines)
    avg_a = averages[0]
    avg_u = averages[1]
    avg_m = averages[2]
    data = averages[3]
    users = averages[4]
    movies = averages[5]

    num_test = sum(1 for line in open("test.txt"))
    fr = open("test.txt","r",encoding="utf-8")
    r = 0
    for k in range(num_test):
        line = fr.readline().split("\t")
        real = int(line[2])
        b_user = find_avg_u(data, avg_u, users, int(line[0])) - avg_a
        b_movie = find_avg_m(data, avg_m, movies, line[1]) - avg_a
        h = avg_a + b_user + b_movie

        if(h < 1):
            h = avg_a
        if(h > 5):
            h = 5

        r = r + sqrt((h - real)**2)

    print(r/num_test)

#main

avg_bias() #0.945
