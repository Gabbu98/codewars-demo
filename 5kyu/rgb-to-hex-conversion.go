// The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

// Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

// Examples (input --> output):
// 255, 255, 255 --> "FFFFFF"
// 255, 255, 300 --> "FFFFFF"
// 0, 0, 0       --> "000000"
// 148, 0, 211   --> "9400D3"

package kata

import (
  "math"
  "strconv"
)

func RGB(r, g, b int) string {
  var redHex string = Convertor(r)  
  var greenHex string = Convertor(g)
  var blueHex string = Convertor(b)
   
  // Your code here
  return redHex+greenHex+blueHex
}

func Convertor(input int) string {
  
  if(input < 0) {
    return "00"
  }
  
  if(input>255) {
    return "FF"
  }
  
  hexValues := [6]string{"A","B","C","D","E","F"}

  var divisible int = 16
  
  var result float64 = float64(input) / float64(divisible)
  
  if math.IsNaN(result) {
    result = 0.0
  }
 
  // find hex value in digit form
  resultRounded := int(math.Floor(result))  // find out level of rounding required
  
  remainder := input - (resultRounded * 16)

  var hexValue1 string
  var hexValue2 string
  
  if resultRounded > 9 {
    resultRounded = resultRounded -10
    hexValue1 = hexValues[resultRounded]
  } else {
    hexValue1 = strconv.Itoa(resultRounded) 
  }
   
  if remainder > 9 {
    remainder = remainder - 10
    hexValue2 = hexValues[remainder]
  } else {
    hexValue2 = strconv.Itoa(remainder)
  }
 
  return hexValue1 + hexValue2
}

func indexOf(element string, data []string) int {
  for i, x := range data {
    if element == x {
      return i
    }
  }
  return -1 // not found
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
package kata_test

import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)

var _ = Describe("Test Example", func() {
  It("should test that the solution returns the correct value", func() {
    Expect(RGB(0,0,0)).To(Equal("000000"))
    Expect(RGB(1,2,3)).To(Equal("010203"))
    Expect(RGB(255,255,255)).To(Equal("FFFFFF"))
    Expect(RGB(254,253,252)).To(Equal("FEFDFC"))
    Expect(RGB(-20,275,125)).To(Equal("00FF7D"))
  })
})
