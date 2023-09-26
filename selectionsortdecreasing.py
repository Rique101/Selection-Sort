def sort (data, first :int):
    """_summary_

    Args:
        data (_type_): _description_
        first (_type_): _description_
        int (_type_): _description_
    """    
    #initialize loop counter variable name i
    i = len(data) - first - 1

    #initialize loop counter variable named j to 0
    j = 0

    #initialize variable named big that will be used 
    #to store index of the biggest value
    big = 0

    #initialize variable named temp that will be used 
    #to swap list values
    temp = 0

    #loop through list as many times as specified by
    #len(data) and first
    #this loop represents the blue arrow
    while (i > 0):
        #set big equal to first
        big = first

        #set j equal to first + 1
        j = first + 1

        #loop through list starting with element at
        #first + 1 and continue until reach first + 1
        #this loop represents the yellow arrow
        while (j <= first + i):
            #if the value in data[big] is greater than
            #data[j]
            if (data[big] > data[j]):
                #set big equal to j
                big = j
            #increment j by 1
            j += 1
        
        #swap the data in the first + i with the data in big
        #set temp to value in data[first + i]
        temp = data[first + i]

        #set data[first + i] to value in data[big]
        data[first + i] = data[big]

        #set data[big] to value in temp
        data[big] = temp

        #decrement i by 1
        i -= 1