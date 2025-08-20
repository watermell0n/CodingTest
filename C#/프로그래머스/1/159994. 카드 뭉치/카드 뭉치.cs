using System;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {
        string answer = "Yes";
        int i = 0; int j = 0;
        int num = 0;
        
        while (num<goal.Length)
        {
            if (i<cards1.Length && goal[num]==cards1[i])
            {
                num++;
                i++;
            }
            else if (j<cards2.Length && goal[num]==cards2[j])
            {
                num++;
                j++;
            }
            else
            {
                answer = "No";
                break;
            } 
        }
        return answer;
    }
}