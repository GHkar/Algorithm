import java.util.*;

// K번째 수
public class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i= 0; i < answer.length; i++){
            int[] command = commands[i];
            // 정답 구해서 answer[i]에 넣기
            int from = command[0] - 1;
            int to = command[1];
            int k = command[2] - 1;

            int[] sub = Arrays.copyOfRange(array, from, to);
            Arrays.sort(sub);
            answer[i] = sub[k];
        }
        return answer;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input1 = {1, 5, 2, 6, 3, 7, 4};
        int[][] input2 = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
        int[] result = answer.solution(input1, input2);

        System.out.print(Arrays.toString(result));
    }
}
