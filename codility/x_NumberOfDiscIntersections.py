# https://jobjava00.github.io/algorithm/codility/lesson6/NumberOfDiscIntersections/

# 현재 J 기준으로 반지름을 구해서 lower, upper 배열에 담는다.
# lower 배열 : J - A[J]
# upper 배열: J + A[J]
# 각 배열을 정렬한다.
# upper 보다 작은 lower 들은 반드시 가장 작은 upper 보다 큰 반지름을 갖는다. = 접점
# 다음 upper 에서 겹치지 않게 현재 J 만큼 빼준다.