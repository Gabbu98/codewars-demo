/*
Package ffc provides utilities for calculating expected donations.

The accounts of the "Fat to Fit Club (FFC)" association are supervised by John as a volunteered accountant.
The association is funded through financial donations from generous benefactors.

John keeps track of the donations. For example, he has a list of the first n donations:
[14, 30, 5, 7, 9, 11, 15]

He wants to calculate how much the next benefactor should donate so that the average of the first (n + 1) donations 
reaches a desired target average. For instance, he wants the average to reach 30.

After calculating, he initially thought the next donation should be 149, but he doubts his result.
This function helps him calculate the correct expected donation.

Task:
- The function should return the expected donation amount (rounded up to the next integer) that will allow the average to reach the desired value.
- If the computed donation is non-positive (<= 0), the function should either return this value or throw an error to clearly show that John's expectation is not achievable.

Notes:
- All donations and the desired new average can be integers or floats.
- The array of donations can be empty.
- Example results:
    - donations: [14, 30, 5, 7, 9, 11, 15], desired average: 92 → result: 645
    - donations: [14, 30, 5, 7, 9, 11, 15], desired average: 2  → result: non-positive value (error)
*/

package kata
import (
  "fmt"
  "math"
)

func Sum(arr []float64) float64 {
  var sum float64
  fmt.Println(arr)
  for i:=0; i<len(arr); i++ {
    sum = float64(arr[i]) + sum
    fmt.Println(sum)
  }
  return sum
}

func NewAvg(arr []float64, navg float64) int64 {
  x := new(float64)
  lengthOfArray := len(arr) + 1
  
  *x = (navg * float64(lengthOfArray)) - Sum(arr)
  
  if *x <= 0 { return -1 }
  
  return int64(math.Round(*x))
}
