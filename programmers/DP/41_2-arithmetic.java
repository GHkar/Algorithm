import java.util.*;

// 사칙연산
/*
* + : 양쪽 모두 커야 함
* - : 왼쪽이 크고 오른쪽은 작아야 함
* type = 0 최댓값, type = 1 최솟값
*  */
public class Solution {
    // 초깃값
    private static final int[] INIT ={
            Integer.MIN_VALUE,
            Integer.MAX_VALUE,
    };

    // 결과를 최댓값/최솟값과 비교
    private interface IntComparator extends Comparator<Integer> {
    }
    private static final IntComparator[] COMP = {
            (a, b) -> Integer.compare(a,b),     // 최댓값 v > result
            (a, b) -> Integer.compare(b,a),     // 최솟값 v < result
    };

    // 메모이제이션
    private final int[][][] mem = new int[202][202][2];

    // 재귀 함수
    private int compute(int start, int end, int type, String[] arr){
        if (mem[start][end][type] != Integer.MIN_VALUE){
            return mem[start][end][type];
        }

        if (end - start == 1) return Integer.parseInt(arr[start]);

        int result = INIT[type];
        for(int i = start + 1; i < end; i += 2){
            int l = compute(start, i, type, arr);
            int v;
            if (arr[i].equals("+")){
                int r = compute(i+1, end, type, arr);
                v = l + r;
            } else {
                int r = compute(i + 1, end, 1 - type, arr);
                v = l - r;
            }
            if(COMP[type].compare(v, result) > 0) result = v;
        }
        return mem[start][end][type] = result;
    }

    public int solution(String[] arr) {
        // 메모이제이션 배열 초기화
        for(int[][] m : mem){
            for (int[] row : m) {
                Arrays.fill(row, Integer.MIN_VALUE);
            }
        }

        return compute(0, arr.length, 0, arr);
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
