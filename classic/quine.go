/*
 * Go Quine - 经典实现
 * 
 * 运行和验证:
 *     go run quine.go | diff - quine.go
 */

package main

import "fmt"

func main() {
	s := "package main\n\nimport \"fmt\"\n\nfunc main() {\n\ts := %c%s%c\n\tfmt.Printf(s, 34, s, 34)\n}\n"
	fmt.Printf(s, 34, s, 34)
}
