/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
  function order(a, b) {
      return fn(a) - fn(b);
  }
  return arr.sort(order);
};