class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length(), m = p.length();
        int i = 0, j = 0, iprev = -1, star = -1;
        while (i < n) 
        {
            if (j < m && (p[j] == '?' || s[i] == p[j])) 
            {
                i++; 
                j++;
            } 
            else if (j < m && p[j] == '*') 
            {
                star = j++;
                iprev = i;
            } 
            else if (star != -1) {
                j = star + 1;
                i = iprev++;
            } 
            else 
                return false;
        }
        
        while (j < m && p[j] == '*') 
            j++;
        return j == m;
    }
};
