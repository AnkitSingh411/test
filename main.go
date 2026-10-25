package main

import (
	"fmt"
	"strings"
)

func greet(name string) string {
	return fmt.Sprintf("Hello, %s!", name)
}

func add(a, b int) int {
	return a + b
}

func isEven(n int) bool {
	return n%2 == 0
}

func shout(s string) string {
	return strings.ToUpper(s)
}

func main() {
	fmt.Println(greet("world"))
	fmt.Println("Sum:", add(2, 3))
	fmt.Println("Even?", isEven(4))
	fmt.Println(shout("welcome to the sample project"))
}
