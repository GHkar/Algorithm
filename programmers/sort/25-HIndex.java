import java.util.*;

// H-Index
public class Solution {
    // h의 조건을 검사 - n회 이상 인용된 논문이 n개 이상인지 검사 - 뒤에서 n번째 논문이 n회 이상 인용되었는지 검사
    private boolean isValid(int[] citations, int h){
        int index = citations.length - h;
        return citations[index] >= h;
    }
    public int solution(int[] citations) {
        Arrays.sort(citations);
        for (int h = citations.length; h >= 1; h--){
            if (isValid(citations, h)) return h;
        }
        return 0;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int[] input = {3, 0, 6, 1, 5};
        int result = answer.solution(input);

        System.out.print(result);
    }
}
