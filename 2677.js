/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
  let subsize = 0;
  let chunks = 0;
  const chunked = [];

  for (let i = 0; i < arr.length; i++) {
      if (subsize == 0) {  // start of chunk
          chunked[chunks] = [];
          subsize++;
      }
      chunked[chunks].push(arr[i]);
      if (subsize == size) {  // end of chunk, reset and create new chunk
          subsize = 0;
          chunks++;
      }
      else {  // continue chunk
          subsize++;
      }
  }
  return chunked;
};