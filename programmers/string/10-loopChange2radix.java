import java.util.Arrays;

// 이진 변환 반복하기
public class Solution {

    // 문자열에 포함된 0의 개수 세기
    private int countZeros(String s){
        int zeros = 0;
        for (char c : s.toCharArray()){
            if(c=='0') zeros++;
        }
        return zeros;
    }

    public int[] solution(String s){
        int loop = 0;
        int removed = 0;

        // s가 "1"이 될 때까지 반복
        while (!s.equals("1")){
            // loop, removed 누적
            int zeros = countZeros(s);
            loop += 1;
            removed += zeros;

            // 문자열 s 변환
            int ones = s.length() - zeros;
            s = Integer.toString(ones, 2);

        }
        return new int[] {loop, removed};
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "110010101001";
        int[] result = answer.solution(input);

        System.out.print(Arrays.toString(result));
    }
}

