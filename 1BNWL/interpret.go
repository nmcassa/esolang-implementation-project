package main

import (
	"fmt"
	"errors"
	"os"
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

	oob := errors.New("Out of Bounds Error")

	pointer := 0
	var mem [100]bool
	i := 0

	for i < len(str) {
		item := str[i]

		/* < */
		if item == 60 {
			if pointer == 0 {
				panic(oob)
			}
			pointer = pointer - 1
		}

		/* > */
		if item == 62 {
			if pointer == len(mem)-1 {
				panic(oob)
			}
			pointer = pointer + 1
		}

		/* + */
		if item == 43 {
			mem[pointer] = true
		}

		/* - */
		if item == 45 {
			mem[pointer] = false
		}

		/* [ */
		if item == 91 {
			if !mem[pointer] {
				for str[i] != 93 {
					i += 1
					if i == len(str) {
						panic(oob)
					}
				}
				i += 1
			}
		}

		/* ] */
		if item == 93 {
			if mem[pointer] {
				for str[i] != 91 {
					i -= 1
					if i == -1 {
						panic(oob)
					}
				}
			}
		}

		/* . */
		if item == 46 {
			if mem[pointer]{
				fmt.Print("1")
			} else {
				fmt.Print("0")
			}
		}
		i = i + 1
	}
}