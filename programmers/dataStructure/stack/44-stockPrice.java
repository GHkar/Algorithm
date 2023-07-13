import java.util.*;

// 주식 가격
public class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();

        // 더 작은 값이 나타나면 스택 순회를 통해 더 큰 값들과 짝 지어줌
        for (int i = 0; i < prices.length; i++){
            while(!stack.isEmpty() && prices[stack.peek()] > prices[i]){
                int index = stack.pop();
                answer[index] = i - index;
            }
            stack.push(i);
        }

        // 남아 있는 값들은 가격이 내리지 않은 값들, 총 길이와 비교하여 날을 세 줌
        while(!stack.isEmpty()){
            int index = stack.pop();
            answer[index] = prices.length - index - 1;
        }
        return answer;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {1, 2, 3, 2, 3};
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}
