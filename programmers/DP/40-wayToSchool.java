import java.util.*;

// 등굣길
public class Solution {
    private final int[][] mem = new int[101][101];
    // 재귀 메서드
    private int count (int x, int y, int w, int h, boolean[][] isPuddle) {
        // 지도를 벗어나거나, 웅덩이면 갈 수 없음
        if (x > w || y > h) return 0;
        if(isPuddle[y][x]) return 0;

        if(mem[x][y] != -1) return mem[x][y];
        // 학교 도착
        if(x == w && y == h) return 1;

        int total = count(x+1, y, w, h, isPuddle) + count(x, y+1, w, h, isPuddle);
        return mem[x][y] = total % 1000000007;
    }

    public int solution(int m, int n, int[][] puddles) {
        // 메모이제이션 배열 초기화
        for(int[] row : mem){
            Arrays.fill(row, -1);
        }

        // 웅덩이 표시
        boolean[][] isPuddle = new boolean[n+1][m+1];
        for(int[]p : puddles){
            isPuddle[p[1]][p[0]] = true;
        }
        return count(1,1,m,n,isPuddle);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input1 = 4;
        int input2 = 3;
        int input3[][] = {{2,2}};
        int result = answer.solution(input1, input2, input3);

        System.out.print(result);
    }
}
