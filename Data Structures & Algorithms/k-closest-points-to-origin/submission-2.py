class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(points):
            return points[0] ** 2 + points[1] ** 2

        def partition(left, right):
            if left >= right:
                return left
                
            pivot = distance(points[right])

            p = left

            for i in range(left, right):
                if distance(points[i]) <= pivot:
                    points[i], points[p] = points[p], points[i]
                    p += 1
            
            points[p], points[right] = points[right], points[p]

            return p

        left = 0
        right = len(points) - 1

        while True:
            pivot_index = partition(left, right)

            if pivot_index == k:
                break

            elif pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

        return points[:k]
