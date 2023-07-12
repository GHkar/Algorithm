import java.util.*;

// 사칙연산
/*
* + : 양쪽 모두 커야 함
* - : 왼쪽이 크고 오른쪽은 작아야 함
*  */
public class Solution {
    private final int[][] maxMem = new int[202][202];
    private final int[][] minMem = new int[202][202];
  
    // 최댓값
    private int max(int start, int end, String[] arr){
        if (maxMem[start][end] != Integer.MIN_VALUE){
            return maxMem[start][end];
        }

        if (end - start == 1) return Integer.parseInt(arr[start]);

        int max = Integer.MIN_VALUE;
        for(int i = start + 1; i < end; i += 2){
            int l = max(start, i, arr);
            int v;
            if (arr[i].equals("+")){
                int r = max(i+1, end, arr);
                v = l + r;
            } else {
                int r = min(i + 1, end, arr);
                v = l - r;
            }
            if(v > max) max = v;
        }
        return maxMem[start][end] = max;
    }

    // 최솟값
    private int min(int start, int end, String[] arr){
        if (minMem[start][end] != Integer.MIN_VALUE){
            return minMem[start][end];
        }

        if (end - start == 1) return Integer.parseInt(arr[start]);

        int min = Integer.MAX_VALUE;
        for(int i = start + 1; i < end; i += 2){
            int l = min(start, i, arr);
            int v;
            if (arr[i].equals("+")){
                int r = min(i+1, end, arr);
                v = l + r;
            } else {
                int r = max(i + 1, end, arr);
                v = l - r;
            }
            if(v < min) min = v;
        }
        return minMem[start][end] = min;
    }

    public int solution(String[] arr) {
        // 메모이제이션 배열 초기화
        for(int[] row : maxMem){
            Arrays.fill(row, Integer.MIN_VALUE);
        }
        for(int[] row : minMem){
            Arrays.fill(row, Integer.MIN_VALUE);
        }

        return max(0, arr.length, arr);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[] input = {"1", "-", "3", "+", "5", "-", "8"};
        int result = answer.solution(input);

        System.out.print(result);
    }
}
