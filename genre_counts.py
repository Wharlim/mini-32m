import sys

def main():
    infile = sys.stdin
    dictionary = {
    }
    header = infile.readline()
    for line in infile:
        line = line.removesuffix("\n")
        row = line.split("\t")
        genres = row[2].split("|")
        for genre in genres:
            if genre not in dictionary:
                dictionary[genre] = 0
            for key in dictionary.keys():
                if key == genre:
                    dictionary[key] +=1
               
        
    infile.close()
    for key, value in dictionary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()