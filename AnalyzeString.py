from fuzzywuzzy import fuzz
print(fuzz.partial_ratio("'ate'", "eat"))
original = "Spring may have officially arrived this week but Toronto could get one more blast of wintry weather before the warm temperatures arrive. Environment Canada says near zero-temperatures could cause bring 'patchy' freezing rain, causing slippery roads and sidewalks."
sub = "Region possible freezing"
nextPos = 0
subListg = original.split()
print(subListg)
print(subListg.index("'patchy'"))
def analyze(original, sub, nextPos):
    originalList = original.split()
    subList = sub.split()
    n = len(subList)
    scores = []
    for i in range(0, 15):
        scores.append(fuzz.partial_ratio(" ".join(originalList[nextPos+i:nextPos+i+n]), sub))
    best = max(scores)
    #Finds the closest occurence even if 2 maxes
    bestI = scores.index(best)    
    print(scores)
    print(originalList[nextPos+bestI:nextPos+bestI+n])
    return nextPos + bestI
##def analyzeWords(original, sub, nextPos):
##    originalList = original.split()
##    subList = sub.split()
##    n = len(subList)
##    scores = []
print(analyze(original, sub, 20))
