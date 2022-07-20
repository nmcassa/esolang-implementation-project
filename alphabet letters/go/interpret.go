package main

import (
	"os"
	"fmt"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {

	dat, err := os.ReadFile(os.Args[1])
	check(err)

	str := string(dat)

	pointer := 0
	num := 0
	var mem [100]rune

	for _, item := range str {

		/* 'p' */
		if item == 112 {
			num = 0
		}
		
		/* 'a' */
		if item == 97 {
			num = num + 1
		}

		/* 's' */
		if item == 115 {
			num = num - 1
		}

		/* 'z' */
		if item == 122 {
			mem[pointer] = rune(num)
			pointer = pointer + 1
		}

		/* 'c' */
		if item == 99 {
			for _, letter := range mem {
				fmt.Printf(string(letter))
			}
		}

		/* 'e' */
		if item == 101 {
			os.Exit(3)
		}

	}

}