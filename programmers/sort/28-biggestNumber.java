import java.util.*;
import java.util.stream.Collectors;

// 가장 큰 수
public class Solution {
    public String solution(int[] numbers) {
        return Arrays.stream(numbers)
                .mapToObj(String::valueOf)
                .sorted((s1, s2) -> {
                    int original = Integer.parseInt(s1 + s2);
                    int reversed = Integer.parseInt(s2 + s1);
                    return reversed - original;
                })
                .collect(Collectors.joining(""))
                .replaceAll("^0+", "0");    // 0이 여러개 나타나면 0 하나로 바꿈
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {6, 10, 2};
        String result = answer.solution(input);

        System.out.print(result);
    }
}
