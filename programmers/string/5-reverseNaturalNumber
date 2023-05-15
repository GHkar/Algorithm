import java.util.Arrays;

// 자연수 뒤집어 배열로 만들기
public class Solution {

    public int[] solution(long n){
        // 입력받은 숫자를 문자열로 변환
        String str = Long.toString(n);
        // 문자열 뒤집기
        String reversed = new StringBuilder(str).reverse().toString();
        // 뒤집힌 문자열을 문자의 배열로 변환
        char[] arr = reversed.toCharArray();
        // 배열의 각 문자를 정수로 변환
        int[] result = new int[arr.length];
        for (int i = 0; i < result.length; i++){
            result[i] = arr[i] - '0';
        }

        return result;
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        long input = 12345;
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}

