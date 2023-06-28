import java.util.*;

// 두 개 뽑아서 더하기
public class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < numbers.length; i++){
            for (int j = i + 1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }
        return set.stream().mapToInt(Integer::intValue).sorted().toArray();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {2,1,3,4,1};
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}
