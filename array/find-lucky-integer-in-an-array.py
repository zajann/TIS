'''
[문제]
https://leetcode.com/problems/find-lucky-integer-in-an-array/

* Easy *

주어진 배열에서 lucky-integer를 반환하라.
lucky-integer란 자신의 값과 그 카운트 수가 일치하는 수
여러 개의 lucky-integer가 있는 경우 가장 큰 수를 반환
lucky-integer가 없는 경우 -1을 리턴

ex)
arr = [1,2,2,3,3,3] -> 3
arr = [2,2,2,3,3] -> -1

Date: 2021.06.08 (화)
'''

from typing import Collection, List
import sys
import collections

class Solution:
    '''
    풀이 1
    - val:cnt인 딕셔너리를 만들고 딕셔너리를 val == cnt 인 값 중 가장 큰 수를 반환
    - 어차피 val은 자연수일 것이기 때문에 굳이 sys.maxsize를 안써도 될 듯
    '''
    def find_lucky_1(self, arr: List[int]) -> int:
        nums_cnt_dict = {}

        for n in arr:
            if n in nums_cnt_dict:
                nums_cnt_dict[n] += 1
            else:
                nums_cnt_dict[n] = 1

        max_num = -sys.maxsize
        
        for k, v in nums_cnt_dict.items():
            if k == v:
                max_num = max(max_num, v)

        if max_num == -sys.maxsize:
            return -1

        return max_num

    '''
    풀이 2
    - 미리 생성된 array에 해당 값을 인덱스로 하는 카운트를 증가하고 이후 내림차순으로 순회하며 인덱스==카운트인 경우 바로 리턴(가장 큰 수)
    - 54라인에서 값이 전체 길이보다 큰 경우에는 skip하는 것이 포인트, 어차피 카운트가 안됨 (ex. [5]인 경우에 카운트가 5가 될 수 없음)
    - 주어진 배열의 길이만큼 새로운 배열을 생성하므로 공간복잡도면에서는 조금 안좋지만 성능 우수
    '''
    def find_lucky_2(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n+1)
        for a in arr:
            if a <= n:
                cnt[a] += 1
        for i in range(n, 0, -1):
            if cnt[i] == i:
                return i
        return -1


    '''
    풀이 3
    - collections.Counter()를 이용하여 값:카운트의 딕셔너리를 얻고 리스트 컴프리헨션을 통해 간단하게 최대값 리턴
    - https://docs.python.org/3/library/collections.html
    '''
    def find_lucky_3(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)

        return max([k for k, v in cnt.items() if k == v] + [-1])

    '''
    풀이 4
    - 리스트의 count() 내장 함수를 이용하여 값 구하기
    '''
    def find_lucky_4(self, arr: List[int]) -> int:
        result = []
        for a in arr:
            if arr.count(a) == a:
                result.append(a)
            else:
                result.append(-1)
        return max(result)

if __name__ == '__main__':
    sol = Solution()

    print(sol.find_lucky_1([1,2,2,3,3,3]))
    print(sol.find_lucky_2([1,2,2,3,3,3]))
    print(sol.find_lucky_3([1,2,2,3,3,3]))
    print(sol.find_lucky_4([1,2,2,3,3,3]))
    
