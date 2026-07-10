/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  let ar = [0,1];
    for(let i=0; i<n; i++){

        let newVal = ar[0] + ar[1];
        ar[0] = ar[1];
        ar[1] = newVal;

    }

    return ar[1];


};