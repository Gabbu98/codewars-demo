// Count the number of Duplicates
// Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

// Example
// "abcde" -> 0 # no characters repeats more than once
// "aabbcde" -> 2 # 'a' and 'b'
// "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
// "indivisibility" -> 1 # 'i' occurs six times
// "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
// "aA11" -> 2 # 'a' and '1'
// "ABBA" -> 2 # 'A' and 'B' each occur twice

// count distinct case-insensitive alphabetic characters and numeric digits which occur more than once in a string

// input: string
// output: number representing count of duplicate letters case-insensitive and numeric digits

// example: aA11 => 2 'a' and '1', ABBA => 2 'A' and 'B'

export function duplicateCount(text: string): number{
  let arr: String[] = text.toLowerCase().split('').sort()
  
  let counter: number = 0;
  let current: String = "";
  let same: boolean = false;
  for(let character of arr) {
    if (current !== character) {
      same = false;
      current = character;
      continue;
    }
    
    if ((current === character) && !same) {
      counter++;
      same = true
      continue;
    }
    
  }
  
  return counter;
}
