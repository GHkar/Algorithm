import java.util.HashSet;
import java.util.Set;

// 중복된 문자 제거
public class Solution {
    public String solution(String myString) {
        Set<Character> used = new HashSet<>();
        StringBuilder builder = new StringBuilder();

        // 사용한 적 없으면 추가
        for(char c : myString.toCharArray()) {
            if(used.contains(c)) continue;
            used.add(c);
            builder.append(c);
        }
        return builder.toString();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "people";
        String result = answer.solution(input);

        System.out.print(result);
    }
}
