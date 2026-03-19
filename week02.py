import statistics # 통계모듈 (각종 통계함수를 제공), 파이썬 모듈 기반으로 만들어져서 느리다.
scores = [100, 97, 88, 91]
average = statistics.mean(scores)
print(average)