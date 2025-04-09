// Last updated: 4/10/2025, 12:52:38 AM
class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i=0,j=0;
        int word1Len=word1.length();
        int word2Len=word2.length();
        StringBuilder result=new StringBuilder();
        while((i<word1Len) && (j<word2Len))
        {
            result.append(word1.charAt(i++));
            result.append(word2.charAt(j++));
        }
        while (i<word1Len)
           result.append(word1.charAt(i++));
        while(j<word2Len)
             result.append(word2.charAt(j++));

        return result.toString();
    }
}