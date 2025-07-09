class Solution {
    public int maxFreeTime(int event, int k, int[] start, int[] end) {
        int n = end.length;
        int dif[] = new int[n+1];

        dif[0] = start[0];
        for(int i=1;i<n;i++) dif[i] = start[i]-end[i-1];
        dif[n] = event-end[n-1];

        int lf=0; int rf=0;
        int sum=0; int ans=0;
        while(rf<=n){
            sum += dif[rf];
            if(rf-lf+1==(k+1)){
                ans = Math.max(ans,sum);
                sum -= dif[lf];
                lf++;
            }
            rf++;
        }
        return ans;
    }
}