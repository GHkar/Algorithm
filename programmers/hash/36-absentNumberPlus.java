import java.util.HashSet;
import java.util.Set;

// 없는 숫자 더하기
public class Solution {
    public int solution(int[] numbers) {
        Set<Integer> set = new HashSet<Integer>();
        for(int v : numbers) {
            set.add(v);
        }

        int sum = 0;
        for (int n = 0; n <= 9; n++){
            if(set.contains(n)) continue;
            sum += n;
        }
        return sum;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {1,2,3,4,6,7,8,0};
        int result = answer.solution(input);

        System.out.print(result);
    }
}
