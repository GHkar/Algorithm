import java.util.*;

// 소수 찾기
public class Solution {
    // 소수 검사
    private boolean isPrime(int n){
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++){
            if (n % i == 0) return false;
        }
        return true;
    }

    // 재귀 메서드
    private void getPrimes(int acc, int[] numbers, boolean[] isUsed, Set<Integer> primes){
        // 점화식 구현
        if (isPrime(acc)) primes.add(acc);

        // 상태 전이 구현
        for (int i = 0; i < numbers.length; i++){
            if (isUsed[i]) continue;
            // numbers[i]로 상태 전이 진행 (자릿수를 늘려주기 위해 10을 곱함)
            int nextAcc = acc * 10 + numbers[i];
            isUsed[i] = true;
            getPrimes(nextAcc, numbers, isUsed, primes);
            isUsed[i] = false;
        }
    }

    public int solution(String nums){
        Set<Integer> primes = new HashSet<>();
        int[] numbers = nums.chars().map(c -> c - '0').toArray();
        getPrimes(0, numbers, new boolean[numbers.length], primes);
        return primes.size();
    }

    // 실행
    public static void main(String[] args)
    {
        Solution answer = new Solution();
        String input = "011";
        long result = answer.solution(input);

        System.out.print(result);
    }
}
