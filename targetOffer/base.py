class Solution:
    """array
    1. 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    idea: 从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。
    于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。
    """
    def Find(self, target, array):
        if not array or not target:
            return False
        row = len(array) - 1
        col = len(array[0]) - 1
        i = row
        j = 0
        while i >= 0 and j <= col:
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False

    def replaceSpace(self, s):
        """array
        2. 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
        """
        return s.replace(' ', '%20')

    def MoreThanHalfNum_Solution(self, numbers):
        """array tips

        :param numbers:
        :return:
        """
        from collections import Counter
        count = Counter(numbers).most_common()
        if count[0][1] > len(numbers) / 2.0:
            return count[0][0]
        return 0


    def GetLeastNumbers_Solution(self, tinput, k):
        """
        输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
        :param tinput:
        :param k:
        :return:
        """
        if k > len(tinput):
            return []
        import heapq
        return heapq.nsmallest(k, tinput)


if __name__ == '__main__':
    solution = Solution()
    # 1. array: 二维数组， target给定数值
    array = [[1, 3, 4], [2, 5, 7], [10, 12, 14]]
    target1 = 12
    target2 = 13
    res1 = solution.Find(target1, array)
    # res12 = solution.Find(target12, array)
    print("1. result: %s" % res1)

    res21 = solution.replaceSpace("We are Happy!")
    print("2. result: %s" % res21)

