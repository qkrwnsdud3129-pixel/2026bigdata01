import numpy # 써드파티 라이브러리, C 배열 기반으로 대규모 처리에 적합. 매우빠름
scores = [100, 97, 88, 91]
average = numpy.mean(scores)
print(average)