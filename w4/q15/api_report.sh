#!/bin/bash

curl -fsS http://127.0.0.1:8000/packages.json |
jq -r '
  [
    "# Package Report",
    "",
    "| name | version | downloads |",
    "| --- | --- | ---: |"
  ]
  + (
    [.[] | select(.status == "active" and .downloads >= 100)]
    | sort_by(-.downloads, .name)
    | map("| \(.name) | \(.version) | \(.downloads) |")
  )
  | .[]
' > summary.md
