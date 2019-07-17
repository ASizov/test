def max_substring_with_k_unique(s):
  if not isinstance(s, str):
      return 'string expected'
  curr_sub, result_sub = [], []
  max_len = -1
  for i in range(0, len(s)):
    curr_sub.append(s[i])
    if len(set(curr_sub)) <= 2:
      if len(curr_sub) >= max_len:
        max_len = len(curr_sub)
        result_sub = curr_sub[:]
    else:
      while len(set(curr_sub)) != 2:
        curr_sub = curr_sub[1:]
      if max_len <= len(curr_sub) and len(set(curr_sub)) <= 2:
        max_len =  len(curr_sub)
        result_sub = curr_sub[:]
  result = ''
  for x in result_sub:
    result = result + x
  return result

if __name__ == '__main__':
    s='aabacbebebe'
    print(max_substring_with_k_unique(s))