// Description:
// There is an array with some numbers. All numbers are equal except for one. Try to find it!

// findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
// findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
// It’s guaranteed that array contains at least 3 numbers.

// The tests contain some very huge arrays, so think about performance.

// This is the first kata in series:

// Find the unique number (this kata)
// Find the unique string
// Find The Unique

export function findUniq(arr: number[]): number {
  console.log(arr)
  // Do the magic
  const value1: number = arr[0];
  const value2: number = arr[1];
  let canProceed: boolean = false;
  if(value1===value2) {
    canProceed=true
  }
  
  if(!canProceed) {
    const value3: number = arr[2];
    if(value3===value1){
      return value2
    }
    return value1
    
  }

  for(var val of arr) {
    if(val!==value1){
      return val
    }
  }

  return -1;
}

// input: array with numbers, all equal except one, find it
// guarantees: array contains at least 3 integers
