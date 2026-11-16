#so the idea is that i want to go through ratings.tsv, record every single movie id and the total respective ratings.
#then go to movies.tsv and check for those movie ids, and get their average rating

import sys

def main():
    dictionary1 = {}
    infile = sys.stdin
    header = infile.readline()
    for line in infile:
        line = line.removesuffix("\n")
        row = line.split("\t")
        movie_id = row[1]
        rating = row[2]
        if movie_id not in dictionary1:
            dictionary1[movie_id]= [0,0," "]
        for key in dictionary1.keys():
            if key == movie_id:
                dictionary1[movie_id][0]+=1 
                dictionary1[movie_id][1]+=float(rating)
   
    with open("movies.tsv", "r") as infile:
        header = infile.readline()
        for line in infile:
            line = line.removesuffix("\n")
            row = line.split("\t")
            movie_id = row[0]
            title = row[1]
            if dictionary1[movie_id][0] >= 100:
                dictionary1[movie_id][2] = title

    
    total = 0
    for key, value in dictionary1.items():
        average_rating = value[1] / value[0]
        if average_rating >= 4.0 and value[2] != " ":
            print(f"{average_rating:.2f} {value[2]}")
            total += 1 

    print(f"Total movies with average rating >= 4.0: {total}")
 

if __name__ == "__main__":
    main()