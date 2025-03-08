class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        // length of nums
        int n = nums.length;
        int[] seen = new int[51];
        int res = 0;
        for (int i = 0; i < n; i++) {
            seen[nums[i]]++;
            if (seen[nums[i]] == 2) {
                res ^= nums[i];
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] tests = {
                { 1, 2, 1, 3 },
                { 1, 2, 3 },
                { 1, 2, 2, 1 }
        };
        int[] res = {1,0,3};
        for (int i = 0; i < tests.length; i++) {
            int output = sol.duplicateNumbersXOR(tests[i]);
            System.out.println(output);
            System.out.println(output == res[i]);
        }
    }
}