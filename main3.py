# -*- coding: utf-8 -*-
def max_substring_with_k_unique(s, k=2):
    if not isinstance(s, str):
      return 'string expected'
    result_sub = ''

    if len(s) < k:
        return s
    elif len(s) == k and len(set(s)) == k:
        return s
    
    for i in range(len(s)):
        curr_sub = s[i:]

        if len(set(curr_sub)) <= k: 
            curr_sub = s[i:]
            if len(curr_sub) > len(result_sub):
                result_sub = curr_sub
        else: 
            while len(set(curr_sub)) > k:
                curr_sub = curr_sub[:-1]
                if len(set(curr_sub)) == k and len(curr_sub) > len(result_sub):
                    result_sub = curr_sub

    if result_sub == '':
        result_sub = -1

    return result_sub



if __name__ == '__main__':
    s='daabbabacbebebe'
    print(max_substring_with_k_unique(s))