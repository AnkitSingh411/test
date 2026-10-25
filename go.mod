module testproject

go 1.21

require (
	example.com/mylinter v0.0.0
	golang.org/x/tools v0.20.0
)

replace example.com/mylinter => ./mylinter
