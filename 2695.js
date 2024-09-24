/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
  this.values = nums;
};

/**
* @return {number}
*/
ArrayWrapper.prototype.valueOf = function() {
  let sum = 0;
  for (let i = 0; i < this.values.length; i++) {
      sum += this.values[i];
  }
  return sum;
}

/**
* @return {string}
*/
ArrayWrapper.prototype.toString = function() {
  let output = "[";
  for (let i = 0; i < this.values.length - 1; i++) {
      output += this.values[i] + ",";
  }
  if (this.values.length > 0) {  // check if element exists in array
      output += this.values[this.values.length - 1] + "]";
  }
  else {  // empty array, close bracket immediately
      output += "]";
  }
  return output;
}

/**
* const obj1 = new ArrayWrapper([1,2]);
* const obj2 = new ArrayWrapper([3,4]);
* obj1 + obj2; // 10
* String(obj1); // "[1,2]"
* String(obj2); // "[3,4]"
*/