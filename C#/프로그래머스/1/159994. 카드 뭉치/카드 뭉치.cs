using System;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {
        string answer = "Yes";
        int i = 0; int j = 0;

        for (int num=0; num<goal.Length; num++)
        {
            if (i<cards1.Length && goal[num]==cards1[i])
            {
                i++;
                continue;
            }
            else if (j<cards2.Length && goal[num]==cards2[j])
            {
                j++;
                continue;
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