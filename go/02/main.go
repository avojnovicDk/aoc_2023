package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func GetMinimumCubes(games string) map[string]int {
	min_cubes := map[string]int{"red": 0, "green": 0, "blue": 0}
	for _, game := range strings.Split(games, ";") {
		for _, group := range strings.Split(game, ",") {
			single_color := strings.Split(strings.TrimSpace(group), " ")
			curr_num, _ := strconv.Atoi(single_color[0])

			if curr_num > min_cubes[single_color[1]] {
				min_cubes[single_color[1]] = curr_num
			}
		}
	}
	return min_cubes
}

func main() {
	readFile, _ := os.Open("input.txt")

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	sum_pt1, sum_pt2 := 0, 0

	for fileScanner.Scan() {
		result := strings.Split(fileScanner.Text(), ":")
		minCubes := GetMinimumCubes(result[1])

		if minCubes["red"] <= 12 && minCubes["green"] <= 13 && minCubes["blue"] <= 14 {
			game_number, _ := strconv.Atoi(strings.Split(result[0], " ")[1])
			sum_pt1 += game_number
		}

		sum_pt2 += minCubes["red"] * minCubes["green"] * minCubes["blue"]
	}

	fmt.Printf("sum part 1: %d\n", sum_pt1)
	fmt.Printf("sum part 2: %d\n", sum_pt2)
	readFile.Close()
}
