#!/bin/bash
# 向终端输入一条命令并回车：t.sh <pid> <命令文本> [等待秒数]
MAC="/Users/liuchenxi/Library/Application Support/Doubao/Default/.doubao/agent_mode/workspace/.user_skills/huashu-mac-use/scripts/mac"
"$MAC" type "$1" "$2"
sleep 0.35
"$MAC" key "$1" 36 --force
sleep ${3:-0.7}
