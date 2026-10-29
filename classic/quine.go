// Quine in Go - verify: go run quine.go | diff - quine.go
package main

import "fmt"

func main() {
	s := "// Quine in Go - verify: go run quine.go | diff - quine.go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\ts := %q\n\tfmt.Printf(s, s)\n}\n"
	fmt.Printf(s, s)
}
