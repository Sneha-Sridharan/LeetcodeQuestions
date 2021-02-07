int search(int* nums, int numsSize, int target){
    int i,pivotind=1,flag=0,first,last,mid;
    if(nums[0]==target) return 0;
    for(i=1;i<numsSize&&flag==0;i++)
    {
        if(nums[i]==target)
            return i;
        if(nums[i-1]>nums[i])
        {
            pivotind=i;
            flag=1;
        }
    }
    first=pivotind;
    last=numsSize-1;
    while(first<=last)
    {
        mid=(first+last)/2;
        if(nums[mid]==target)
            return mid;
        else if(target<nums[mid])
            last=mid-1;
        else
            first=mid+1;
    }
    return -1;
}