// 순위
public class Solution {
    // 한 선수가 이긴 선수들의 수 세기
    private int countForward(int u, boolean[][] graph, boolean[] isVisited){
        int count = 1;
        // 재귀 진행
        for(int v = 0; v < graph[u].length; v++){
            if(!graph[u][v] || isVisited[v]) continue;
            isVisited[v] = true;
            count += countForward(v, graph, isVisited);
        }
        return count;
    }

    // 한 선수가 진 선수들의 수 세기
    private int countBackward(int u, boolean[][] graph, boolean[] isVisited){
        int count = 1;
        // 재귀 진행
        for(int v = 0; v < graph[u].length; v++){
            if(!graph[v][u] || isVisited[v]) continue;
            isVisited[v] = true;
            count += countBackward(v, graph, isVisited);
        }
        return count;
    }

    public int solution(int n, int[][] results) {
        boolean[][] graph = new boolean[n][n];
        // 이긴 여부
        for(int[] edge : results){
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            graph[u][v] = true;
        }

        int count = 0;
        for(int u = 0; u < n; u++){
            int wins = countForward(u, graph, new boolean[n]) - 1;
            int loses = countBackward(u, graph, new boolean[n]) - 1;
            if(wins + loses + 1 ==n){
                count++;
            }
        }
        return count;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input1 = 5;
        int[][] input2 = {{4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}};
        int result = answer.solution(input1, input2);

        System.out.print(result);
    }
}
