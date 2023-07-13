import java.util.*;

// 주식 가격
public class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < prices.length; i++){
            while(!stack.isEmpty() && prices[stack.peek()] > prices[i]){
                int index = stack.pop();
                answer[index] = i - index;
            }
            stack.push(i);
        }

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
