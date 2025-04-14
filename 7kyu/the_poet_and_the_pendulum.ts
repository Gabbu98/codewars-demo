// Task
// Given an array/list [] of n integers , Arrange them in a way similar to the to-and-fro movement of a Pendulum

// The Smallest element of the list of integers , must come in center position of array/list.

// The Higher than smallest , goes to the right .
// The Next higher number goes to the left of minimum number and So on , in a to-and-fro manner similar to that of a Pendulum.

// pendulum
// input: array of integers. arrange in pendulum form
// smallest element at center
// higher -> right, higher -> left ...

// example: [6,6,8,5,10] => [10,6,5,6,8]
export function pendulum(values: number[]) {
  // your code here
  
  // sort
  values.sort((n1,n2) => n1 - n2)

  let result: number[] = [];
  result.push(values[0])
  let isRightTurn: boolean = true;
  
  for(var val of values.slice(1,values.length)) {
    if(isRightTurn){
      result.push(val)
      isRightTurn = false
      
      continue
    }
    
    result.unshift(val)
    isRightTurn = true
    
  }
  return result
}

// sort
// maintain two lists push to one and then the other
