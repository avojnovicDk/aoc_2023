package main
import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	digits := map[string]int{
	    "one": 1,
	    "two": 2,
	    "three": 3,
	    "four": 4,
	    "five": 5,
	    "six": 6,
	    "seven": 7,
	    "eight": 8,
	    "nine": 9,
	}

    readFile, err := os.Open("input.txt")
    if err != nil {
        fmt.Println(err)
    }

    fileScanner := bufio.NewScanner(readFile)
    fileScanner.Split(bufio.ScanLines)
    sum := 0

    for fileScanner.Scan() {
     	line := fileScanner.Text()
      	foundDigit := -1

     	for _ = range len(line) {
        	for word, digit := range digits {
	          	if (strings.HasPrefix(line, word) || strings.HasPrefix(line, strconv.Itoa(digit))) {
	           		if (foundDigit == -1) {
	             		foundDigit = digit
	                    sum += foundDigit * 10
	             	} else {
	                    foundDigit = digit
	              	}
	            }
         	}
          	line = line[1:]
      	}
	    sum += foundDigit
    }
   	fmt.Println(sum)
    readFile.Close()
}
