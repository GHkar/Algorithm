import java.util.*;

// 정수 삼각형
/*
점화식 : (x ,y) = [x, y] + MAX{(x, y+1), (x+1, y+1)}
*/
public class Solution {
    private final int[][] mem = new int[501][501];
    private int max (int x, int y, int[][] triangle) {
        if (y == triangle.length) return 0;
        if(mem[x][y] != -1) return mem[x][y];

        return mem[x][y] = triangle[y][x] + Math.max(
                max(x, y+1, triangle),
                max(x+1, y+1, triangle));
    }

    public int solution(int[][] triangle) {
        for(int[] row : mem){
            Arrays.fill(row, -1);
        }
        return max(0, 0, triangle);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input[][] = {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
        int result = answer.solution(input);

        System.out.print(result);
    }
}
