// 3진법 뒤집기
public class Solution {
    // 문자열 압축 후 압축된 문자열의 길이 반환

    public int solution(int n){
        // 정수를 3진법으로 변환
        String str = Integer.toString(n, 3);

        // 변환된 문자열 뒤집기
        String reversed = new StringBuilder(str).reverse().toString();

        // 뒤집은 문자열을 정수로 변환
        return Integer.valueOf(reversed, 3);
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        int input = 125;
        int result = answer.solution(input);

        System.out.print(result);
    }
}

