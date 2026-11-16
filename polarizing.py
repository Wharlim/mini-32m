#so the idea is that i want to go through ratings.tsv, record every single movie id and the total respective ratings.
#then go to movies.tsv and check for those movie ids, and get their average rating

import sys
import math

def stddeviation(data):
    n = len(data)
    if n == 0:
        return 0.0
    mean = sum(data) / n
    variance = 0
    for x in data:
        variance += (x - mean) ** 2
    variance /= n
    return math.sqrt(variance)

def main():
    dictionary1 = {}
    infile = sys.stdin
    header = infile.readline()
    for line in infile:
        line = line.removesuffix("\n")
        row = line.split("\t")
        movie_id = row[1]
        rating = float(row[2])
        if movie_id not in dictionary1:
            dictionary1[movie_id]= [0,0," ",[]]
        for key in dictionary1.keys():
            if key == movie_id:
                dictionary1[movie_id][0]+=1 
                dictionary1[movie_id][1]+=(rating)
                dictionary1[movie_id][3].append(rating)
    

    with open("movies.tsv", "r") as infile:
        header = infile.readline()
        for line in infile:
            line = line.removesuffix("\n")
            row = line.split("\t")
            movie_id = row[0]
            title = row[1]
            if dictionary1[movie_id][0] >= 100:
                dictionary1[movie_id][2] = title



    highestt_std_dev = 0.0
    for key in dictionary1.keys():
        if dictionary1[key][0] >= 100:
            std_dev = stddeviation(dictionary1[key][3])
            if std_dev > highestt_std_dev:
                highestt_std_dev = std_dev
                movie_with_highest_std_dev = dictionary1[key][2]

    print(f"Movie with highest standard deviation: {movie_with_highest_std_dev} (std dev: {highestt_std_dev:.2f})")



if __name__ == "__main__":
    main()