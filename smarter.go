package main

import (
	"fmt"
	"time"
	"strings"
)

func generateString(n int) string {
	var bbuf strings.Builder
	bbuf.Grow(n*2)
	for i := 0; i < n; i++ {
		fmt.Fprintf(&bbuf, "12")
	}
	b:=bbuf.String()
	var resbuf strings.Builder
	resbuf.Grow(n)
	for _, c := range b {
		if c == '1' {
			fmt.Fprintf(&resbuf, string(c))
		}
	}
	return resbuf.String()
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

