using System;

public class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Array.Sort(times);
        long start = 0;  
        long end = (long)times[times.Length-1]*n;   // 입국심사 걸리는 시간 최댓값(모두 오래 걸리는 사람한테만 받는 경우)
        
        while (start <= end)
        {
            long mid = (start+end) / 2;
            long people = 0; // mid 시간에 검사 받는 사람 수
            foreach (var time in times)
            {
                // 1명당 times[i]만큼 걸리면 mid 시간 동안 심사하는 사람 수
                people += mid / time;
            }
            if (people < n)
            {
                start = mid + 1;
            }
            else
            {
                answer = mid;
                end = mid - 1;
            }
        }        
        
        return answer;
    }
}