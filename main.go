package main

import (
	"fmt"
	"time"
)

func generateString(n int) string {
	res := ""
	b := ""
	for i := 0; i < n; i++ {
		b += "12"
	}
	for _, c := range res {
		if c == '1' {
			res += string(c)
		}
	}
	return res
}

func main() {
	for i := 1; i < 7; i++ {
		iterations := intPow(10, i)
		start := time.Now()
		generateString(iterations)
		elapsed := time.Since(start)
		fmt.Println(iterations, elapsed.Seconds())
	}
}

func intPow(base, exp int) int {
	result := 1
	for exp != 0 {
		if exp%2 != 0 {
			result *= base
		}
		exp /= 2
		base *= base
	}
	return result
}

