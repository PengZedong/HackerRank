def main():
    n = int(input())
    # map applies a function to all the items in an input_list.
    nums = list( map( int, input().split() ) )
    #nums.sort() changes the order of list,sort(nums) don't change the order of the list
    nums.sort()
    #print( nums )
    #   Get median element
    if len( nums ) % 2 == 0:
        median = ( nums[ int(len(nums) / 2) ] + nums[ int(len(nums) / 2) - 1 ] ) / 2
    else:
        median = nums[ int(len(nums) / 2) ]
    #use dictionary to store the number of nums
    numDict = {}
    max = 1
    maxElement = nums[0]
    sum = 0
    max = 1
    for element in nums:
        sum += element
        #   Hash to get mode
        if element not in numDict.keys():
            #print( "inserting , ", element )
            numDict[ element ] = 1
        else:
            numDict[ element ] = numDict[ element ] + 1
            if numDict[ element ] == max:
                #   Check if new element is less than old
                if element < maxElement:
                    max = numDict[ element ]
                    maxElement = element
            elif numDict[ element ] > max:
                max = numDict[ element ]
                maxElement = element

    print( "{:.1f}".format( sum / len(nums) ) )
    print( "{:.1f}".format( median ) )
    print( maxElement )


if __name__ == "__main__":
    main()
