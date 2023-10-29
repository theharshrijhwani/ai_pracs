import math


def minMax(currDepth, nodeIndex, maxTurn, scores, targetDepth):
    if (currDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minMax(currDepth+1, nodeIndex*2, False, scores, targetDepth), minMax(currDepth+1, nodeIndex*2+1, False, scores, targetDepth))
    else:
        return min(minMax(currDepth+1, nodeIndex*2, True, scores, targetDepth), minMax(currDepth+1, nodeIndex*2+1, True, scores, targetDepth))


scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("Optimal path is: ", end="")
print(minMax(0, 0, True, scores, treeDepth))
