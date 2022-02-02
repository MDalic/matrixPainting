def NormalizeRows(matrix):
    rows = []
    for i in range(len(matrix)):
        rowBuffer = list(matrix[i])
        rows.append(list(map(int,rowBuffer)))
    return rows

def GetColumn(matrix,i):
    return [row[i] for row in matrix]

def GetAllLines(normalizedMatrix):
    listBuffer = []
    for i in range(len(normalizedMatrix)):
        listBuffer.append((normalizedMatrix[i],GetColumn(normalizedMatrix,i))) #(row,column) 
    return listBuffer

def GetPaintOptions(linesList):
    indexList = []
    for i in range(len(linesList)):
        for j in range(len(linesList[i])):
            if sum(linesList[i][j]) >= 5 and sum(linesList[i][j]) <9:
                if j == 0:
                    indexList.append((i,9-sum(linesList[i][j]),True)) #(index of list, ammount of 0's, true if row | false if column)
                if j == 1:
                    indexList.append((i,9-sum(linesList[i][j]),False))
    return indexList

def PaintColumn(matrix,i):
    for row in matrix:
        row[i] = 1
    return matrix

def PaintRow(matrix,i):
    matrix[i] = [1,1,1,1,1,1,1,1,1]
    return matrix



def test(matrix):
    intMatrix = NormalizeRows(matrix)
    counter = 0

    while True:
        AllLines = GetAllLines(intMatrix)
        listOfOptions = GetPaintOptions(AllLines)
        if len(listOfOptions) == 0:
            Failed = False
            for rows in intMatrix:
                if 0 in rows:
                    Failed = True
                    break
            if Failed:
                counter = -1
            break
        maxGain = max(listOfOptions, key=lambda x:x[1])
        if maxGain[2] == False:
            intMatrix = PaintColumn(intMatrix,maxGain[0])
        if maxGain[2] == True:
            intMatrix = PaintRow(intMatrix,maxGain[0])
        counter += 1

    return counter

def main():
    matrix1 = ["001111111","011111111","011111111","011111111","011111111","101111111","101111111","101111111","101111111"]
    matrix2 = ["011111111","101111111","110111111","111011111","111101111","111110111","111111011","111111101","111111110"]
    matrix3 = ["000000001","000000011","000000111","000001111","000011111","000011110","000011100","000011000","000010000"]
    matrix4 = ["000000001","000000011","000000111","000001111","000011111","000011110","000011100","000011000","000000000"]
    matrix5 = ["011111111","010001001","111111101","011111111","101010100","011111111","111111101","111011101","011111111"]


    print("test: "+"0) " +"Returns: " + str(test(matrix1)))
    print("test: "+"1) " +"Returns: " + str(test(matrix2)))
    print("test: "+"2) " +"Returns: " + str(test(matrix3)))
    print("test: "+"3) " +"Returns: " + str(test(matrix4)))
    print("test: "+"4) " +"Returns: " + str(test(matrix5)))



if __name__ == "__main__":
    main()