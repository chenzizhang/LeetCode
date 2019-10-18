"""
Cite from this blog:


本文链接：https://blog.csdn.net/fuxuemingzhu/article/details/83045983
作者： 负雪明烛
id： fuxuemingzhu
个人博客： http://fuxuemingzhu.cn/
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/83045983
"""


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        count = collections.Counter(A)
        Aset = set(A)
        Alist = list(Aset)
        Alist.sort()
        _lenA = len(Alist)
        res = 0
        for i in range(_lenA):
            for j in range(i, _lenA):
                c = target - Alist[i] - Alist[j]
                if c >= Alist[j] and c in Aset:
                    if Alist[i] != Alist[j] != c:
                        res += count[Alist[i]] * count[Alist[j]] * count[c]
                    elif Alist[i] == Alist[j] and Alist[j] != c:
                        res += count[c] * self.caculate(count[Alist[i]], 2)
                    elif Alist[j] == c and Alist[i] != Alist[j]:
                        res += count[Alist[i]] * self.caculate(count[Alist[j]], 2)
                    elif Alist[i] == c and Alist[j] != c:
                        res += count[Alist[j]] * self.caculate(count[c], 2)
                    else:
                        res += self.caculate(count[Alist[i]], 3)
        return int(res % (10 ** 9 + 7))
    
    def caculate(self, x, i):
        if i == 2:
            return x * (x - 1) / 2
        elif i == 3:
            return x * (x - 1) * (x - 2) / 6
