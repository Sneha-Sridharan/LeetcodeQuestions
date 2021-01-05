class Solution {
    public boolean isMatch(String s, String p) {
        s=' '+s;
        p=' '+p;
        int plen=p.length(), slen=s.length(), i, j;
        boolean dp[][] = new boolean[slen][plen];
        dp[0][0]=true;
        for(j=1;j<plen;j++)
            if(p.charAt(j)=='*')
                dp[0][j]=dp[0][j-2];
        for(i=1;i<slen;i++)
            for(j=1;j<plen;j++)
            {
                if(p.charAt(j)==s.charAt(i) || p.charAt(j)=='.')
                    dp[i][j]=dp[i-1][j-1];
                else if(p.charAt(j)=='*')
                {
                    if(p.charAt(j-1)==s.charAt(i) || p.charAt(j-1)=='.')
                        dp[i][j]=dp[i][j-2] || dp[i-1][j];
                    else
                    {
                        dp[i][j]=dp[i][j-2];
                    }
                }
            }
        return dp[slen-1][plen-1];
    }
}