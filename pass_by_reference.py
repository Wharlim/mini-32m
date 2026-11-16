def main():
   x = [1, 2, 3]
   y = [1, 2, 3]
   print(id(x), id(y))
   x = y 
   print(id(x), id(y))

if __name__ == "__main__":
    main()