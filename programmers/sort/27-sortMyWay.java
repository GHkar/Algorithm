import java.util.*;

// 문자열 내 마음대로 정렬하기
public class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, (s1, s2) -> {
            if (s1.charAt(n) != s2.charAt(n)) {
                return s1.charAt(n) - s2.charAt(n);
            }
            return s1.compareTo(s2);
        });
        return strings;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String[] input1 = {"sun", "bed", "car"};
        int input2 = 1;
        String[] result = answer.solution(input1, input2);

        System.out.print(Arrays.toString(result));
    }
}
