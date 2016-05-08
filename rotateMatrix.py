#!/usr/bin/python -tt
 
import sys
 
#create a N X N matrix
def getMatrix(n):
    matrix = []
    for i in range(n):
        inside = []
        for j in range(n):
            inside.append(j + i + 2)
        matrix.append(inside)
    return matrix
 
#print the matrix
def printMatrix(m):
    for row in m:
        print row
    print
 
#rotate the matrix by 90 degrees (clockwise) in place
def rotate90Degrees(m):
    layers = len(m) / 2
    length = len(m) - 1
 
    for layer in range(layers): #for each layer
        for i in range(layer, length - layer): # loop through the elements we need to change at each layer
            temp = m[layer][i] #save the top element, it takes just one variable as extra memory
            print 'i ->'+str(i)
            print
            print 'Temp = '+str(temp)
            #Left -> Top
            m[layer][i] = m[length - i][layer]
            #Bottom -> left
            m[length - i][layer] = m[length - layer][length - i]
            #Right -> bottom
            m[length - layer][length - i] = m[i][length - layer]
            #Top -> Right
            m[i][length - layer] = temp
 
#main function
def main():
    #it takes values from stdin
    line = input()
    n = int(line)
    print "N = "+ str(n)
    matrix = getMatrix(n)
    print "Original matrix:\n"
    printMatrix(matrix)
    rotate90Degrees(matrix)
    print "Rotate matrix by 90 degrees:\n"
    printMatrix(matrix)
 
if __name__ == '__main__':
    main()
