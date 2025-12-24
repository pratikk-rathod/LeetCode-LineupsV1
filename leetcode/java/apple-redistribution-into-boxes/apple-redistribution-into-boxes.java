class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        // int ans=0;
        int ans =0;
        int sum1 = 0;
        // summ=
        // Method 2: Using IntStream.of().sum()
        int sum2 = IntStream.of(apple).sum();
        // System.out.println("The sum using IntStream.of() is: " + sum2); // Output: 150
        Arrays.sort(capacity);
        System.out.println(capacity);
        for(int i=capacity.length-1;  i >= 0; i--){
        System.out.println("The sum using IntStream.of() is: " + i); // Output: 150
        sum1+= (capacity[i]);
        ans+=1;
        if(sum1>=sum2){
            return ans;
        }
        }
        return sum2;
    }
}