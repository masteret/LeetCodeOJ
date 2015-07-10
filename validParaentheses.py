def isValid(s):
    count = 0
    last = []

    for d in s:
        print d
        if (d == '('):
            count += 1
            last.append('(')
        elif (d == '['):
            count += 1
            last.append('[')
        elif (d == '{'):
            count += 1
            last.append('{')
        elif d == ')':
            if count <= 0 or last[-1] != '(':
                return False
            count -= 1
            last.pop(-1)
        elif d == ']':
            if count <= 0 or last[-1] != '[':
                return False
            count -= 1
            last.pop(-1)
        elif d == '}':
            if count <= 0 or last[-1] != '{':
                return False
            count -= 1
            last.pop(-1)
        else:
            return False

    if count != 0:
        return False
    return True

def main():
    print isValid("([{[()]}])")

if __name__ == "__main__":
    main()

# public class Solution {
#     public boolean isValid(String s) {
#         int count = 0;
#         int[] next = new int[s.length()];
        
#         for (int i = 0; i < s.length(); i++) {
#             if (s.charAt(i) == '(') {
#                 next[count] = 1;
#                 count++;
#             } else if (s.charAt(i) == '[') {
#                 next[count] = 2;
#                 count++;
#             } else if (s.charAt(i) == '{') {
#                 next[count] = 3;
#                 count++;
#             } else if (s.charAt(i) == ')') {
#                 if ((count <= 0) || (next[count-1] != 1)) return false;
#                 count--;
#             } else if (s.charAt(i) == ']') {
#                 if ((count <= 0) || (next[count-1] != 2)) return false;
#                 count--;
#             } else if (s.charAt(i) == '}') {
#                 if ((count <= 0) || (next[count-1] != 3)) return false;
#                 count--;
#             }
#         }
        
#         if (count != 0) return false;
#         return true;
#     }
# }