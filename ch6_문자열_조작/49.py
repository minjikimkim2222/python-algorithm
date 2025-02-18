# Group Anagrams
# 문자열 배열 -> 애너그램(철자재배열)로 그룹핑


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 애너그램 관계 파악 -> 모든 리스트를 동일한 기준으로 정렬한 후, 같으면 애너그램 관계이다

        # 딕셔너리는 아래와 같이 그냥 dict(strs) 리스트가 아니라, 키-값 쌍의 리스트를 만들어야 값 제대로 변환함
            #  strs_todict = dict(strs)

        dict_str = dict()
        for str in strs:
            sorted_str = sorted(str)
            joined_str = ''.join(sorted_str)
            # print(f'str :: {str} // sorted :: {sorted_str} -> {joined_str}')

            # 각 정렬한 기준별로, 어떤 값들이 있는지 정리해줘야 함 -> 자료구조 : dict 필요
            if joined_str in dict_str:
                dict_str[joined_str].append(str)
            else:
                dict_str[joined_str] = [str] ## 초기값을 리스트로 설정하면, 위에서 append가 가능해짐 !!
        # print(f'dict_str :: {dict_str}')

        ret_list = []
        for key, value in dict_str.items():
            ret_list.append(value)

        return ret_list

solution = Solution()
input = ["a"]

ret_list = solution.groupAnagrams(input)
print(f'return :: {ret_list}')