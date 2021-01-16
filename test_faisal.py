def Display_Players(Selector1,Selector2):
    def bubbleSort(arr): 
        n = len(arr) 
      
        # Traverse through all array elements 
        for i in range(n-1): 
        # range(n) also work but outer loop will repeat one time more than needed. 
      
            # Last i elements are already in place 
            for j in range(0, n-i-1): 
      
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater 
                # than the next element 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
      
    # Driver code to test above 
    # Selector1 = [] 
    for i in range(len(Selector1)):
        Selector1[i] = Selector1[i].lower()
    for y in range(len(Selector2)):
        Selector2[y] = Selector2[y].lower()    
    bubbleSort(Selector1)
    bubbleSort(Selector2)  
    print(Selector1,Selector2)
    return Selector1,Selector2 
    # print ("Sorted array is:") 
    # for i in range(len(arr)): 
    #     print ("%d" %arr[i]), 


a = ['ali ahmed', 'ali zeshan','babar yonus'] # this list should be of 12

b = ['Babar Younus', ' ali ahmed', 'kaka rival']

x = Display_Players(a,b)
print(x)