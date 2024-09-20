/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
  let a = 0;
  let b = 1;
  while (1) {
      yield a;
      let temp = b;
      b = a + b;
      a = temp;
  }
};

/**
* const gen = fibGenerator();
* gen.next().value; // 0
* gen.next().value; // 1
*/