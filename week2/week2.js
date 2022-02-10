1.
function calculate(min, max){
  let total = 0;
  for(i = min ;i <= max ;i++ ){
   total+= i;
  }
  console.log(total);
}
  calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6 
  calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30




2.
function avg(data){
  let sum = 0;
  for(i = 0; i < data.count; i++){
    sum+=data.employees[i].salary;
  }
  let x = sum / data.count;
  console.log(x);
}
avg({
  "count":3,
  "employees":[ 
    {
      "name":"John",
      "salary":30000 
    },
    {
      "name":"Bob",
      "salary":60000 },
    {
      "name":"Jenny",
      "salary":50000 
    }
  ]
});
   



3.
function maxProduct(nums){
  let arr=[] ;
  for(i=0 ;i<nums.length ; i++){
     for(j=0 ; j<i ; j++){
       arr.push(nums[i]*nums[j]);      
     }
  }
  console.log(Math.max(...arr));
};

maxProduct([5, 20, 2, 6]) // 得到 120 
maxProduct([10, -20, 0, 3]) // 得到 30 
maxProduct([-1, 2]) // 得到 -2 
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0])




4.
function twoSome(nums,target){
  for(i=0 ;i<nums.length-1 ; i++){
   for(j=i+1 ; j<nums.length ; j++){
     if (nums[i]+nums[j] == target){
     return([i,j]) ;
     }     
   }
  };
}
let result = twoSome([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9




// 5.
function maxZeros(nums){
  let arr = [];
  let count = 0;
  for(i=0 ; i<nums.length ; i++){
      if(nums[i]==0){
          count+=1;
      }else if(nums[i]==1){
          count=0;
      }
      arr.push(count);
  }
  console.log(Math.max(...arr));
}
maxZeros([0, 1, 0, 0]); 
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]); 
maxZeros([0, 0, 0, 1, 1]);