package main
import (
	"bufio"
	"fmt"
	"os"
)

func main() {
    readFile, err := os.Open("input.txt")
    if err != nil {
        fmt.Println(err)
    }

    fileScanner := bufio.NewScanner(readFile)
    fileScanner.Split(bufio.ScanLines)

    sum := 0
    for fileScanner.Scan() {
    	digit := -1
	    for _, char := range fileScanner.Text() {
			if (char >= 48 && char <= 58) {
				if (digit == -1) {
					digit = int(char) - 48
					sum += digit * 10
				} else {
					digit = int(char) - 48
				}
			}
	    }
		sum += digit
    }
    readFile.Close()

    fmt.Println(sum)
}
