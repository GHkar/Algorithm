import java.util.*;

// 올바른 괄호
public class Solution {
    public boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()){
            switch (c){
                case '(' -> stack.push(c);
                case ')' -> {
                    if (stack.isEmpty()) return false;
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "()()";
        boolean result = answer.solution(input);

        System.out.print(result);
    }
}
