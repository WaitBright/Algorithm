class Solution:
    """数组
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


if __name__ == '__main__':
    solution = Solution()
    # 1. array: 二维数组， target给定数值
    array = [[1, 3, 4], [2, 5, 7], [10, 12, 14]]
    target1 = 12
    target2 = 13
    res1 = solution.Find(target1, array)
    # res12 = solution.Find(target12, array)
    print("1. result: %s" % res1)