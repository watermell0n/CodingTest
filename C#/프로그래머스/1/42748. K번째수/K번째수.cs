using System;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        int[] answer = new int[commands.GetLength(0)];
        
        for (int i=0; i<commands.GetLength(0); i++)
        {
            int start = commands[i,0]-1;
            int end = commands[i,1];
            int[] arr_copy = new int[end-start];
            
            Array.Copy(array,start,arr_copy,0,end-start);
            Array.Sort(arr_copy);
            
            answer[i] = arr_copy[commands[i,2]-1];
        }
        
        return answer;
    }
}