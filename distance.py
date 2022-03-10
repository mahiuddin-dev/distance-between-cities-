
#list city 
city = ['Rabat','Sueca','Rudow','Mosu','Plessis Trevise','Kang Dong','Nezahualcóyotl','Lindenwold','Queanbeyan','Saint Chamond','Cheektowaga','Tirupati','Snezhinsk','Glazov','Gaoyou','Nola','Rutigliano','Colombo','Meckenheim','Hamburg']

# distance city 
distance = [1063,2656,1352,1841,61,1634,151,285,146,11,380,2547,2524,97,6999,63,105,244,502,30]


input1 = input("Enter the city name 1 : ").title()
input2 = input("Enter the city name 2 : ").title()

totalcity = len(city)-1

# distance city and distance
def distance_city(input1,input2):
    if input1 in city and input2 in city:
        if input1 == input2:
            print("Distance is 0")
        else:
            # index of input city
            index1 = city.index(input1)
            index2 = city.index(input2)

            # variable swap
            if index1 > index2:
                index1,index2 = index2,index1

            distance1 = 0
            distance1path = []
            index1_data = index1

            # distance 1 
            while index1 != index2:
                distance1 = distance1 + distance[index1]
                distance1path.append(index1)
                index1 = index1 + 1

            # distance 2
            distance2 = 0
            distance2path = []

            if index1_data > 0:
                data = index1_data
                for i in range(data):
                    distance2 = distance2 + distance[i] 
                    distance2path.append(i)

            for i in range(totalcity,index2-1,-1):
                distance2 = distance2 + distance[i]
                distance2path.append(i)
               
            # check distance 1 and distance 2 and print the shortest path    
            if distance1 < distance2:
                print("Distance is",distance1,"km")
                for i in distance1path:
                    print(city[i])
      
            else:
                print("Distance is",distance2,"km")
                for i in distance2path:
                    print(city[i])

    else:
        print("Invalid input")

# Print the shortest path function 
distance_city(input1,input2)

