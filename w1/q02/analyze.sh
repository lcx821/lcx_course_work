#!/bin/bash

# 检查文件是否存在
if [ ! -f "$1" ]; then
    echo "错误：文件不存在：$1" >&2
    exit 1
fi

echo "HTTP 5xx 数量最多的前 2 个 path："

awk -F',' 'NR > 1 && $4 >= 500 && $4 < 600 {count[$3]++} END {for (path in count) print path, count[path]}' "$1" |
sort -k2,2nr -k1,1 |
head -n 2

echo
echo "平均 latency_ms："

awk -F',' 'NR > 1 {sum += $5; count++} END {printf "%.2f\n", sum / count}' "$1"
