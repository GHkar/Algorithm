import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// 하노이의 탑
public class Solution {
    // 재귀 method
    private void hanoi (int n, int from, int to, List<int[]> process) {
        if ( n == 1 ){
            process.add(new int[] {from, to});
            return;
        }

        // 점화식
        int empty = 6 - from - to;

       hanoi(n-1, from, empty, process);
       hanoi(1, from, to, process);
       hanoi(n-1, empty, to, process);
    }
    public int[][] solution(int n){
        List<int[]> process = new ArrayList<>();
        hanoi(n, 1, 3, process);
        return process.toArray(new int[0][]);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input = 2;
        int[][] result = answer.solution(input);

        System.out.print(Arrays.deepToString(result));
    }
}
