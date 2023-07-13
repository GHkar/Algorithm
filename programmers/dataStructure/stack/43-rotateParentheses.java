import java.util.*;

// 괄호 회전하기
public class Solution {
    // 괄호가 짝이 맞는가
    private boolean isCorrect(char[] str, int offset){
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < str.length; i++){
            char c = str[(offset + i) % str.length];
            switch (c){
                case '(' -> stack.push(')');
                case '{' -> stack.push('}');
                case '[' -> stack.push(']');
                case ')', '}', ']' -> {
                    if (stack.isEmpty()) return false;
                    if (stack.pop() != c) return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public int solution(String s) {
        char[] str = s.toCharArray();

        int count = 0;

        for(int offset = 0; offset < str.length; offset++){
            if(isCorrect(str, offset)){
                count++;
            }
        }
        return count;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "[](){}";
        int result = answer.solution(input);

        System.out.print(result);
    }
}
